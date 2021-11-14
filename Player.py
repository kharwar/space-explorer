class Player:

    def __init__(self, name):
        self.name = name
        self.abilities = []

    def getName(self):
        return self.name

    def getAbilities(self):
        if len(self.abilities) == 0:
            print('You don\'t have any abilities yet.')
        else:
            print(self.abilities)

    def addAbility(self, ability):
        if ability in self.abilities:
            print('You already have this ability enabled')
        elif len(self.abilities) <= 3:
            print('You already have 3 abilities enabled. Please disable an ability!')
        else:
            self.abilities.append(ability)
            self.getAbilities()
