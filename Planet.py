"""
    Create a room described "description". Initially, it has
    no exits. 'description' is something like 'kitchen' or
    'an open court yard'
"""


class Planet:

    def __init__(self, description, name, items, hops):
        """
            Constructor method
        :param description: text description for this room
        """
        self.description = description
        self.name = name
        self.exits = {}
        self.items = items
        self.hops = hops

    def setExit(self, planetName, neighbour):
        self.exits[planetName] = neighbour

    def getItems(self):
        return self.items

    def getShortDescription(self):
        return self.description

    def getName(self):
        return self.name

    def getLongDescription(self):
        return f'Location: {self.description}, Exits: {self.getExits()} '

    def getExits(self):

        allExits = self.exits.keys()
        return list(allExits)

    def getExit(self, planetName):
        if planetName in self.exits:
            return self.exits[planetName]
        else:
            return None
