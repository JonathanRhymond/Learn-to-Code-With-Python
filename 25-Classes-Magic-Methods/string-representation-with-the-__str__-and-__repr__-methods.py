class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return (f"{self.rank} of {self.suit}")
    def __repr__(self):
        return (f'Card("{self.rank}", "{self.suit}")')

c = Card("Ace", "Spades")
print(c) # c.__str__()
print(str(c)) # c.__str__()
print(repr(c)) # c.__repr__()