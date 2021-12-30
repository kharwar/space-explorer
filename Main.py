from SpaceExplorer import Game
import tkinter as tk


class App():

    # Creates a Frame for the application
    # and populates the GUI ...
    def __init__(self, root):

        self.game = Game()

        # Create two frames owned by the window root
        # In order to use multiple layout managers, the frames
        # cannot share a parent frame. Here both frames are owned
        # by a top level instance root.

        self.frame1 = tk.Frame(root, width=400, height=150,
                               bg='BLUE', borderwidth=2)
        self.frame1.pack_propagate(0)   # Prevents resizing
        self.frame2 = tk.Frame(root, width=400, height=150,
                               bg='LIGHT GREY', borderwidth=2)
        self.frame2.grid_propagate(0)   # Prevents resizing
        # This packs both frames into the root window ...
        self.frame1.pack()
        self.frame2.pack()

        # Now add some useful widgets ...
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
        self.textArea1.configure(text=self.game.doPrintHelp())

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
                self.textArea1.configure(text=self.game.doPrintHelp())
            elif commandWord == "GO":
                (endGame, msg) = self.game.doGoCommand(secondWord)
                self.textArea1.configure(text=msg)
            else:
                # Unknown command ...
                self.textArea1.configure(text="Don't know what you mean")
        return endGame


def main():
    win = tk.Tk()                           # Create a window
    win.title("Adventure World with GUI")   # Set window title
    win.geometry("400x300")                 # Set window size
    win.resizable(False, False)             # Both x and y dimensions ...

    # Create the GUI as a Frame
    # and attach it to the window ...
    myApp = App(win)

    # Call the GUI mainloop ...
    win.mainloop()


if __name__ == "__main__":
    main()
