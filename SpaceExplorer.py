from Planet import Planet
from Ship import Ship
from TextUI import TextUI

"""
    This class is the main class of the "Space Explorer" application.
    'Space Explorer' is a very simple, text based adventure game.

    To play this game, create an instance of this class and call the "play"
    method.
"""


class Game:

    def __init__(self):
        """
        Initializes the game
        """
        self.createPlanets()
        shipName = input("Please enter the name of your ship: ")
        self.ship = Ship(shipName)
        self.currentPlanet = self.worlorm
        self.textUI = TextUI()

    def createPlanets(self):
        """
            Sets up all Planet
        :return: None
        """
        self.worlorm = Planet(
            "You are on the Worlorm Planet", "Worlorm", [], 0)
        self.cybertron = Planet(
            "These is a planet of Robots be Carefull and make friendship wisely", "Cybertron", [], 1)
        self.ego = Planet(
            "These is a planet of a living tribual its not the safe planet", "Ego", [], 0)
        self.krypton = Planet(
            "This planet is going to die soon", "Krypton", [], 1)
        self.solaris = Planet(
            "You have safely landed to Solaris", "Solaris", [], 1)
        self.titan = Planet(
            "This planet is where thanos lives", "Titan", ["starsaber"], 1)
        self.dagobah = Planet(
            "This planet is well known planet of star Wars", "Dagobah", [], -2)
        self.vormir = Planet(
            "This is the planet where you can get super powers", "Vormir", ["key"], 2)
        self.knowhere = Planet(
            "This is the home of the mining colony of Exitar.", "Knowhere", [], 0)
        self.earth = Planet(
            "This is the last planet where you can reach your destination", "Earth", [], 0)
        self.xander = Planet(
            "", "Xander", [], 0)
        self.asgard = Planet(
            "", "Asgard", [], 1)
        self.pluto = Planet(
            "", "Pluto", ["orbHolder"], 2
        )

        self.worlorm.setExit("cybertron", self.cybertron)
        self.worlorm.setExit("ego", self.ego)
        self.ego.setExit("worlorm", self.worlorm)
        self.ego.setExit("krypton", self.krypton)
        self.ego.setExit("titan", self.titan)
        self.cybertron.setExit("worlorm", self.worlorm)
        self.cybertron.setExit("krypton", self.krypton)
        self.cybertron.setExit("dagobah", self.dagobah)
        self.dagobah.setExit("cybertron", self.cybertron)
        self.dagobah.setExit("solaris", self.solaris)
        self.dagobah.setExit('asgard', self.asgard)
        self.titan.setExit("ego", self.ego)
        self.titan.setExit("vormir", self.vormir)
        self.krypton.setExit("cybertron", self.cybertron)
        self.krypton.setExit("solaris", self.solaris)
        self.krypton.setExit("vormir", self.vormir)
        self.krypton.setExit("ego", self.ego)
        self.solaris.setExit("dagobah", self.dagobah)
        self.solaris.setExit("krypton", self.krypton)
        self.solaris.setExit("knowhere", self.knowhere)
        self.solaris.setExit("xander", self.xander)
        self.vormir.setExit("krypton", self.krypton)
        self.vormir.setExit("titan", self.titan)
        self.vormir.setExit("knowhere", self.knowhere)
        self.knowhere.setExit("solaris", self.solaris)
        self.knowhere.setExit("vormir", self.vormir)
        self.knowhere.setExit("earth", self.earth)
        self.asgard.setExit("dagobah", self.dagobah)
        self.asgard.setExit("xander", self.xander)
        self.asgard.setExit("pluto", self.pluto)
        self.pluto.setExit("asgard", self.asgard)
        self.xander.setExit("solaris", self.solaris)
        self.xander.setExit("asgard", self.asgard)
        self.xander.setExit("earth", self.earth)
        self.earth.setExit("knowhere", self.knowhere)
        self.earth.setExit("xander", self.xander)

    def canEnter(self, planetKey, items):
        if self.currentPlanet.getExit(planetKey):
            for item in items:
                if item not in self.ship.inventory:
                    return False
        return True

    def play(self):
        """
            The main play loop
        :return: None
        """
        self.doPrintHelp()
        finished = False
        while (finished == False):
            command = self.textUI.getCommand()      # Returns a 2-tuple
            finished = self.processCommand(command)

        print("Thank you for playing!")

    def doPrintHelp(self):
        """
            Displays a welcome message
        :return:
        """
        self.textUI.printtoTextUI(
            f'You are on Planet {self.currentPlanet.getName()}. You are alone. You wander')
        self.textUI.printtoTextUI(
            "around the vast void of universe traversing through different planets.")
        self.textUI.printtoTextUI("Your task is to find the Metaverse orb")
        self.textUI.printtoTextUI(
            "which can be found on any of the planets in the universe. All you need to do is EXPLORE!")
        self.textUI.printtoTextUI("")
        self.textUI.printtoTextUI(
            f'Your command words are: {self.showCommandWords()}')
        self.textUI.printtoTextUI(
            f'Your exits are: {self.currentPlanet.getExits()}')

    def showCommandWords(self):
        """
            Show a list of available commands
        :return: None
        """
        return ['help', 'go', 'quit']

    def processCommand(self, command):
        """
            Process a command from the TextUI
        :param command: a 2-tuple of the form (commandWord, secondWord)
        :return: True if the game has been quit, False otherwise
        """
        commandWord, secondWord = command
        if commandWord != None:
            commandWord = commandWord.upper()

        endGame = False
        if commandWord == "HELP":
            self.doPrintHelp()
        elif commandWord == "GO":
            endGame = self.doGoCommand(secondWord)
        elif commandWord == "QUIT":
            endGame = True
        else:
            # Unknown command ...
            self.textUI.printtoTextUI("Don't know what you mean")

        return endGame

    def doGoCommand(self, secondWord):
        """
            Performs the GO command
        :param secondWord: the direction the player wishes to travel in
        :return: None
        """

        requiredItems = {"Earth": ["orbHolder"], "Pluto": ["key"]}
        if secondWord == None:
            # Missing second word ...
            self.textUI.printtoTextUI("Go where?")
            return
        endGame = False
        nextPlanet = self.currentPlanet.getExit(secondWord)
        if nextPlanet == None:
            self.textUI.printtoTextUI("There is no such planet!")
        else:
            self.ship.subHops()
            if self.ship.hops == 0:
                self.textUI.printtoTextUI("You don't have any hops left!")
                endGame = True
            else:
                allowedToEnter = self.canEnter(
                    "earth", ["orbHolder"]) and self.canEnter("pluto", ["key"])
                if allowedToEnter:
                    self.currentPlanet = nextPlanet
                    hops = self.currentPlanet.hops
                    
                    
                    if hops > 0:
                        self.ship.addHops(hops)
                        self.textUI.printtoTextUI(
                            f"\nFuel found. {hops} hop/s added.")
                        hops = 0
                    self.textUI.printtoTextUI(
                        f'You have {self.ship.hops} hops remaining!')
                    self.textUI.printtoTextUI(
                        f"You currently have these items in your inventory: {self.ship.inventory}")
                    if len(self.currentPlanet.items) != 0:
                        self.textUI.printtoTextUI(
                            f"There are few items found on this planet: {self.currentPlanet.items}\n")
                        for i in self.currentPlanet.items:
                            acceptItem = input(
                                f"Do you want to add {i} in your inventory? Yes or No : ")
                            if acceptItem.lower() == "yes":
                                self.ship.addItem(i)
                    self.textUI.printtoTextUI(
                        self.currentPlanet.getLongDescription())
                    if(self.currentPlanet.getName() == "Dagobah"):
                        self.textUI.printtoTextUI("Careful you are attack by Darth Vader! Take out your starsaber.")
                        if "starsaber" in self.ship.inventory:
                            self.textUI.printtoTextUI("You successfully invade Dark Vader attack.")
                            self.ship.inventory.remove("starsaber")
                        else:
                            self.textUI.printtoTextUI(f"Oh no! You don't have starsaber you lost hops.")
                            self.ship.addHops(hops)
                            if self.ship.hops > 0:
                                self.textUI.printtoTextUI(f'You have {self.ship.hops} hops remaining!')
                            else:
                                endGame = True
                    if self.currentPlanet.getName() == "Earth":
                        self.textUI.printtoTextUI(
                            'You have found the Metaverse Orb.')
                        endGame = True
                else:
                    self.textUI.printtoTextUI(
                        'You do not have the following required items to enter the planet.')
                    self.textUI.printtoTextUI(requiredItems[nextPlanet.getName()])
                    self.textUI.printtoTextUI(f'Your exits are: {self.currentPlanet.getExits()}')
        return endGame


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
