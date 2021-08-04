import random
import datetime
from cards import Card
from cards import suite
from cards import rank


class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        for x in suite:
            for z in rank:
                self.cards.append(Card(x, z))

    def show_deck(self):
        for e in self.cards:
            e.card_show()

    def shuffle(self):
        timestamp = datetime.datetime.now().timestamp()
        random.Random(timestamp).shuffle(self.cards)

    def draw_card(self):
        card = self.cards.pop()
        return card

# deck = Deck()
# deck.shuffle()
# deck.show_deck()
# card = deck.draw_card_pack()
# # deck.card_show()
