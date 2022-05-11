import glob
import json

def rf(f):
    with open(f, 'r', encoding = 'utf-8') as x:
        y = x.read()
    return y

version = 0
ckey = ''
getlex = []
getproperty = []
swfName = '158'
files = glob.glob(swfName + '-0/*.class.asasm')

for f in files:
    lines = rf(f).split('\n')
    for index, line in enumerate(lines):
        if 'SHA256_faux' in line:
            if 'getlex' in lines[index + 6]:
                x = index
                while not 'getlex              QName(PackageNamespace("flash.system"), "Capabilities")' in lines[x]:
                    if 'getlex' in lines[x]:
                        if 'getproperty' in lines[x+1] and not 'findpropstrict' in lines[x+2]:
                            getlex.append(swfName + '-0/' + lines[x].split('"')[-2].split('"')[0].replace("\\x", "%") + '.class.asasm')
                            getproperty.append(lines[x+1].split('"')[-2].split('"')[0])
                    x += 1

for prop in getproperty:
    for f in getlex:
        lines = rf(f).split('\n')
        for index, line in enumerate(lines):
            if prop in lines[index - 1]:
                if 'pushstring' in line:
                    ckey += line.split('"')[1].split('"')[0]
                    break

for f in files:
    lines = rf(f).split('\n')
    for index, line in enumerate(lines):
        if not 'end ; code' in lines[index - 3] and 'end ; body' in lines[index - 2]:
            if 'type QName(PackageNamespace(""), "int") value Double' in line:
                if 'type QName(PackageNamespace(""), "int") value Double' in lines[index + 1]:
                    v= int(line[-8:-5])
                    if v != 750:
                        version = v
                    break

print(version)
print(ckey)
input()