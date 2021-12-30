from TextUI import TextUI


class Ship:

    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.hops = 3
        self.textUI = TextUI()

    def getName(self):
        return self.name

    def getItems(self):
        if len(self.inventory) == 0:
            self.textUI.printtoTextUI(
                'You don\'t have any items in your inventory.')
            return f'You don\'t have any items in your inventory.'
        else:
            self.textUI.printtoTextUI(
                f"Your inventory now includes {self.inventory}")
            return f'Your inventory now includes {self.inventory}'

    def addHops(self, hops):
        self.hops = self.hops + hops

    def subHops(self):
        self.hops = self.hops - 1

    def addItem(self, item):

        if item in self.inventory:
            self.textUI.printtoTextUI(
                'You already have this item in your inventory')
            return f'You already have this item in your inventory'
        # elif len(self.abilities) <= 3:
        #     print('You already have 3 abilities enabled. Please disable an ability!')
        else:
            self.inventory.append(item)
            self.textUI.printtoTextUI(f'{item} added to the inventory.')
            self.getItems()
            return f'{item} added to the inventory.'
