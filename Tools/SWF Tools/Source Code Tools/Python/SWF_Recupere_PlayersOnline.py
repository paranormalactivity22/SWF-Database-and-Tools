# -*- coding: utf-8 -*-
import os, glob
os.system("title SWF Recupere PlayersOnline")

def GetAllAsasm():
    files = []
    for asasm in glob.glob(GetPathByName("*")):
        files += [asasm]
    return files

def GetClassNameByFile(file):
    return file.replace("\\", "/").split("/")[-1].split('.')[0].replace("%", "\\x")

def ReadAllLines(path):
    return ReadAllText(path).split('\n')

def ReadAllText(path):
    r = open(path.replace("\\x", "%"), "r+")
    text = r.read()
    r.close()
    return text

def WriteAllLines(path, text):
    WriteAllText(path, "\n".join(map(str, text)))
    
def WriteAllText(path, text):
    w = open(path.replace("\\x", "%"), "w+")
    w.write(text)
    w.close()

def GetPathByName(name):
    return "./158-0/{0}.class.asasm".format(name.replace("\\x", "%"))

def FindEnligne():
    x_enligneProp = 'getproperty         Multiname("x_enligne", [PrivateNamespace('
    for file in files:
        lines = ReadAllLines(file)
        x = 0
        while x < len(lines):
            if x_enligneProp in lines[x]:
                return [GetClassNameByFile(file), lines[x+1].split('"')[-2]]
            x+=1
    return []

def FindPseudo():
    for file in files:
        lines = ReadAllLines(file)
        x = 0
        while x < len(lines):
            if '"$Pseudo"' in lines[x] and "pushstring" in lines[x]:
                return [GetClassNameByFile(file), lines[x+1].split('"')[-2]]
            x+=1

    return []

def GetRecupereTextFunction(x_enligne, Pseudo):
    lines = ReadAllLines(GetPathByName(x_enligne[0]))
    x = 0
    getproperty = 'getproperty         QName(PackageNamespace(""), "{0}")'.format(Pseudo[1])
    getlex = 'getlex              QName(PackageNamespace(""), "{0}")'.format(Pseudo[0])
    htmlText = 'setproperty         QName(PackageNamespace(""), "htmlText")'
    while x < len(lines):
        if getlex in lines[x]:
            if getproperty in lines[x+1]:
                maxJump = 7
                jump = 0
                found = False
                while jump < maxJump:
                    if htmlText in lines[x+jump]:
                        found = True
                        break
                    
                    jump += 1

                if found:
                    x += jump
                    while not 'callproperty' in lines[x]:
                        x -= 1

                    varmethod = lines[x].split('"')[-2]

                    while not 'getlocal1' in lines[x]:
                        x -= 1

                    varclass = lines[x+1].split('"')[-2]

                    while not 'setlocal1' in lines[x]:
                        x -= 1

                    return [varclass, varmethod, x]
        x+=1

    return []

def FindLogoTransformice():
    for file in files:
        lines = ReadAllLines(file)
        x = 0
        while x < len(lines):
            if '"$LogoTransformice"' in lines[x] and "pushstring" in lines[x]:
                return [GetClassNameByFile(file), lines[x+1].split('"')[-2]]
            x+=1

    return []

def FindNombre_Joueur():
    for file in files:
        lines = ReadAllLines(file)
        x = 0
        while x < len(lines):
            if '"$Nombre_Joueur"' in lines[x] and "pushstring" in lines[x]:
                return [GetClassNameByFile(file), lines[x+1].split('"')[-2]]
            x+=1

    return []

def GetPlayersOnlineVar():
    checkLines = ['getlex              QName(PackageNamespace("flash.system"), "Capabilities")',
                  'getproperty         QName(PackageNamespace(""), "language")',
                  'getlex              QName(PackageNamespace("flash.system"), "Capabilities")',
                  'getproperty         QName(PackageNamespace(""), "os")',
                  'getlex              QName(PackageNamespace("flash.system"), "Capabilities")',
                  'getproperty         QName(PackageNamespace(""), "version")']

    for file in files:
        lines = ReadAllLines(file)
        x = 0
        while x < len(lines):
            i = 0
            while i < len(checkLines):
                if checkLines[i] in lines[x+i]:
                    i+=1
                else:
                    break

            if i == len(checkLines):
                while x > 0:
                    if 'getlocal' in lines[x]:
                        if 'setproperty' in lines[x + 2]:
                            mainClass = lines[x-2].split('"')[-2]
                            mainInstance = lines[x-1].split('"')[-2]
                            mainVar = lines[x+2].split('"')[-2]
                            return [mainClass, mainInstance, mainVar]
                    x -= 1
            x += 1

    return []
    

def SaveFile(x_enligne, RTFunc, poVar):
    x_enligneClss = x_enligne[0]
    indextoAddLine = RTFunc[2]
    

    path = GetPathByName(x_enligneClss)
    lines = ReadAllLines(path)
    if 'iffalse' in lines[indextoAddLine+4]:
        print("Changing file...")

        Nombre_Joueur = FindNombre_Joueur()
        Log("Nombre_Joueur:",Nombre_Joueur)
        Nombre_JoueurLines = '{startSpace}pushstring          "$Nombre_Joueur"' 
        if Nombre_Joueur:
            Nombre_JoueurLines = '{startSpace}getlex              QName(PackageNamespace(""), "'+Nombre_Joueur[0]+'")\n'+\
                                 '{startSpace}getproperty         QName(PackageNamespace(""), "'+Nombre_Joueur[1]+'")'
                            
                            
        playersOnlineLine = '{startSpace}setlocal1\n\n'+\
                            '{startSpace}getlocal0\n'+\
                            '{startSpace}getproperty         QName(PackageNamespace(""), "{x_enligneVar}")\n'+\
                            '{startSpace}getlocal1\n'+\
                            '{startSpace}getlex              QName(PackageNamespace(""), "{RTClass}")\n'+\
                            Nombre_JoueurLines+'\n'+\
                            '{startSpace}getlex              QName(PackageNamespace(""), "{MainClass}")\n'+\
                            '{startSpace}getproperty         QName(PackageNamespace(""), "{MainInstance}")\n'+\
                            '{startSpace}getproperty         QName(PackageNamespace(""), "{OnlinesVar}")\n'+\
                            '{startSpace}callproperty        QName(PackageNamespace(""), "{RTMethod}"), 2\n'+\
                            '{startSpace}add\n'+\
                            '{startSpace}setproperty         QName(PackageNamespace(""), "htmlText")'
        
        
        playersOnlineLine = playersOnlineLine.format(startSpace = " "*len(lines[indextoAddLine].split(" ")[:-1]),
                                                     x_enligneVar = x_enligne[1],
                                                     RTClass = RTFunc[0],
                                                     RTMethod = RTFunc[1],
                                                     MainClass = poVar[0],
                                                     MainInstance = poVar[1],
                                                     OnlinesVar = poVar[2])

        lines[indextoAddLine] = playersOnlineLine
        
        logoTransformice = FindLogoTransformice()
        Log("logoTransformice:",logoTransformice)
        if logoTransformice:
            x = 0
            logolex = 'getlex              QName(PackageNamespace(""), "{0}")'.format(logoTransformice[0])
            logoprop = 'getproperty         QName(PackageNamespace(""), "{0}")'.format(logoTransformice[1])
            while x < len(lines):
                if logoprop in lines[x]:
                    if logolex in lines[x-1]:
                        yprop = 'setproperty         QName(PackageNamespace(""), "y")'
                        while not yprop in lines[x]:
                            x += 1

                        x-=1
                        lines[x] = '{0}pushbyte{1}{2}'.format(" "*5, " "*12, 50)
                        
                        while not 'getlocal0' in lines[x-2]:
                            del lines[x-1]
                            x-=1

                x += 1
            
        WriteAllLines(path, lines)
        print("end!")

    else:
        print("\nthis swf already has Online Players Text!")
        
DEBUG = False
def Log(*args):
    if DEBUG:
        print(" ".join(map(str, args)))

if __name__ == "__main__":
    print("Started")
    files = GetAllAsasm()
    x_enligne = FindEnligne()
    Log("loaded",len(files),"asasm")
    if x_enligne:
        Pseudo = FindPseudo()
        Log("$Pseudo:",Pseudo)
        if Pseudo:
            RTFunc = GetRecupereTextFunction(x_enligne, Pseudo)
            Log("RTFunc:",RTFunc)
            if RTFunc:
                playersOnlineVar = GetPlayersOnlineVar()
                Log("playersOnlineVar: ",playersOnlineVar)
                if playersOnlineVar:
                    SaveFile(x_enligne, RTFunc, playersOnlineVar)
        
    os.system("pause.")
