import tkinter as tk
from tkinter import Label, Frame, DISABLED, Entry, Button, NORMAL
import random

number = random.randint(1, 100)
chance = 10


class GuessGame:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Guessing Game")
        self.root.geometry("+150+50")
        self.root.minsize(600, 550)
        self.root.resizable(False, False)
        self.setupRoot()

    def setupRoot(self):
        # Frame 1
        self.leftFrame = Frame(self.root, bg="black")
        self.leftFrame.place(relwidth=0.5, relheight=1, relx=0, rely=0)

        # Label 1
        self.titleLabel = Label(self.leftFrame, text="Guessing Game", bg="black", fg="darkgoldenrod1",
                                font=("Times New Roman", 28, "bold"))
        self.titleLabel.place(relx=0.01, rely=0.4, relwidth=0.99, relheight=0.09)

        # Label 2
        self.textLabel = Label(self.leftFrame, text="Guess the number between 1 to 100.\nYou have 10 chances to win",
                               bg="black", fg="cyan", font=("Times New Roman", 13))
        self.textLabel.place(relx=0.01, rely=0.5, relwidth=0.99, relheight=0.09)

        # Start button
        self.startButton = Button(self.leftFrame, text="Start", bg="black", fg="white", borderwidth=2,
                                  font=("Times New Roman", 12), command=self.start)
        self.startButton.place(relx=0.2, rely=0.6, relwidth=0.3, relheight=0.06)
        self.startButton.config(state=DISABLED)

        # End button
        self.endButton = Button(self.leftFrame, text="Quit", bg="black", fg="white", borderwidth=2,
                                font=("Times New Roman", 12), command=lambda: self.quit(None))
        self.endButton.place(relx=0.52, rely=0.6, relwidth=0.3, relheight=0.06)

        # ******************** Right Frame ********************
        # Frame 2
        self.rightFrame = Frame(self.root, bg="white")
        self.rightFrame.place(relwidth=0.5, relheight=1, relx=0.5, rely=0)

        # Entry
        self.outputEntry = Label(self.root, bg="white", borderwidth=2)
        self.outputEntry.place(relx=0.6, rely=0.1, relwidth=0.3, relheight=0.07)
        self.outputEntry.configure(state=DISABLED)

        # Label 3
        self.inputLabel = Label(self.rightFrame, text="Guess the number", bg="white", fg="darkgreen",
                                font=("Times New Roman", 15, "bold"))
        self.inputLabel.place(relx=0.01, rely=0.4, relwidth=0.99, relheight=0.09)

        # Entry
        self.inputEntry = Entry(self.rightFrame, bg="white", highlightcolor="black", highlightthickness=2)
        self.inputEntry.place(relx=0.21, rely=0.5, relwidth=0.3, relheight=0.06)
        self.inputEntry.bind('<Return>', lambda event=None: self.guessNumber())
        self.inputEntry.focus()

        # Guess button
        self.guessButton = Button(self.rightFrame, text="Guess", bg="white", fg="black", borderwidth=2,
                                  font=("Times New Roman", 12), command=self.guessNumber)
        # make the guess button on action by clicking enter
        # self.guessButton.bind('<Return>', lambda event=None: self.guessNumber())
        self.guessButton.place(relx=0.53, rely=0.5, relwidth=0.2, relheight=0.06)

        # Actual number button
        self.ActualButton = Button(self.rightFrame, text="See", bg="white", fg="purple", borderwidth=2,
                                   font=("Times New Roman", 12), command=self.actualNumber)
        self.ActualButton.place(relx=0.75, rely=0.5, relwidth=0.2, relheight=0.06)
        self.ActualButton.config(state=DISABLED)

        # Label 4
        self.chanceLabel = Label(self.rightFrame, text=f"Chances Left: {chance}", bg="white", fg="black",
                                 font=("Times New Roman", 12))
        self.chanceLabel.place(relx=0.01, rely=0.59, relwidth=0.9, relheight=0.06)

    def guessNumber(self):
        global chance
        guess = 0
        guess1 = self.inputEntry.get()
        if guess1.strip() and guess1.isdigit():
            guess = int(guess1)
        self.inputEntry.delete(0, "end")

        if guess == number:
            self.outputEntry.configure(state=NORMAL)
            self.startButton.config(state=NORMAL)
            self.outputEntry.configure(text="You Win", fg="cyan", font=("Times New Roman", 20, "bold"))
            self.outputEntry.configure(state=DISABLED)
            self.guessButton.configure(state=DISABLED)
        elif guess < number:
            self.outputEntry.configure(text="Low.. Try again", fg="blue", font=("Times New Roman", 15, "bold"))
        else:
            self.outputEntry.configure(text="High.. Try again", fg="blue", font=("Times New Roman", 15, "bold"))

        chance -= 1
        self.chanceLabel.configure(text=f"Left Chances: {chance}", fg="black", font=("Times New Roman", 15, "bold"))

        if chance == 0:
            self.outputEntry.config(state=NORMAL)
            self.outputEntry.config(text="Game Over", fg="red", font=("Times New Roman", 20, "bold"))
            self.outputEntry.config(state=DISABLED)
            self.guessButton.configure(state=DISABLED)
            self.startButton.config(state=NORMAL)
            self.ActualButton.config(state=NORMAL)

    def start(self):
        global chance
        global number
        chance = 10
        number = random.randint(1, 100)
        self.chanceLabel.config(text=f"Left Chances: {chance}", font=("Times New Roman", 15, "bold"))
        self.startButton.config(state=DISABLED)
        self.outputEntry.configure(state=NORMAL)
        self.outputEntry.configure(text="")
        self.outputEntry.configure(state=DISABLED)
        self.guessButton.configure(state=NORMAL)
        self.inputEntry.focus()
        self.inputEntry.delete(0, "end")

    def actualNumber(self):
        self.outputEntry.config(state=NORMAL)
        self.outputEntry.config(text=f"The number was: {number}", font=("Times New Roman", 15, "bold"))
        self.outputEntry.config(state=DISABLED)
        self.ActualButton.config(state=DISABLED)

    def quit(self, event):
        self.root.destroy()


if __name__ == "__main__":
    game = GuessGame()
    game.root.mainloop()
