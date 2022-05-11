# -*- coding: utf-8 -*-


import os, glob
def GetAllAsasm():
    files = []
    for asasm in glob.glob(GetPathByName("*")):
        files += [asasm]
    return files

def GetClassNameByFile(file):
    return file.replace("\\", "/").split("/")[-1].split('.')[0].replace("%", "\\x")
    
def GetPathByName(name):
    return "./158-0/{0}.class.asasm".format(name.replace("\\x", "%"))

    
def ReadAllLines(path):
    return ReadAllText(path).split('\n')
    
def ReadAllText(path):
    r = open(path.replace("\\x", "%"), encoding='utf-8')
    text = r.read()
    r.close()
    return text
    
def WriteAllLines(path, text):
    WriteAllText(path, "\n".join(map(str, text)))
    
def WriteAllText(path, text):
    w = open(path.replace("\\x", "%"), "w+")
    w.write(text)
    w.close()
    
def FindImgLogoNoise():
    find = 'pushstring          "divers/twitch-noisette.png"'
    for file in files:
        lines = ReadAllLines(file)
        x = 0
        while x < len(lines):
            if find in lines[x]:
                return [lines[x-1].split('"')[3]]
            x+=1
    return []

    
def FindFile(a):
    find = 'getproperty         QName(PackageNamespace(""), "{0}")'.format(a[0])
    for file in files:
        lines = ReadAllLines(file)
        x = 0
        while x < len(lines):
            if find in lines[x]:
                P22 = True
                return [GetClassNameByFile(file), lines[x]]
            x+=1
    return []


def RemoveImgLogo(a):
    path = GetPathByName(a[0])
    lines = ReadAllLines(GetPathByName(a[0]))
    x = 0
    find = a[1]
    while x < len(lines):
        if find in lines[x]:
            lines[x] = ""   
            WriteAllLines(path, lines)
            return            
        x+=1

if __name__ == "__main__":
    print("Started")
    P11 = False
    P22 = False
    files = GetAllAsasm()
    P1 = FindImgLogoNoise()
    if P1:
        P2 = FindFile(P1)
        if P2:
            RemoveImgLogo(P2)
            print("Finished")
    os.system("pause")