class card:

    name = ""
    code = ""
    suit = 0
    value = 0
    royal = False

    def __init__(self, name, code, suit, value, royal):
        self.name = name
        self.code = code
        self.suit = suit
        self.value = value
        self.royal = royal


    def display(self):
        print("Name:", self.name)
        # Check the suit number and print its name
        if self.suit == 0:
            print("Suit: Unknown")
        if self.suit == 1:
            print("Suit: Clubs")
        if self.suit == 2:
            print("Suit: Hearts")
        if self.suit == 3:
            print("Suit: Spades")
        if self.suit == 4:
            print("Suit: Diamonds")
        if self.suit == 5:
            print("Suit: Joker")
        # Print remaining card information
        print("Value:", self.value)
        print("Royal Card:", self.royal)


    def __str__(self):
        return self.code