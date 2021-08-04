from Hand import Hand
from Deck import Deck


class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand()

    def draw_a_card(self):
        return self.deck.draw_card()

    def draw_self_card(self):
        self.hand.add_card(self.draw_a_card())

    def get_hand_value(self):
        return self.hand.get_hand_value()

    def empty_hand(self):
        self.hand.clear()

    def shuffle_deck(self):
        self.deck.shuffle()

    def reset_deck(self):
        self.deck = Deck()
        self.deck.shuffle()
