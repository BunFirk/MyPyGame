
class Bag:
    def __init__(self):
        self.items = []
    
    def addItem(self, item):
        self.items.append(item)
        
    def removeItem(self, itemNum):
        if 0 <= itemNum < len(self.items): 
            self.items.pop(itemNum)
        else:
            print("error: item is not found")
    
    def checkBag(self):
        i = 0
        for item in self.items:
            i += 1
            print(f"{i}. " + item)

"""
myBag = Bag()
myBag.addItem("hello")
myBag.addItem("proroeoe")
myBag.removeItem(1)
myBag.checkBag()
"""