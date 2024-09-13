class player:

    name = ""
    coins = 0
    suit = 0
    cards = []
    max_rerolls = 3
    rerolls = 0
    dice = 3
    
    def __init__(self) -> None:
        pass

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("Coins:", self.coins)
        # Check the suit number and print its name
        if self.suit == 0:
            print("Suit: Unselected")
        if self.suit == 1:
            print("Suit: Clubs")
        if self.suit == 2:
            print("Suit: Hearts")
        if self.suit == 3:
            print("Suit: Spades")
        if self.suit == 4:
            print("Suit: Diamonds")
        # Print remaining player information
        print("Cards:", self.cards)
        print("Dice:", self.dice)
        print("Max amount of Rerolls:", self.max_rerolls)
        print("Current Rerolls:", self.rerolls)