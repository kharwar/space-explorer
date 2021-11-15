class Ship:

    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.hops = 100000

    def getName(self):
        return self.name

    def getItems(self):
        if len(self.inventory) == 0:
            print('You don\'t have any items in your inventory.')
        else:
            print("Your inventory is",self.inventory)

    def addHops(self):
        self.hops = self.hops + 1
    
    def subHops(self):
        self.hops = self.hops - 1
        

    def addItem(self, item):
        
        if item in self.inventory:
            print('You already have this item in your inventory')
        # elif len(self.abilities) <= 3:
        #     print('You already have 3 abilities enabled. Please disable an ability!')
        else:
            self.inventory.append(item)
            self.getItems()
            
