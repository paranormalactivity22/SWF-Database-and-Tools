import re, glob, sys, random

swfname = (input if sys.version_info[0] == 3 else raw_input)('-> Enter swf name please (without .swf) -> ')

files, _files = glob.glob('{}-0/*.class.asasm'.format(swfname)), {}

def _open(*args):
    return (open(*args) if sys.version_info[0] == 2 else open(*args, encoding='utf-8'))

def rf(f):
    if f in _files:
        return _files.get(f)
    with _open(f, 'r') as x:
        y = x.read()
    _files[f] = y
    return y

def sf(f, c):
    _files[f] = c
    with _open(f, 'w') as x:
        x.write(c)

def fixLanguages():
    urlvar = None
    changed = False
    for file in files:
        c = rf(file)
        if 'langues/tfz_' in c:
            ls = c.split('\n')
            for i, l in enumerate(ls):
                if 'langues/tfz_' in l:
                    ls[i] = l.replace('tfz_', 'tfm-')
                    urlvar = ls[i - 1].split('"')[3]
                    changed = True
                    break
            sf(file, '\n'.join(ls))
            break
        elif 'langues/tfm-' in c:
            ls = c.split('\n')
            for i, l in enumerate(ls):
                if 'langues/tfm-' in l:
                    urlvar = ls[i - 1].split('"')[3]
                    break
            break

    for file in files:
        c = rf(file)
        if urlvar in c and 'langues/tfm-' not in c:
            ls = c.split('\n')
            for i, l in enumerate(ls):
                if urlvar in l:
                    for ii in range(i, 0, -1):
                        ll = ls[ii]
                        if ll.replace(' ', '') == 'setlocal2' and 'MultinameL' in ls[ii - 2]:
                            conds = [int(cond) for cond in re.findall('L(\d*):', c)]
                            cond = random.choice(list(set(range(min(conds) + 1, max(conds))) - set(conds)))
                            ls = ls[:ii+2] + [
                                '     getlocal2',
                                '     pushstring "br"',
                                '     equals',
                                '     iffalse L{}'.format(cond),
                                '     pushstring "pt-"',
                                '     getlocal2',
                                '     add',
                                '     setlocal2',
                                '',
                                'L{}:'.format(cond)
                            ] + ([
                                '     getlocal2',
                                '     pushstring ".gz"',
                                '     add',
                                '     setlocal2',
                            ] if changed else []) + ls[ii+2:]
                            break
                    break
            sf(file, '\n'.join(ls))
            break

    if not changed:
        return

    done = False
    for file in files:
        if done:
            break
        c = rf(file)
        if '¤' in c:
            ls = c.split('\n')
            for i, l in enumerate(ls):
                if '¤' in l and 'findproperty' in ls[i - 1]:
                    charvar = ls[i - 1].split('"')[3]
                    done = True
                    break

    done = False
    for file in files:
        if done:
            break
        c = rf(file)
        if charvar in c and '¤' not in c:
            ls = c.split('\n')
            for i, l in enumerate(ls):
                if charvar in l and '"split"' in ls[i + 1]:
                    del ls[i]
                    ls[i - 1] = '     pushstring          "\\n-\\n"'
                    done = True
                    sf(file, '\n'.join(ls))
                    break

fixLanguages()
