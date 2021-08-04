suite = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
rank = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, }
#create a card


class Card:
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank

    def card_show(self):
        print("{} of {}".format(self.rank, self.suite))
#
# carte = Card("PIKE",6)
# carte.card_show()