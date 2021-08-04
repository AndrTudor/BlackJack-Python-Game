from Hand import Hand


class Player:
    def __init__(self, firstname, lastname, age, nationality, chips):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.nationality = nationality
        self.chips = chips
        self.hand = Hand()
        self.bet = 0

    def __str__(self):
        return 'Here we have a new player:\n' + self.firstname + ' ' \
               + self.lastname + ', at the age of ' + str(self.age) + ', coming from ' \
               + self.nationality + ', will enter with ' + str(self.chips) + ' chips in the game\n'

    def get_final_results(self):
        return "Player {} {} final amount: {}".format(self.firstname, self.lastname, self.chips)

    def get_amount_of_chips(self):
        total_amount = self.chips
        return total_amount

    def can_place_bet(self, amount):
        return amount <= self.chips

    def place_bet(self, amount):
        self.chips -= amount
        self.bet = amount

    def add_card_to_hand(self, card):
        self.hand.add_card(card)

    def get_hand_value(self):
        return self.hand.get_hand_value()

    def win_bet(self):
        self.chips += self.bet * 2

    def get_bet(self):
        return self.bet

    def empty_hand(self):
        self.hand.clear()
