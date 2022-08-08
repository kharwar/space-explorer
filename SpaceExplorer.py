from Planet import Planet
from Ship import Ship
import tkinter as tk


class Game:

    def __init__(self):
        """
        Initializes the game
        """
        self.createPlanets()
        self.ship = Ship('StarLight')
        self.currentPlanet = self.worlorm

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

    def canEnter(self, nextPlanet, planetKey, items):
        if nextPlanet.getName().lower() == planetKey:
            for item in items:
                if item not in self.ship.inventory:
                    return False
        return True

    def play(self, root):
        try:
            """
                The main play loop
            :return: None
            """
            self.frame1 = tk.Frame(root, width=690, height=150,
                                   bg='BLUE', borderwidth=2)
            self.frame1.pack_propagate(0)   # Prevents resizing
            self.frame2 = tk.Frame(root, width=690, height=150,
                                   borderwidth=2)
            self.frame2.grid_propagate(0)   # Prevents resizing
            # This packs both frames into the root window ...
            self.frame3 = tk.Frame(
                root, width=690, height=400, borderwidth=2, bg="LIGHT BLUE")
            self.frame3.pack_propagate(0)
            self.frame1.pack()
            self.frame2.pack()
            self.frame3.pack(expand=True)

            self.textArea1 = tk.Label(self.frame1, text='')
            self.textArea1.pack()
            self.cmdArea = tk.Entry(self.frame2, text='', width=600)
            self.cmdArea.pack()

            self.imageArea = tk.Label(self.frame3, image='')
            self.imageArea.pack(side="bottom", fill="both", expand="yes")
            self.buildGUI()
        except:
            print('Unknown error')

    def buildGUI(self):
        try:
            self.image = tk.PhotoImage(file='images/worlorm.png')
            self.doCmd = tk.Button(self.frame2, text='Run command',
                                   fg='white', bg='blue',
                                   command=self.doCommand)
            self.doCmd.pack()
            self.textArea1.configure(text=self.doPrintHelp())
            self.imageArea.configure(image=self.image)
        except:
            print('Unknown error')

    def doCommand(self):
        try:
            command = self.cmdArea.get()  # Returns a 2-tuple
            self.processCommand(command)
        except:
            print('Unknown error')

    def getCommandString(self, inputLine):
        """
            Fetches a command (borrowed from old TextUI)
        :return: a 2-tuple of the form (commandWord, secondWord)
        """
        try:
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
        except:
            print('Unknown error')

    def processCommand(self, command):
        try:
            endGame = False
            commandWord, secondWord = self.getCommandString(command)
            if commandWord != None:
                commandWord = commandWord.upper()
                if commandWord == "HELP":
                    self.textArea1.configure(text=self.doPrintHelp())
                elif commandWord == "GO":
                    (endGame, msg) = self.doGoCommand(secondWord)
                    if endGame:
                        self.doCmd['state'] = 'disabled'
                    self.textArea1.configure(text=msg)
                    self.imageArea.configure(image=self.image)
                else:
                    # Unknown command ...
                    self.textArea1.configure(text="Don't know what you mean")

                for i in self.currentPlanet.items:
                    # TODO: find a solution to accept items in the
                    self.textArea1.configure(
                        text=f'Do you want to add {i} in your inventory? Yes or No : ')
                    acceptItem = self.cmdArea.get()
                    if acceptItem.upper()[0] == "Y":
                        # self.ship.addItem(i)
                        self.textArea1.configure(text=f'''{self.ship.addItem(i)}\n 
                        {self.currentPlanet.getLongDescription()}''')
                    elif acceptItem.upper()[0] == "N":
                        self.textArea1.configure(text=f'''{self.ship.getItems()}\n
                        {self.currentPlanet.getLongDescription()}''')
            return endGame
        except:
            print('Unknown error')

    def doPrintHelp(self):
        """
            Displays a welcome message
        :return:
        """
        try:
            msg = f'''You are on Planet {self.currentPlanet.getName()}. You are alone. You
            around the vast void of universe traversing through different planets.
            which can be found on any of the planets in the universe. All you need to do is EXPLORE!

            Your command words are: {self.showCommandWords()}
            Your exits are: {self.currentPlanet.getExits()}
            '''
            return msg
        except:
            print('Unknown error')

    def showCommandWords(self):
        """
            Show a list of available commands
        :return: None
        """
        try:
            return ['help', 'go']
        except:
            print('Unknown error')

    def doGoCommand(self, secondWord):
        """
            Performs the GO command
        :param secondWord: the direction the player wishes to travel in
        :return: None
        """
        try:

            msg = ''
            requiredItems = {"Earth": ["orbHolder"], "Pluto": ["key"]}
            if secondWord == None:
                # Missing second word ...
                msg += "Go where?"
                return
            endGame = False
            nextPlanet = self.currentPlanet.getExit(secondWord)
            if nextPlanet == None:
                msg = msg + "There is no such nearby planet!\n" + \
                    self.currentPlanet.getLongDescription()
            else:
                self.ship.subHops()
                if self.ship.hops == 0:
                    msg = msg + "You don't have any hops left!"
                    endGame = True
                else:
                    allowedToEnter = self.canEnter(nextPlanet,
                                                   "earth", ["orbHolder"]) and self.canEnter(nextPlanet, "pluto", ["key"])
                    if allowedToEnter:
                        self.currentPlanet = nextPlanet
                        self.image = tk.PhotoImage(
                            file=f'images/{self.currentPlanet.getName()}.png')
                        hops = self.currentPlanet.hops
                        if hops > 0:
                            self.ship.addHops(hops)
                            msg += f"\nFuel found. {hops} hop/s added."
                            hops = 0
                        msg += f'\nYou have {self.ship.hops} hops remaining!'
                        msg += f"\nYou currently have these items in your inventory: {self.ship.inventory}"
                        if len(self.currentPlanet.items) != 0:

                            msg += f"\nThere are few items found on this planet: {self.currentPlanet.items}\n"
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
                        msg += '\nYou do not have the following required items to enter the planet.\n'
                        msg += requiredItems[nextPlanet.getName()][0]
                        msg += f'\nYour exits are: {self.currentPlanet.getExits()}'
            return (endGame, msg)
        except:
            print('Unknown error')


def main():
    try:
        game = Game()
        win = tk.Tk()
        win.title("Space Explorer with GUI")   # Set window title
        win.geometry("690x690")                 # Set window size
        win.resizable(False, False)             # Both x and y dimensions ...
        game.play(win)
        win.mainloop()
    except:
        print('Unknown error')


if __name__ == "__main__":
    main()
