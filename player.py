class player:

    name = ""
    player_id = 0
    coins = 0
    suit = 0
    cards = []
    max_rerolls = 3
    rerolls = 0
    dice = 3
    
    def __init__(self, name, id):
        self.name = name
        self.player_id = id

    def display(self):
        print("Name:", self.name)
        print("Player ID:", self.player_id)
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