from cards import Card
from cards import values
from Deck import Deck


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def get_hand_value(self):
        if self.has_ace():
            return self.value, self.value + 10
        return self.value

    def clear(self):
        self.cards = []
        self.value = 0

    def has_ace(self):
        for card in self.cards:
            if card.rank == "Ace":
                return True




