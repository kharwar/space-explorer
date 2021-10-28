from Room import Room
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
        self.currentRoom = self.outside
        self.textUI = TextUI()

    def createPlanets(self):
        """
            Sets up all Planets
        :return: None
        """
        self.worlorm = Room("You are on the Worlorm Planet(Its a initial or Starting Point of the Game))")
        self.Cybertron=Room
        self.corridor = Room("in a corridor")
        self.lab = Room("in a computing lab")
        self.office = Room("in the computing admin office")





        self.worlorm.setExit("east", self.lobby)
        self.worlorm.setExit("south", self.lab)
        self.worlorm.setExit("west", self.corridor)
        self.lobby.setExit("west", self.worlorm)
        self.corridor.setExit("east", self.worlorm)
        self.lab.setExit("north", self.worlorm)
        self.lab.setExit("east", self.office)
        self.office.setExit("west", self.lab)

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

        nextRoom = self.currentRoom.getExit(secondWord)
        if nextRoom == None:
            self.textUI.printtoTextUI("There is no door!")
        else:
            self.currentRoom = nextRoom
            self.textUI.printtoTextUI(self.currentRoom.getLongDescription())

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()