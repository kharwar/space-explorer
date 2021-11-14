from Planet import Planet
from Player import Player
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
        self.player = Player('Starlord')
        self.currentPlanet = self.worlorm
        self.textUI = TextUI()

    def createPlanets(self):
        """
            Sets up all Planet
        :return: None
        """
        self.worlorm = Planet("You are on the Worlorm Planet", "Worlorm")
        self.cybertron = Planet(
            "These is a planet of Robots be Carefull and make friendship wisely", "Cybertron")
        self.ego = Planet(
            "These is a planet of a living tribual its not the safe planet", "Ego")
        self.krypton = Planet("This planet is going to die soon", "Krypton")
        self.solaris = Planet("You have safely landed to Solaris", "Solaris")
        self.titan = Planet("This planet is where thanos lives", "Titan")
        self.dagobah = Planet(
            "This planet is well known planet of star Wars", "Dagobah")
        self.vormir = Planet(
            "This is the planet where you can get super powers", "Vormir")
        self.knowhere = Planet(
            "This is the last planet where you can reach your destination", "Knowhere")

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
        self.titan.setExit("ego", self.ego)
        self.titan.setExit("vormir", self.vormir)
        self.krypton.setExit("cybertron", self.cybertron)
        self.krypton.setExit("solaris", self.solaris)
        self.krypton.setExit("vormir", self.vormir)
        self.krypton.setExit("ego", self.ego)
        self.solaris.setExit("dagobah", self.dagobah)
        self.solaris.setExit("krypton", self.krypton)
        self.solaris.setExit("down", self.knowhere)
        self.vormir.setExit("knowhere", self.krypton)
        self.vormir.setExit("titan", self.titan)
        self.vormir.setExit("knowhere", self.knowhere)
        self.knowhere.setExit("solaris", self.solaris)
        self.knowhere.setExit("vormir", self.vormir)

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
        if secondWord == None:
            # Missing second word ...
            self.textUI.printtoTextUI("Go where?")
            return
        endGame = False
        nextPlanet = self.currentPlanet.getExit(secondWord)
        if nextPlanet == None:
            self.textUI.printtoTextUI("There is no door!")
        else:
            self.currentPlanet = nextPlanet
            self.textUI.printtoTextUI(self.currentPlanet.getLongDescription())
            if self.currentPlanet.getName() == "Knowhere":
                self.textUI.printtoTextUI('You have found the Metaverse Orb.')
                endGame = True
        return endGame


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
