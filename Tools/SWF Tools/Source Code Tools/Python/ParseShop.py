import requests, os, json
api_url = "https://cheese.formice.com/api/dressroom/mouse/"
api_url_2 = "https://cheese.formice.com/api/dressroom/shaman/"
__version__ = "0.2"
__author__ = "Lucas"

class Updater:
    def __init__(self):
        #mouse
        self.fur: int = 217
        self.head: int = 236
        self.eyes: int = 49
        self.ears: int = 84
        self.mouth: int = 80
        self.neck: int = 64
        self.hair: int = 104
        self.tail: int = 54
        self.contact: int = 67
        self.hands: int = 51
        #shaman
        self.box: int = 142
        self.ibox: int = 246
        self.gr: int = 340
        self.igr: int = 443
        self.ball: int = 636
        self.gred: int = 709
        self.nick: int = 1021
        self.ball2: int = 1735
        self.ballo: int = 2844
    def on(self, t="1;0",y=False):
        if y:
            return requests.get(f'{api_url_2}{t}').status_code == 200
        return requests.get(f'{api_url}{t}').status_code == 200
    
    def update(self):
        i = 0
        t = True
        while t:
            if i == 0:
                self.fur = self.updater('0',self.fur,';0')
            elif i == 1:
                self.head = self.updater('1;',self.head)
            elif i == 2:
                self.eyes = self.updater('1;0,',self.eyes)
            elif i == 3:
                self.ears = self.updater('1;0,0,',self.ears)
            elif i == 4:
                self.mouth = self.updater('1;0,0,0,',self.mouth)
            elif i == 5:
                self.neck = self.updater('1;0,0,0,0,',self.neck)
            elif i == 6:
                self.hair = self.updater('1;0,0,0,0,0,',self.hair)
            elif i == 7:
                self.tail = self.updater('1;0,0,0,0,0,0,',self.tail)
            elif i == 8:
                self.contact = self.updater('1;0,0,0,0,0,0,0,',self.contact)
            elif i == 9:
                self.hands = self.updater('1;0,0,0,0,0,0,0,0,',self.hands)
            elif i == 10:
                #shaman
                for d in ['box','ibox','gr','igr','ball','gred','nick','ball2','ballo']:
                    exec(f"self.{d} = self.updater('',self.{d})")
            else:
                t = False
            i+=1
        return self
    
    def updater(self, start='', _id=0, end=''):
        while True:
            if self.on(f'{start}{_id+1}{end}',start == ''):
                _id+=1
            else:
                return _id
                
class Saver:
    def __init__(self, shop):
        self.shop = shop
        d = {'shopItems':[],'shamanItems':[],'fullLooks':[]}
        i = 1
        while self.shop.head >= i:
            d['shopItems'].insert(0, {"category": 0, "id": i, "cheese": 950, "fraise": 100, "new": i == self.shop.head, "customs": 2, "collector": i == self.shop.head})
            i+=1
        i = 1
        while self.shop.eyes >= i:
            d['shopItems'].insert(0, {"category": 1, "id": i, "cheese": 200, "fraise": 30, "new": i == self.shop.eyes, "customs": 1, "collector": i == self.shop.eyes})
            i+=1
        i = 1
        while self.shop.ears >= i:
            d['shopItems'].insert(0, {"category": 2, "id": i, "cheese": 400, "fraise": 40, "new": i == self.shop.ears, "customs": 1, "collector": i == self.shop.ears})
            i+=1
        i = 1
        while self.shop.mouth >= i:
            d['shopItems'].insert(0, {"category": 3, "id": i, "cheese": 400, "fraise": 40, "new": i == self.shop.mouth, "customs": 1, "collector": i == self.shop.mouth})
            i+=1
        i = 1
        while self.shop.neck >= i:
            d['shopItems'].insert(0, {"category": 4, "id": i, "cheese": 300, "fraise": 40, "new": i == self.shop.neck, "customs": 3, "collector": i == self.shop.neck})
            i+=1
        i = 1
        while self.shop.hair >= i:
            d['shopItems'].insert(0, {"category": 5, "id": i, "cheese": 400, "fraise": 50, "new": i == self.shop.hair, "customs": 4, "collector": i == self.shop.hair})
            i+=1
        i = 1
        while self.shop.tail >= i:
            d['shopItems'].insert(0, {"category": 6, "id": i, "cheese": 1000, "fraise": 120, "new": i == self.shop.tail, "customs": 2, "collector": i == self.shop.tail})
            i+=1
        i = 1
        while self.shop.contact >= i:
            d['shopItems'].insert(0, {"category": 7, "id": i, "cheese": 400, "fraise": 80, "new": False, "customs": 0, "collector": False})
            i+=1
        i = 1
        while self.shop.hands >= i:
            d['shopItems'].insert(0, {"category": 8, "id": i, "cheese": 1100, "fraise": 180, "new": i == self.shop.hands, "customs": 2, "collector": i == self.shop.hands})
            i+=1
        i = 0
        while 7 > i:
            d['shopItems'].insert(0, {"category": 21, "id": i, "cheese": 3000, "fraise": 150, "new": False, "customs": 0, "collector": False})
            i+=1
        i = 2
        while self.shop.fur >= i:
            d['shopItems'].insert(0, {"category": 22, "id": i, "cheese": 6500, "fraise": 400, "new": i == self.shop.fur, "customs": 0, "collector": i == self.shop.fur})
            i+=1
        i = 101
        while self.shop.box >= i:
            d['shamanItems'].insert(0, {"id": i, "cheese": 1500, "fraise": 50, "customs": 5, "flag": 5, "new": i == self.shop.box})
            i+=1
        i = 201
        while self.shop.ibox >= i:
            d['shamanItems'].insert(0, {"id": i, "cheese": 3000, "fraise": 100, "customs": 5, "flag": 5, "new": i == self.shop.ibox})
            i+=1
        i = 301
        while self.shop.gr >= i:
            d['shamanItems'].insert(0, {"id": i, "cheese": 3000, "fraise": 100, "customs": 6, "flag": 6, "new": i == self.shop.gr})
            i+=1
        i = 401
        while self.shop.igr >= i:
            d['shamanItems'].insert(0, {"id": i, "cheese": 3000, "fraise": 100, "customs": 4, "flag": 4, "new": i == self.shop.igr})
            i+=1
        i = 601
        while self.shop.ball >= i:
            d['shamanItems'].insert(0, {"id": i, "cheese": 1500, "fraise": 50, "customs": 5, "flag": 5, "new": i == self.shop.ball})
            i+=1
        i = 701
        while self.shop.gred >= i:
            d['shamanItems'].insert(0, {"id": i, "cheese": 200, "fraise": 10, "customs": 4, "flag": 4, "new": i == self.shop.gred})
            i+=1
        i = 1002
        while self.shop.nick >= i:
            d['shamanItems'].insert(0, {"id": i, "cheese": 2000, "fraise": 10, "customs": 2, "flag": 2, "new": i == self.shop.nick})
            i+=1
        i = 1701
        while self.shop.ball2 >= i:
            d['shamanItems'].insert(0, {"id": i, "cheese": 3000, "fraise": 100, "customs": 2, "flag": 2, "new": i == self.shop.ball2})
            i+=1
        i = 2801
        while self.shop.ballo >= i:
            d['shamanItems'].insert(0, {"id": i, "cheese": 3000, "fraise": 100, "customs": 2, "flag": 2, "new": i == self.shop.ballo})
            i+=1
        open('shop.json', 'w').write(json.dumps(d))
        
if __name__ == '__main__':
    print("[+] Started")
    print("[+] Getting new shop, may take a while...")
    shop = Updater().update()
    print("[+] Saving all shop..")
    Saver(shop)
    print("[+] Done, Saved as shop.json")
    os.system("pause")