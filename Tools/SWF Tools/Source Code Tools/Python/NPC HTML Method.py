import glob
import json

def rf(f):
    with open(f, 'r', encoding = 'utf-8') as x:
        y = x.read()
    return y

def sf(f, c):
    _files[f] = c
    with _open(f, 'w') as x:
        x.write(c)

swfName = '158'
files = glob.glob(swfName + '-0/*.class.asasm')

def npchtml():
    for file in files:
        c = rf(file)
        if '31743' in c:
            p, si, ei, o = 0, 0, 0, 0
            ls = c.split('\n')
            cc = []
            for i, l in enumerate(ls):
                i -= o
                if si != 0 and ei != 0:
                    cc = ls[si:ei][:]
                    del ls[si:ei]
                    si, ei, o = 0, 0, o + (ei - si)
                if p == 0 and l == '      getlocal            9' and ls[i+2] == '      convert_i' and ls[i+3] == '      setlocal            14':
                    p += 1
                elif p == 1 and 'findpropstrict' in l:
                    si = i + 1
                    p += 1
                elif p >= 2 and p < 5 and 'add' in l:
                    if 'add' in l:
                        p += 1
                elif p == 5 and 'getlex' in l:
                    ls[i - 1] = '      pushstring          "undefined"'
                    ei = i - 1
                    p += 1
                elif p == 6 and '      setproperty         QName(PackageNamespace(""), "y")' in l and len(cc) > 0:
                    cc.insert(0, '      getlocal 16')
                    cc.extend([
                        '      add',
                        '      setproperty         QName(PackageNamespace(""), "htmlText")',
                        '',
                        '      getlocal 16',
                        '      pushstring "center"',
                        '      setproperty QName(PackageNamespace(""), "autoSize")',
                        ''
                    ])
                    ls = ls[:i+1] + cc + ls[i+1:]
                    sf(file, '\n'.join(ls))
                    break
            break
    print('[#] NPC HTML method added.\n')