import random


class Player:
    def __init__(self, name):
        self.name = name
        self.chips = 100
        self.bet = 0  # the bet the player chooses.

    def setBet(self, amount):
        """Set the player bet. Pass in the amount as arguement."""
        if amount > self.chips:
            print("You don't have that many chips.")
            self.bet = 0
        elif amount <= 0:
            print("You can't play without chips.\nPlease reset your chips.")
            self.bet = 0
        else:
            self.bet = amount

    def resetChips(self):
        self.chips = 100


class Slot:
    def __init__(self):
        self.symboles = ['apple', 'cherry', 'banana', 'peach', 'strawberry']
        # assign symbol variables.
        self.s1, self.s2, self.s3 = 0, 0, 0

    def spin(self):
        self.s1, self.s2, self.s3 = random.randint(0, len(self.symboles)-1), random.randint(
            0, len(self.symboles)-1), random.randint(0, len(self.symboles)-1)
        return self.s1, self.s2, self.s3

    def display(self, info):
        """This function expects a tuple as arguement. We are only going to access 3 items from the tuple."""
        print(
            f"The wheel landed on {self.symboles[info[0]]}, {self.symboles[info[1]]}, {self.symboles[info[2]]}")


class Game:
    def __init__(self, slot, player):
        """Takes a slot and player object as arguements."""
        self.slot = slot
        self.player = player

    def initialize(self):
        """Set up everything to start playing."""
        self.player.setBet(
            10)  # give the player a default bet of 10 to get started.
        print(
            f"Welcome to simple slots {self.player.name}.\nYou have {self.player.chips} chips to spend and your current bet is set to {self.player.bet} chips.")

    def play(self, number):
        """This method is for when the user actually plays the game. Spinning, betting , exiting or resetting chips for now. The number represents the option"""
        if number == 0:
            if not self.player.bet > self.player.chips and self.player.chips > 0 and self.player.bet > 0:
                s = self.slot.spin()
                self.slot.display(s)
                self.checkWin(list(s))
            else:
                print("You don't have enough chips. Reset them or change your bet.")
            print(
                f"You have {self.player.chips} chips remaining and your bet is set to {self.player.bet} chips.")
        elif number == 1:
            # set the player's bet
            try:
                self.player.setBet(int(input("Please set your bet.")))
            except:
                print("Only enter a number.\nPlease try again.")
            print(f"Your bet is set to {self.player.bet}.")
        elif number == 2:
            self.player.resetChips()  # reset the player's chips amount
            print(f"Your chips total has been reset to {self.player.chips}.")
        elif number == 3:
            self.exit()  # quit the game.
        else:
            print("That option is invalid. Please try again.")

    def processInput(self):
        """Process the input of the player. Return a number. Each number will represent an option for when the user playes the game. If -1 is returned, there is an error. else if the number is greater than or equal to 0, it is a valid option. Only valid options must be supplied."""
        options = ["spin", "bet", "resetChips",
                   "exit"]  # The possible choices the player can enter.
        text = input(
            f"Please enter an option.\nYou can choose from the following:\n{','.join(options)}")
        if not text in options:
            return -1
        else:
            return options.index(text)

    def exit(self):
        """Exit the game."""
        print(f"Thank you {self.player.name} for playing.")
        quit()

    def checkWin(self, lst):
        """Expects a list as an arguement. the list will be compared to possible winning conditions. Based on this, you either gain or looze chips."""
        possibleWinConditions = [[0, 0, 0], [
            1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
        if lst in possibleWinConditions:
            self.player.chips += self.player.bet*2
            print(
                f"You hit the jackpot!\nYou received {self.player.bet*2} chips.")
        else:
            self.player.chips -= self.player.bet
            print(
                f"You lost {self.player.bet} chips.")


def start():
    gameSlot = Slot()
    gamePlayer = Player(input("Enter your name"))
    mainGame = Game(gameSlot, gamePlayer)
    mainGame.initialize()
    while 1:
        mainGame.play(mainGame.processInput())


start()
