from Planets import Planets
from TextUI import TextUI

"""
    This class is the main class of the "Adventure World" application. 
    'Adventure World' is a very simple, text based adventure game.  Users 
    can walk around some scenery. That's all. It should really be extended 
    to make it more interesting!
    
    To play this game, create an instance of this class and call the "play"
    method.

    This main class creates and initialises all the others: it creates all
    rooms, creates the parser and starts the game.  It also evaluates and
    executes the commands that the parser returns.
    
    This game is adapted from the 'World of Zuul' by Michael Kolling
    and David J. Barnes. The original was written in Java and has been
    simplified and converted to Python by Kingsley Sage
"""
class Game:

    def __init__(self):
        """
        Initialises the game
        """
        self.createPlanets()
        self.currentPlanets = self.worlorm
        self.textUI = TextUI()

    def createPlanets(self):
        """
            Sets up all Planets
        :return: None
        """
        self.worlorm = Planets("You are on the Worlorm Planet(Its a initial or Starting Point of the Game))")
        self.cybertron=Planets("These is a planet of Robots be Carefull and make friendship wisely")
        self.ego = Planets("These is a planet of a living tribual its not the safe planet")
        self.krypton = Planets("This planet is going to die soon")
        self.solaris = Planets("You have safely landed to Solaris")
        self.titan = Planets("This planet is where thanos lives")
        self.dagobah = Planets("This planet is well known planet of star Wars")
        self.vormir = Planets("This is the planet where you can get super powers")
        self.knowhere = Planets("This is the last planet where you can reach your destination")

        # Directions are up,left,right and south
        self.worlorm.setExit("right",self.cybertron)
        self.worlorm.setExit("down",self.ego)
        self.ego.setExit("up",self.worlorm)
        self.ego.setExit("right",self.krypton)
        self.ego.setExit("down",self.titan)
        self.cybertron.setExit("left",self.worlorm)
        self.cybertron.setExit("down",self.krypton)
        self.cybertron.setExit("right",self.dagobah)
        self.daggoobah.setExit("left",self.cybertron)
        self.dagobah.setExit("down",self.solaris)
        self.titan.setExit("up",self.ego)
        self.titan.setExit("right",self.vormir)
        self.krypton.setExit("up",self.cybertron)
        self.krypton.setExit("right",self.solaris)
        self.krypton.setExit("down",self.vormir)
        self.krypton.setExit("left",self.ego)
        self.solaris.setExit("up",self.dagobah)
        self.solaris.setExit("left",self.krypton)
        self.solaris.setExit("down",self.knowhere)
        self.vormir.setExit("up",self.krypton)
        self.vormir.setExit("left",self.titan)
        self.vormir.setExit("right",self.knowhere)
        self.knowhere.setExit("up",self.solaris)
        self.knowhere.setExit("left",self.vormir)

    def play(self):
        """
            The main play loop
        :return: None
        """
        self.printWelcome()
        finished = False
        while (finished == False):
            command = self.textUI.getCommand()      # Returns a 2-tuple
            finished = self.processCommand(command)

        print("Thank you for playing!")

    def printWelcome(self):
        """
            Displays a welcome message
        :return:
        """
        self.textUI.printtoTextUI("You are lost. You are alone. You wander")
        self.textUI.printtoTextUI("around the deserted complex.")
        self.textUI.printtoTextUI("")
        self.textUI.printtoTextUI(f'Your command words are: {self.showCommandWords()}')

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

        wantToQuit = False
        if commandWord == "HELP":
            self.doPrintHelp()
        elif commandWord == "GO":
            self.doGoCommand(secondWord)
        elif commandWord == "QUIT":
            wantToQuit = True
        else:
            # Unknown command ...
            self.textUI.printtoTextUI("Don't know what you mean")

        return wantToQuit

    def doPrintHelp(self):
        """
            Display some useful help text
        :return: None
        """
        self.textUI.printtoTextUI("You are lost. You are alone. You wander")
        self.textUI.printtoTextUI("around the deserted complex.")
        self.textUI.printtoTextUI("")
        self.textUI.printtoTextUI(f'Your command words are: {self.showCommandWords()}')

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

        nextPlanets = self.currentPlanets.getExit(secondWord)
        if nextPlanets == None:
            self.textUI.printtoTextUI("There is no door!")
        else:
            self.currentPlanets = nextPlanets
            self.textUI.printtoTextUI(self.currentPlanets.getLongDescription())

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
