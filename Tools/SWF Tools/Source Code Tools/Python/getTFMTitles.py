import requests, json, os
from bs4 import BeautifulSoup

def types(type, hp="html.parser"):
    req, bfs, headers = None, None, {}
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    if (type == "First"):
        req = requests.get("https://transformice.fandom.com/wiki/Title/Firsts", headers=headers)
        bfs = BeautifulSoup(req.content, hp)
    elif (type == "Cheese"):
        req = requests.get("https://transformice.fandom.com/wiki/Title/Cheese", headers=headers)
        bfs = BeautifulSoup(req.content, hp)
    elif (type == "Bootcamp"):
        req = requests.get("https://transformice.fandom.com/wiki/Title/Bootcamp", headers=headers)
        bfs = BeautifulSoup(req.content, hp)
    elif (type == "Shop"):
        req = requests.get("https://transformice.fandom.com/wiki/Title/Shop", headers=headers)
        bfs = BeautifulSoup(req.content, hp)
    elif (type == "Admin"):
        req = requests.get("https://transformice.fandom.com/wiki/Title/Admin", headers=headers)
        bfs = BeautifulSoup(req.content, hp)
    elif (type == "Divine Mode"):
        req = requests.get("https://transformice.fandom.com/wiki/Title/Divine_Mode", headers=headers)
        bfs = BeautifulSoup(req.content, hp)
    elif (type == "Hard Mode"):
        req = requests.get("https://transformice.fandom.com/wiki/Title/Hard_Mode", headers=headers)
        bfs = BeautifulSoup(req.content, hp)
    elif (type == "Normal Mode"):
        req = requests.get("https://transformice.fandom.com/wiki/Title/Normal_Mode", headers=headers)
        bfs = BeautifulSoup(req.content, hp)
    return [req, bfs]

def sendMessage(items, type, send=True):
    id = (items.find("td").text.replace("\n", ""))
    name = (items.find("td", attrs={"colspan":2}).text.replace("\n", ""))
    gather = (items.find("td", attrs={"style":"text-align: right; width: 7.5%;"}).text.replace("\n", "").replace(" ", ".") if not type == "admin" else items.find("td", attrs={"colspan":3}).text.replace("\n", ""))
    shamanId = (items.find("td", attrs={"style":"text-align: left;"}).text.replace("\n", ""))
    
    if send:
        msg = (f"{type.capitalize()} [Title ID: {id}] - [Title Name: {name}] - [Title Gather: {gather if not type == 'Divine Mode' and not type == 'Hard Mode' and not type == 'Normal Mode' else gather + ' ' + shamanId}]")
    else:
        msg = ""
    
    return msg

def setJson(items, type, get=True):    
    id = (items.find("td").text.replace("\n", ""))
    name = (items.find("td", attrs={"colspan":2}).text.replace("\n", ""))
    
    titles = {}
    titles[id] = name
    if not "titles.json" in os.listdir():
        with open("titles.json", "w") as c:
            json.dump(titles, c)
    else:
        if get:
            with open("titles.json", "r+") as file:
                data = json.load(file)
                data.update(titles)
                file.seek(0)
                json.dump(data, file)
            
def getMessage(finds, type, get=True):
    for items in finds:
        try:
            if get:
                print(sendMessage(items, type))
                setJson(items, type)
        except:
            pass 
      
def getAll(source, type, perm=True):
    find_table = source.find("table", attrs={"class":"wikitable oddrow sortable centertext"})
    finds = find_table.findAll("tr")
    if perm:
        getMessage(finds, type)

def getTitles(type):
    source = None
    if (type == "First"):
        source = types("First")[1]
    elif (type == "Cheese"):
        source = types("Cheese")[1]
    elif (type == "Bootcamp"):
        source = types("Bootcamp")[1]
    elif (type == "Shop"):
        source = types("Shop")[1]
    elif (type == "Admin"):
        source = types("Admin")[1]
    elif (type == "Divine Mode"):
        source = types("Divine Mode")[1]
    elif (type == "Hard Mode"):
        source = types("Hard Mode")[1]
    elif (type == "Normal Mode"):
        source = types("Normal Mode")[1]
    getAll(source, type)

    return type
    
if __name__ == "__main__":
    categories = ["cheese", "first", "bootcamp", "admin", "hard mode", "divine mode", "normal mode", "shop"]
    m = ", ".join(categories)
    print(f"Categories: [{m.title()}]")
    while True:
        choose = input("Select Category: ")
        try:
            if choose in categories:
                getTitles(choose.title())
                break
        except AttributeError:
            print("Enter the correct value.")

