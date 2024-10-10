from card import card
from deck import deck

import random

# Information of each possible card in the game
# Index 0  - 12,  suit = Clubs,    id: 1
# Index 13 - 25,  suit = Hearts,   id: 2 
# Index 26 - 38,  suit = Spades,   id: 3
# Index 39 - 51,  suit = Diamonds, id: 4
# Index 52 - 53,  suit = Jokers,   id: 5
CARD_INFO = (
    card("Ace of Clubs", "A *t*", 1, 15, False),
    card("Two of Clubs", "2 *t*", 1, 2, False),
    card("Three of Clubs", "3 *t*", 1, 3, False),
    card("Four of Clubs", "4 *t*", 1, 4, False),
    card("Five of Clubs", "5 *t*", 1, 5, False),
    card("Six of Clubs", "6 *t*", 1, 6, False),
    card("Seven of Clubs", "7 *t*", 1, 7, False),
    card("Eight of Clubs", "8 *t*", 1, 8, False),
    card("Nine of Clubs", "9 *t*", 1, 9, False),
    card("Ten of Clubs", "10 *t*", 1, 10, False),
    card("Jack of Clubs", "J *t*", 1, 11, True),
    card("Queen of Clubs", "Q *t*", 1, 12, True),
    card("King of Clubs", "K *t*", 1, 13, True),
    card("Ace of Hearts", "A <3", 2, 15, False),
    card("Two of Hearts", "2 <3", 2, 2, False),
    card("Three of Hearts", "3 <3", 2, 3, False),
    card("Four of Hearts", "4 <3", 2, 4, False),
    card("Five of Hearts", "5 <3", 2, 5, False),
    card("Six of Hearts", "6 <3", 2, 6, False),
    card("Seven of Hearts", "7 <3", 2, 7, False),
    card("Eight of Hearts", "8 <3", 2, 8, False),
    card("Nine of Hearts", "9 <3", 2, 9, False),
    card("Ten of Hearts", "10 <3", 2, 10, False),
    card("Jack of Hearts", "J <3", 2, 11, True),
    card("Queen of Hearts", "Q <3", 2, 12, True),
    card("King of Hearts", "K <3", 2, 13, True),
    card("Ace of Spades", "A =S>", 3, 15, False),
    card("Two of Spades", "2 =S>", 3, 2, False),
    card("Three of Spades", "3 =S>", 3, 3, False),
    card("Four of Spades", "4 =S>", 3, 4, False),
    card("Five of Spades", "5 =S>", 3, 5, False),
    card("Six of Spades", "6 =S>", 3, 6, False),
    card("Seven of Spades", "7 =S>", 3, 7, False),
    card("Eight of Spades", "8 =S>", 3, 8, False),
    card("Nine of Spades", "9 =S>", 3, 9, False),
    card("Ten of Spades", "10 =S>", 3, 10, False),
    card("Jack of Spades", "J =S>", 3, 11, True),
    card("Queen of Spades", "Q =S>", 3, 12, True),
    card("King of Spades", "K =S>", 3, 13, True),
    card("Ace of Diamonds", "A <^>", 4, 15, False),
    card("Two of Diamonds", "2 <^>", 4, 2, False),
    card("Three of Diamonds", "3 <^>", 4, 3, False),
    card("Four of Diamonds", "4 <^>", 4, 4, False),
    card("Five of Diamonds", "5 <^>", 4, 5, False),
    card("Six of Diamonds", "6 <^>", 4, 6, False),
    card("Seven of Diamonds", "7 <^>", 4, 7, False),
    card("Eight of Diamonds", "8 <^>", 4, 8, False),
    card("Nine of Diamonds", "9 <^>", 4, 9, False),
    card("Ten of Diamonds", "10 <^>", 4, 10, False),
    card("Jack of Diamonds", "J <^>", 4, 11, True),
    card("Queen of Diamonds", "Q <^>", 4, 12, True),
    card("King of Diamonds", "K <^>", 4, 13, True),
    card("Red Joker", "$Joker#", 5, 10, True),
    card("Black Joker", "@Joker!", 5, 10, True)
)

class deckController:
    
    main_deck = []
    side_deck = []


    """ 
    Constructor to the deck controller. 
    If player attribute is false, then create the main and discard deck of the game.
    Otherwise, the player has two decks: the main deck becomes the royal cards, and the 
     side deck becomes the points deck.
    """
    def __init__(self, player):
        if player:
            self.main_deck = deck(player.name + "'s Royal cards", 1)
            self.side_deck = deck("'s Points deck", 1)
        else:
            self.main_deck = deck("Main Deck", 0)
            self.side_deck = deck("Discard Deck", 1)

    """
    Add a set of cards to the main deck 
    """
    def addCardSet(self, suit):
        if suit < 5:
            index = (12 * (suit - 1)) + (suit - 1)
            for card in CARD_INFO[index:(index + 13)]:
                self.main_deck.cards.append(card)
        else:
            for card in CARD_INFO[-2:]:
                self.main_deck.cards.append(card)

    """
    Shuffle the main deck 
    """
    def shuffle(self):
        random.shuffle(self.main_deck.cards)
    
    """
    Get card from main deck from position index.
    This method will be used in the game to visualize the card.
    """
    def getCardMainDeck(self, index):
        return self.main_deck[index]
    
    """
    Get card from side deck from position index.
    This method will be used in the game to visualize the card.
    """
    def getCardSideDeck(self, index):
        return self.side_deck[index]
    
    """
    Create a new full main deck with all cards shuffled 
    """
    def newFullDeck(self):
        for suit in range(1,6):
            self.addCardSet(suit)
        self.shuffle()

    """
    Draws the top card from main deck, which is the last one.
    It removes the card from the deck and returns it.
    """
    def draw(self):
        return self.main_deck.cards.pop()
    
    """
    Adds the card passed as parameter to the bottom of the main deck.
    """
    def addCardToBottom(self, card):
        self.main_deck.insert(0, card)
    
    """
    Add the card passed as parameter to the deck passed as parameter 
    """
    def addCardToDeck(self, card, deck):
        deck.append(card)
    
    """
    Search deck passed as parameter for position of the card passed as parameter, if exists. 
    If the card exists, returns the index position of the card. Otherwise, returns False. 
    """
    def searchCardIndex(self, card, deck):
        for index in range(0, len(deck)):
            if deck[index] == card:
                return index
        return False
    
    """
    Removes the card passed as parameter from the deck passed as parameter, if exists.
    Returns the removed card. If the card doesn't exists, returns False. 
    """
    def removeCard(self, card, deck):
        index = self.searchCardIndex(card, deck)
        if index != False:
            return deck.pop(index)
        return False