import glob, os
path = "./158-0/{0}.class.asasm"
files = []
for asasm in glob.glob(path.format("*")):
    files += [asasm]

def readFile(file, isClass = False):
    file = file.replace("\\x", "%")
    if isClass:file = path.format(file)
    r = open(file, "r+")
    text = r.read()
    r.close()
    return text

def writeFile(file, content, isClass = False):
    file = file.replace("\\x", "%")
    if isClass:file = path.format(file)
    w = open(file, "w+")
    w.write(str(content))
    w.close()

def getLargFile():
    maxSize = 0
    fileMax = None
    for file in files:
        fileSize = os.path.getsize(file)
        if fileSize > maxSize:
            maxSize = fileSize
            fileMax = file

    return fileMax

def getConnClass():
    f = getLargFile()
    lines = readFile(f).split('\n')
    x = 0
    while x < len(lines):
        if "pushstring" in lines[x]:
            if "pushfalse" in lines[x + 1]:
                return lines[x-1].split('"')[-2]
        x += 1

    return ""

def main():
    ports = []
    print("-Replace ports:")
    print("Digite 'end' para terminar a edição")
    while True:
        p = input("port nº {0}:".format(len(ports)+1))
        try:
            p = int(p)
            ports.append(p)
        except:
            p = p.lower()
            if p == 'end':
                if len(ports) < 2:
                    print("ports need min 2 value")
                    continue
                break
            print("enter integer port only!")
    
    connClass = getConnClass()
    lines = readFile(connClass, True).split('\n')
    index = 0
    endindex = 0
    while not 'coerce              QName(PackageNamespace(""), "Array")' in lines[index]:
        index += 1

    endindex = index
    while not 'findpropstrict' in lines[index]:
        index -= 1

    startSpace = " "*6
    portlines = ['{0}pushint{1}{2}'.format(startSpace, " "*13, port) for port in ports]
    portlines.append('{0}constructprop       QName(PackageNamespace(""), "Array"), {1}'.format(startSpace, len(portlines)))
    lines[index+1:endindex] = portlines
    writeFile(connClass, "\n".join(lines), True)
    print("Finish")

main()
input("Pressione enter para continuar.")
