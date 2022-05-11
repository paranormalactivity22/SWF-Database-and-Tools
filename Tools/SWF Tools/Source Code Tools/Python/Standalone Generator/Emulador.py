import urllib2, os, tkMessageBox
from Tkinter import *

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


def make_entry(parent, caption, width = None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry


def enter(event):
    create()


def create():
	""" Collect 1's for every failure and quit program in case of failure_max failures """
	print (mice_name.get(), mice_swfL.get())
	mice=mice_name.get()
	url=mice_swfL.get()
	root.destroy()
	
	if (mice, url):
		
		window = Tk()
		window.wm_withdraw()
		window.geometry('1x1+' + str(window.winfo_screenwidth() / 2) + '+' + str(window.winfo_screenheight() / 2))
		tkMessageBox.showinfo(title='Standalone Generator', message='Baixando a swf do '+str(mice)+', aguarde.')
		tfmAIR=None
			
		try:
			pbFile = urllib2.urlopen(url)
			tfmAIR = pbFile.read()
			pbFile.close()
		except:
			tfmAIR=None
			
		if tfmAIR == None:
			tkMessageBox.showinfo(title='Standalone Generator', message='Falha no download, o link deve estar errado.')
			data = os.system("Emulador.py")
			
		if tfmAIR != None:
			tkMessageBox.showinfo(title='Standalone Generator', message='Download concluido.')
			application = '<?xml version="1.0" encoding="utf-8" standalone="no"?><application xmlns="http://ns.adobe.com/air/application/3.4"><id>'+str(mice)+'</id><filename>'+str(mice)+'</filename><name>Transformice</name><versionNumber>1.0.0</versionNumber><description>Fromage !</description><copyright>Copyright Atelier 801</copyright><initialWindow><content>TransformiceAIR.swf</content><title>'+str(mice)+'</title><autoOrients>false</autoOrients><fullScreen>false</fullScreen><visible>true</visible></initialWindow></application>'
			pbFile = open("./files/tfmstand.exe", "rb")
			appexe = pbFile.read()
			pbFile.close()
		
			pbFile = open("./files/signatures.xml", "rb")
			signatures = pbFile.read()
			pbFile.close()
		
			os.mkdir(mice)
			os.mkdir(mice+"/META-INF")
			os.mkdir(mice+"/META-INF/AIR")
			with open(str(mice)+"/"+str(mice)+".exe", "wb") as code:
				code.write(appexe)
			with open(mice+"/TransformiceAIR.swf", "wb") as code:
				code.write(tfmAIR)
			with open(mice+"/META-INF/signatures.xml", "wb") as code:
				code.write(signatures)
			with open(mice+"/META-INF/AIR/application.xml", "wb") as code:
				code.write(application)
			tkMessageBox.showinfo(title='Standalone Generator', message='A standalone do '+str(mice)+' foi criada com sucesso.')
	
	
root = tk.Tk()
root.geometry('300x160')
root.title('Criador de Standalone')
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
mice_name = make_entry(parent, 'Nome do Mice:', 16, show='')
mice_swfL = make_entry(parent, 'Link da swf:', 150, show='')
b = tk.Button(parent, borderwidth=4, text='Criar Standalone', width=20, pady=8, command=create)
b.pack(side=tk.BOTTOM)
mice_swfL.bind('<Return>', enter)
mice_name.focus_set()
parent.mainloop()