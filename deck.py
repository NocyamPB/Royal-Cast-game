class deck:
    cards = []

    def __init__(self, name, orientation):
        self.name = name    
        self.orientation = orientation

    def display(self):
        for card in self.cards[:]:
            card.display()
    
    def __str__(self):
        for card in self.cards[:]:
            print(card)
        return ""
    