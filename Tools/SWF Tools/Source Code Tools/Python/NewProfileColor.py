#coding: utf-8
import os, glob, re, random
mainFileName = '158'
mainSWF = "%s.swf" % mainFileName
mainDirectory = "./%s-0/" % mainFileName
mainABCFile = "%s-0.abc" % mainFileName
mainPath =  "%s*.class.asasm" % (mainDirectory)

    
def GetClassNameByFile(file):
    return file.replace("\\", "/").split("/")[-1].split('.')[0].replace("%", "\\x")
    
def GetPathByName(name):
    return "./158-0/{0}.class.asasm".format(name.replace("\\x", "%"))
    
files = []
for asasm in glob.glob(GetPathByName("*")):
	files += [asasm]
    
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
    w = open(path.replace("\\x", "%"), "w+", encoding='utf-8')
    w.write(text)
    w.close()
	
files = []
for asasm in glob.glob(GetPathByName("*")):
	files += [asasm]


def GenerateSecretString():
	v = []
	e = random.randint(8,16)
	s = ""
	for x in range(0,e):
		s += chr(random.randint(1,8))
	return str(repr(s))

NewColorSecrStr = GenerateSecretString().replace("'", "")
NewIDSecrStr = GenerateSecretString().replace("'", "")

def GetStringBetwean2Chars(srt, s, e):
	return srt[srt.find(s)+len(s):srt.rfind(e)]

def GetMainColorToSearch():
	findString = 'pushint             12238127'
	r = 0
	for file in files:
		lines = ReadAllLines(file)
		num = 0
		while num < len(lines):
			if ( findString in lines[num] and ('findproperty' in lines[num-1] and 'initproperty' in lines[num+1]) ):
				if ( r == 0 ):
					return [GetStringBetwean2Chars(lines[num+1], 'QName(PackageNamespace(""), "', '")'), GetClassNameByFile(file)]
			num += 1
	return []

def GetLastSlotid(search):
	path = GetPathByName(search[1])
	lines = ReadAllLines(path)
	gaha = []
	for x in range(0, len(lines)):
		if ( "slotid" in lines[x] ):
			i = lines[x].find("slotid ")
			r = lines[x][i:][:len("slotid ")+2].replace(' ', '').replace('slotid', '')
			gaha.append(r)
	if ( len(gaha) == 0 ):
		return ""
	return int(gaha[-1])

def ExistLFunction(search, L):
	lines = ReadAllLines(GetPathByName(search))
	serch = "L%s:" % ( L )
	for x in range(0, len(lines)):
		if ( serch in lines[x] ):
			return True
	return False

def GetMainIDToSearch():
	findLines = ["pushint             7108544"]
	res = ""
	for file in files:
		lines = ReadAllLines(file)
		num = 0
		while num < len(lines):
			if ( findLines[0] in lines[num] ):
				res = lines[num-1]
				res = [GetStringBetwean2Chars(res, 'QName(PackageNamespace(""), "', '")'), GetClassNameByFile(file)]
			num += 1
	return res

def GetProfileNameColorsFunction(search):
	findLines = ['getproperty         QName(PackageNamespace(""), "%s")' % search[0], 'convert_i']
	res = ''
	for file in files:
		lines = ReadAllLines(file)
		num = 0
		while num < len(lines):
			if ( findLines[0] in lines[num] and findLines[1] in lines[num+1] ):
				res = lines[num-7]
				res = [res, GetClassNameByFile(file)]
			num += 1
	return res


NewIfElse = random.randint(120,200)

def GetJumpFunc(search):
	path = GetPathByName(search[1])
	lines = ReadAllLines(path)
	for x in range(0, len(lines)):
		if ( search[0] in lines[x] and lines[x+3].find("jump") != -1):
			return GetStringBetwean2Chars(lines[x+4], "L", "")
	return ''

def GetLastIfElse(search):
	path = GetPathByName(search[1])
	lines = ReadAllLines(path)
	for x in range(0, len(lines)):
		if ( search[0] in lines[x] and lines[x+3].find("getlocal2") != -1):
			return GetStringBetwean2Chars(lines[x+4], "L", "")
	return ''

def GetColorAndIDClasses(search):
	path = GetPathByName(search[1])
	lines = ReadAllLines(path)
	for x in range(0, len(lines)):
		if ( search[0] in lines[x] and lines[x+3].find("getlocal2") != -1):
			return [GetStringBetwean2Chars(lines[x+1], 'QName(PackageNamespace(""), "', '")'), GetStringBetwean2Chars(lines[x+6], 'QName(PackageNamespace(""), "', '")')]
	return ''

def SetLastIfElse(search):
	global NewIfElse
	path = GetPathByName(search[1])
	lines = ReadAllLines(path)
	if ( ExistLFunction(search[1], NewIfElse) ):
		NewIfElse = random.randint(150, 250)
	for x in range(0, len(lines)):
		if ( search[0] in lines[x] and lines[x+3].find("getlocal2") != -1):
			lines[x+4] = "ifne                L%s" % NewIfElse
			WriteAllLines(path, lines)

def UpdateProfileNameColorsFunction(search):
	global NewIfElse
	path = GetPathByName(search[3][1])
	lines = ReadAllLines(path)
	finds = "jump                L%s" % search[0]
	exist = False
	v=0
	if ( ExistLFunction(search[3][1], NewIfElse) ):
		NewIfElse = random.randint(150, 250)
	for x in range(0,len(lines)):
		if ( finds in lines[x] and search[3][0] in lines[x-11] ):
			if ( v == 0 ): 
				v = x 
				exist = True
				lines.insert(x+1, "")
				lines.insert(x+2, 'L%s:' % NewIfElse)
				lines.insert(x+3, '      getlex              QName(PackageNamespace(""), "%s")' % search[1][0])
				lines.insert(x+4, '      getproperty         QName(PackageNamespace(""), "%s")' % NewIDSecrStr)
				lines.insert(x+5, '      getlocal2')
				lines.insert(x+6, '      ifne                L%s' % search[2])
				lines.insert(x+7, '')
				lines.insert(x+8, '      getlex              QName(PackageNamespace(""), "%s")' % search[1][1])
				lines.insert(x+9, '      getproperty         QName(PackageNamespace(""), "%s")' % NewColorSecrStr)
				lines.insert(x+10, '      convert_i')
				lines.insert(x+11, '      setlocal3')
				lines.insert(x+12, '')
				lines.insert(x+13, '      jump                L%s' % search[0])
	if ( exist ):
		WriteAllLines(path, lines)
		SetLastIfElse(search[3])
		print("[•] Profile name colors function has been updated.\n[•] You can now use name profile color as %s color with id %s" % (search[4], search[5]))

def SetNewColor(hex, search):
	path = GetPathByName(search[1])
	lines = ReadAllLines(path)
	finds = ['    initproperty        QName(PackageNamespace(""), "%s")' % search[0], ' trait const QName(PackageNamespace(""), "%s") slotid ' % search[0]]
	both = [False, False]
	for x in range(0,len(lines)):
		if ( finds[0] in lines[x] ):
			both[0] = True
			lines.insert(x+1, "")
			lines.insert(x+2, '    findproperty        QName(PackageNamespace(""), "%s")' % NewColorSecrStr)
			lines.insert(x+3, '    pushint             %d' % int("0x"+hex[1:], 16))
			lines.insert(x+4, '    initproperty        QName(PackageNamespace(""), "%s")' % NewColorSecrStr)
		if ( finds[1] in lines[x] ):
			both[1] = True
			lines.insert(x+1, ' trait const QName(PackageNamespace(""), "%s") slotid %s type QName(PackageNamespace(""), "int") value Integer(%d) end' % (NewColorSecrStr, GetLastSlotid(search) + 1, int("0x"+hex[1:], 16)))
	if ( both[0] and both[1] ):
		WriteAllLines(path, lines)
		print("[•] Color %s has been added successfuly!" % hex)

def GetIDsNumsClass(search):
	path = GetPathByName(search[1])
	lines = ReadAllLines(path)
	finds = [
		'getproperty         QName(PackageNamespace(""), "%s")' % search[0]
	]
	classes = []
	for x in range(0,len(lines)):
		if ( finds[0] in lines[x] ):
			classes.append(GetStringBetwean2Chars(lines[x-2], 'QName(PackageNamespace(""), "', '")'))
			classes.append(GetStringBetwean2Chars(lines[x+1], 'QName(PackageNamespace(""), "', '")'))
			classes.append(GetStringBetwean2Chars(lines[x+4], 'StaticProtectedNs("', '")])'))
	return classes

def SetNewID(id, search):
	path = GetPathByName(search[1])
	lines = ReadAllLines(path)
	find = [
		'    findproperty        QName(PackageNamespace(""), "%s")' % search[0], 
		'    initproperty        QName(PackageNamespace(""), "%s")' % search[0], 
		'trait const QName(PackageNamespace(""), "%s") slotid' % search[0]
	]
	findSecondary = 'PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"),'
	exist = [True, True, True]
	
	for x in range(0,len(lines)):
		if ( find[1] in lines[x] ):
			exist[0] = True
			lines.insert(x+1, "")
			lines.insert(x+2, '    findproperty        QName(PackageNamespace(""), "%s")' % NewIDSecrStr)
			lines.insert(x+3, '    getlocal0')
			lines.insert(x+4, '    pushshort           %s' % id)
			lines.insert(x+5, '    pushshort           0')
			lines.insert(x+6, '    add')
			lines.insert(x+7, '    construct           1')
			lines.insert(x+8, '    initproperty        QName(PackageNamespace(""), "%s")' % NewIDSecrStr)
		if ( find[1] in lines[x]):
			exist[1] = True
			lines.insert(x+9, "")
			lines.insert(x+10, '    getlocal0')
			lines.insert(x+11, '    getproperty         QName(PackageNamespace(""), "%s")' % NewIDSecrStr)
			lines.insert(x+12, '    getproperty         QName(PackageNamespace(""), "%s")' % NewIDSecrStr)
			lines.insert(x+13, '    setproperty         MultinameL([PrivateNamespace(null, "{0}#0"), PackageNamespace(""), PrivateNamespace(null, "{0}#1"), PackageInternalNs(""), Namespace("http://adobe.com/AS3/2006/builtin"), ProtectedNamespace("{0}"), StaticProtectedNs("{0}")])'.format(NewIDSecrStr))
		if ( find[2] in lines[x] ):
			exist[2] = True
			lines.insert(x+1, ' trait const QName(PackageNamespace(""), "%s") slotid %s type QName(PackageNamespace(""), "%s") end' % (NewIDSecrStr, GetLastSlotid(search) + 1,"int"))
	if ( exist[0] and exist[1] and exist[2] ):
		WriteAllLines(path, lines)
		print("[•] ID %s has been added successfuly!" % id)

if __name__ == '__main__':
	NewColorProfileInfo = {"id":70, "hex":"#4caf50"}
	print("We creating new profile name color for you with, ID: %s, Color Hex Code: %s" % (NewColorProfileInfo["id"], NewColorProfileInfo["hex"]))
	print("Please wait it'll take a few minutes...")
	ColorVar = GetMainColorToSearch()
	IDVar = GetMainIDToSearch()
	ProfileFunc = GetProfileNameColorsFunction(ColorVar)
	JumpFunc = GetJumpFunc(ProfileFunc)
	ColorsAndIDsClasses = GetColorAndIDClasses(ProfileFunc)
	LastL = GetLastIfElse(ProfileFunc)
	Search = [JumpFunc, ColorsAndIDsClasses, LastL, ProfileFunc, NewColorProfileInfo["id"], NewColorProfileInfo["hex"]]
	SetNewColor(NewColorProfileInfo["hex"], ColorVar)
	SetNewID(NewColorProfileInfo["id"], IDVar)
	UpdateProfileNameColorsFunction(Search)
