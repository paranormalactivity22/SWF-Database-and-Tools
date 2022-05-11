import os
import pip
import zlib

langues = {"EN":0, "FR":1, "FR":2, "BR":3, "ES":4, "CN":5, "TR":6, "VK":7, "PL":8, "HU":9, "NL":10, "RO":11, "ID":12, "DE":13, "E2":14, "AR":15, "PH":16, "LT":17, "JP":18, "CH":19, "FI":20, "CZ":21, "SK":22, "HR":23, "BU":24, "LV":25, "HE":26, "IT":27, "ET":29, "AZ":30, "PT":31}

print("TFM Language Editor by Hadaward")
print("Choose one of the options below")
print("1. Download new languages")
print("2. Uncompress downloaded languages")
print("3. Uncompress languages from another folder")
print("4. Compress languages\n")

while True:
    option = input("Option: ")
    
    if (option == "1"):
        if (not "requests" in globals()):
            try:
                globals()['requests'] = __import__("requests")
            except ImportError:
                print("For the download to be carried out it's necessary to have installed the requests module. TFMLE provides an automatic installer, do you want to continue and install requests?")
                option = input("Proceed (y/n)? ").lower()
                
                if (option == "y"):
                    if hasattr(pip, "main"):
                        pip.main(["install", "requests"])
                    else:
                        pip._internal.main(["install", "requests"])
                    globals()['requests'] = __import__("requests")    
                    
        if ("requests" in globals()):
            print("Downloading %s languages..."%(len(langues)))
            for id in langues:
                print("Downloading tfm-%s.gz"%(id.lower()))
                request = requests.get("https://www.transformice.com/langues/tfm-%s.gz"%(id.lower()))
                
                if ("content-length" in request.headers and int(request.headers["content-length"]) > 400):
                    open("cache/downloads/tfm-%s.gz"%(id.lower()), 'wb').write(request.content)
            print()
        else:
            print("Sorry, the download could not be made due to the lack of a dependency.")
            
    elif (option == "2"):
        for filename in os.listdir("cache/downloads/"):
            print("Uncompressing %s to 'src' folder"%(filename))
            file = open(os.path.join("cache/downloads", filename), 'rb')
            data = zlib.decompress(file.read())
            file.close()
            
            file = open(os.path.join("src", filename.replace(".gz", ".txt")), "wb")
            file.write(data)
            file.close()
            
    elif (option == "3"):
        isdir = False
        while not isdir:
            path = input("Enter the full path to the folder: ")
            isdir = os.path.isdir(path)
            
            if (not isdir):
                print("Enter a valid path")

        for filename in os.listdir(path):
            print("Uncompressing %s from %s to 'src' folder"%(filename, path))
            file = open(os.path.join("cache/downloads", filename), 'rb')
            data = zlib.decompress(file.read())
            file.close()
            
            file = open(os.path.join("src", filename.replace(".gz", ".txt")), "wb")
            file.write(data)
            file.close()
            
    elif (option == "4"):
        for filename in os.listdir("src"):
            print("Compressing %s from 'src' to 'build' folder"%(filename))
            file = open(os.path.join("src", filename), 'rb')
            data = zlib.compress(file.read())
            file.close()
            
            file = open(os.path.join("build", filename.replace(".txt", ".gz")), "wb")
            file.write(data)
            file.close()