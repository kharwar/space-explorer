from Planet import Planet
from Ship import Ship
from TextUI import TextUI
import tkinter as tk
"""
    This class is the main class of the "Space Explorer" application.
    'Space Explorer' is a very simple, text based adventure game.

    To play this game, create an instance of this class and call the "play"
    method.
"""


# TODO: Add images for each planet
# TODO: Remove textUI attributes everywhere

class Game:

    def __init__(self):
        """
        Initializes the game
        """
        self.createPlanets()
        self.ship = Ship('StarLight')
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

    def play(self, root):
        """
            The main play loop
        :return: None
        """
        # self.doPrintHelp()
        # finished = False
        # while (finished == False):
        #     command = self.textUI.getCommand()      # Returns a 2-tuple
        #     finished = self.processCommand(command)

        # print("Thank you for playing!")
        self.frame1 = tk.Frame(root, width=400, height=150,
                               bg='BLUE', borderwidth=2)
        self.frame1.pack_propagate(0)   # Prevents resizing
        self.frame2 = tk.Frame(root, width=400, height=150,
                               bg='LIGHT GREY', borderwidth=2)
        self.frame2.grid_propagate(0)   # Prevents resizing
        # This packs both frames into the root window ...
        self.frame1.pack()
        self.frame2.pack()

        self.textArea1 = tk.Label(self.frame1, text='')
        self.textArea1.pack()
        self.cmdArea = tk.Entry(self.frame2, text='')
        self.cmdArea.pack()
        self.buildGUI()

    def buildGUI(self):
        self.doCmd = tk.Button(self.frame2, text='Run command',
                               fg='black', bg='blue',
                               command=self.doCommand)
        self.doCmd.pack()
        self.textArea1.configure(text=self.doPrintHelp())

    def doCommand(self):
        command = self.cmdArea.get()  # Returns a 2-tuple
        self.processCommand(command)

    def getCommandString(self, inputLine):
        """
            Fetches a command (borrowed from old TextUI)
        :return: a 2-tuple of the form (commandWord, secondWord)
        """
        word1 = None
        word2 = None
        if inputLine != "":
            allWords = inputLine.split()
            word1 = allWords[0]
            if len(allWords) > 1:
                word2 = allWords[1]
            else:
                word2 = None
            # Just ignore any other words
        return (word1, word2)

    def processCommand(self, command):
        commandWord, secondWord = self.getCommandString(command)
        if commandWord != None:
            commandWord = commandWord.upper()
            if commandWord == "HELP":
                self.textArea1.configure(text=self.doPrintHelp())
            elif commandWord == "GO":
                (endGame, msg) = self.doGoCommand(secondWord)
                self.textArea1.configure(text=msg)
            else:
                # Unknown command ...
                self.textArea1.configure(text="Don't know what you mean")
        return endGame

    def doPrintHelp(self):
        """
            Displays a welcome message
        :return:
        """
        msg = f'''You are on Planet {self.currentPlanet.getName()}. You are alone. You
        around the vast void of universe traversing through different planets.
        which can be found on any of the planets in the universe. All you need to do is EXPLORE!

        Your command words are: {self.showCommandWords()}
        Your exits are: {self.currentPlanet.getExits()}
        '''
        return msg

    def showCommandWords(self):
        """
            Show a list of available commands
        :return: None
        """
        return ['help', 'go']

    # ____________ processCommand function is used from Main.py

    # def processCommand(self, command):
    #     """
    #         Process a command from the TextUI
    #     :param command: a 2-tuple of the form (commandWord, secondWord)
    #     :return: True if the game has been quit, False otherwise
    #     """
    #     commandWord, secondWord = command
    #     if commandWord != None:
    #         commandWord = commandWord.upper()

    #     endGame = False
    #     if commandWord == "HELP":
    #         self.doPrintHelp()
    #     elif commandWord == "GO":
    #         (endGame, msg) = self.doGoCommand(secondWord)

    #     elif commandWord == "QUIT":
    #         (endGame, msg) = True
    #     else:
    #         # Unknown command ...
    #         self.textUI.printtoTextUI("Don't know what you mean")

    #     return endGame

    def doGoCommand(self, secondWord):
        """
            Performs the GO command
        :param secondWord: the direction the player wishes to travel in
        :return: None
        """
        msg = ''
        requiredItems = {"Earth": ["orbHolder"], "Pluto": ["key"]}
        if secondWord == None:
            # Missing second word ...
            msg += "Go where?"
            return
        endGame = False
        nextPlanet = self.currentPlanet.getExit(secondWord)
        if nextPlanet == None:
            # self.textUI.printtoTextUI("There is no such planet!")
            msg = msg + "There is no such planet!"
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
                        msg += f"\nFuel found. {hops} hop/s added."
                        hops = 0
                    msg += f'\nYou have {self.ship.hops} hops remaining!'
                    msg += f"\nYou currently have these items in your inventory: {self.ship.inventory}"
                    if len(self.currentPlanet.items) != 0:

                        msg += f"\nThere are few items found on this planet: {self.currentPlanet.items}\n"
                        for i in self.currentPlanet.items:
                            # TODO: find a solution to accept items in the
                            self.textArea1.configure(
                                text=f'Do you want to add {i} in your inventory? Yes or No : ')
                            acceptItem = self.cmdArea.get()
                            if acceptItem.upper()[0] == "Y":
                                self.ship.addItem(i)
                    msg += '\n'
                    msg += self.currentPlanet.getLongDescription()
                    if(self.currentPlanet.getName() == "Dagobah"):
                        msg += "\nCareful you are attacked by Darth Vader! Take out your starsaber."
                        if "starsaber" in self.ship.inventory:
                            msg += "\nYou successfully invade Dark Vader attack."
                            self.ship.inventory.remove("starsaber")
                        else:
                            msg += "Oh no! You don't have starsaber you lost hops."
                            self.ship.addHops(hops)
                            if self.ship.hops > 0:
                                msg += f'\nYou have {self.ship.hops} hops remaining!'
                            else:
                                endGame = True
                    if self.currentPlanet.getName() == "Earth":
                        msg += '\nYou have found the Metaverse Orb.'
                        endGame = True
                else:
                    msg += '\nYou do not have the following required items to enter the planet.'
                    msg += requiredItems[nextPlanet.getName()]
                    msg += f'Your exits are: {self.currentPlanet.getExits()}'
        # return endGame
        return (endGame, msg)


def main():
    game = Game()
    win = tk.Tk()
    win.title("Adventure World with GUI")   # Set window title
    win.geometry("400x300")                 # Set window size
    win.resizable(False, False)             # Both x and y dimensions ...
    game.play(win)

    win.mainloop()


if __name__ == "__main__":
    main()
