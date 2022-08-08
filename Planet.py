class Planet:

    def __init__(self, description, name, items, hops):
        """
            Constructor method
        :param description: text description for this room
        """
        try:
            self.description = description
            self.name = name
            self.exits = {}
            self.items = items
            self.hops = hops
        except:
            print('Unknown Error')

    def setExit(self, planetName, neighbour):
        self.exits[planetName] = neighbour

    def getItems(self):
        return self.items

    def getShortDescription(self):
        return self.description

    def getName(self):
        return self.name

    def getLongDescription(self):
        return f'\nLocation: {self.description}\nYour exits: {self.getExits()} '

    def getExits(self):
        try:
            allExits = self.exits.keys()
            return list(allExits)
        except:
            print('Unknown Error')

    def getExit(self, planetName):
        try:
            if planetName in self.exits:
                return self.exits[planetName]
            else:
                return None
        except:
            print('Unknown Error')
