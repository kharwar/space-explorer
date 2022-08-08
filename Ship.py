class Ship:

    def __init__(self, name):
        try:
            self.name = name
            self.inventory = []
            self.hops = 6
        except:
            print('Unknown error')

    def getName(self):
        try:
            return self.name
        except:
            print('Unknown error')

    def getItems(self):
        try:
            if len(self.inventory) == 0:
                return f'You don\'t have any items in your inventory.'
            else:
                return f'Your inventory now includes {self.inventory}'
        except:
            print('Unknown error')

    def addHops(self, hops):
        self.hops = self.hops + hops

    def subHops(self):
        self.hops = self.hops - 1

    def addItem(self, item):
        try:
            if item in self.inventory:
                return f'You already have this item in your inventory'
            else:
                self.inventory.append(item)
                get = self.getItems()
                return f'{item} added to the inventory.\n {get}'
        except:
            print('Unknown error')
