from Player import Player
from Dealer import Dealer


def init_players(input_data_file):
    player_list = []
    with open(input_data_file, "r") as f:
        for line in f:
            field_list = line.strip().split(" ")
            firstname = field_list[0]
            lastname = field_list[1]
            age = int(field_list[2])
            nationality = field_list[3]
            chips = int(field_list[4])
            player_list.append(Player(firstname, lastname, age, nationality, chips))
    return player_list


def introduce_players(player_list):
    print('Players:')
    for p in player_list:
        print(p)


def request_to_play(player_list):
    active_player_list = []
    for player in player_list:
        answer = input(
            "Player {} {}, would you like to join the current game ? (Y/N): ".format(player.firstname, player.lastname))
        print(answer)
        if answer == "N":
            print("Player {} {}, will not  join the current game!".format(player.firstname, player.lastname))
        else:
            active_player_list.append(player)
    return active_player_list


def place_bets(player_list):
    for player in player_list:
        bet = int(input("Player {} {}, place your bet: ".format(player.firstname, player.lastname)))
        if player.can_place_bet(bet):
            print("Player {} {}, placed a bet of {}".format(player.firstname, player.lastname, bet))
        else:
            bet = int(input("Player {} {}, the bet of  {} exceeds your total amount, try with a lower value: "
                            .format(player.firstname, player.lastname, bet)))
            while not player.can_place_bet(bet):
                bet = int(input("Player {} {}, the bet of  {} exceeds your total amount, try with a lower value: "
                                .format(player.firstname, player.lastname, bet)))
        player.place_bet(bet)


def alocate_initial_cards(player_list, dealer):
    for player in player_list:
        for _ in range(0, 2):
            card = dealer.draw_a_card()
            player.add_card_to_hand(card)
            print("Player {} {}, you have a hand value of {}:".format(player.firstname, player.lastname,
                                                                      player.get_hand_value()))
    dealer.draw_self_card()
    print("Dealer, you have a hand value of {}:".format(dealer.get_hand_value()))


def hit(player, dealer):
    choice = input("Player {} {}, state your intention (S-stand/H-hit): ".format(player.firstname, player.lastname))
    hand_value = player.get_hand_value()
    if isinstance(hand_value, tuple):
        hand_value = min(hand_value)

    while choice != "S" and hand_value <= 21:
        card = dealer.draw_a_card()
        player.add_card_to_hand(card)

        hand_value = player.get_hand_value()
        if isinstance(hand_value, tuple):
            hand_value = min(hand_value)

        if hand_value > 21:
            print("Player {} {}, you have a hand value of {}. You lost your bet!".format(player.firstname,
                                                                                         player.lastname,
                                                                                         player.get_hand_value()))
            break

        print("Player {} {}, you have a hand value of {}:".format(player.firstname, player.lastname,
                                                                  player.get_hand_value()))
        choice = input("Player {} {}, state your intention (S-stand/H-hit): ".format(player.firstname, player.lastname))


def hit_players(player_list, dealer):
    for player in player_list:
        hit(player, dealer)


def play_dealer_hand(dealer):
    hand_value = dealer.get_hand_value()
    if isinstance(hand_value, tuple):
        hand_value = min(hand_value)
    while hand_value < 17:
        dealer.draw_self_card()
        hand_value = dealer.get_hand_value()
        if isinstance(hand_value, tuple):
            hand_value = min(hand_value)
        print("Dealer, you have a hand value of {}".format(dealer.get_hand_value()))


def pay_players(player_list):
    for player in player_list:
        player.win_bet()


def compute_round_results(player_list, dealer):
    dealer_hand_value = dealer.get_hand_value()
    if isinstance(dealer_hand_value, tuple):
        dealer_hand_value = min(dealer_hand_value)
    if dealer_hand_value > 21:
        print("Dealer has lost!")
        for player in player_list:
            player_hand_value = player.get_hand_value()
            if isinstance(player_hand_value, tuple):
                player_hand_value = min(player_hand_value)

            if player_hand_value <= 21:
                print("Player {} {}, your hand value is {}. You won the bet!".format(player.firstname, player.lastname,
                                                                                     player.get_hand_value()))
                player.win_bet()
            else:
                print("Player {} {}, your hand value is {}. You lost the bet!".format(player.firstname, player.lastname,
                                                                                      player.get_hand_value()))
        return

    for player in player_list:
        player_hand_value = player.get_hand_value()
        if isinstance(player_hand_value, tuple):
            player_hand_value = min(player_hand_value)

        if player_hand_value > 21:
            print("Player {} {}, your hand value is {}. You lost the bet!".format(player.firstname, player.lastname,
                                                                                  player.get_hand_value()))
            continue

        if player_hand_value > dealer_hand_value:
            print(
                "Player {} {}, you have a hand value of {} which is greater than the dealer's hand value of {}, you won {} chips".format(
                    player.firstname, player.lastname,
                    player.get_hand_value(), dealer.get_hand_value(), player.get_bet() * 2))
            player.win_bet()
        if player_hand_value <= dealer_hand_value:
            print(
                "Player {} {}, you have a hand value of {} which is lower or equal than the dealer's hand value of {}, you lost {} chips".format(
                    player.firstname, player.lastname,
                    player.get_hand_value(), dealer.get_hand_value(), player.get_bet()))


def reset_player_hands(player_list, dealer):
    for player in player_list:
        player.empty_hand()
    dealer.empty_hand()


def play_game(input_data_file):
    player_list = init_players(input_data_file)
    dealer = Dealer()
    dealer.shuffle_deck()
    introduce_players(player_list)
    print("Starting First Round")
    active_player_list = request_to_play(player_list)
    while active_player_list:
        place_bets(active_player_list)
        alocate_initial_cards(active_player_list, dealer)
        hit_players(active_player_list, dealer)
        play_dealer_hand(dealer)
        compute_round_results(active_player_list, dealer)
        # start next round
        print("Starting Next Round")
        reset_player_hands(player_list, dealer)
        dealer.reset_deck()
        active_player_list = request_to_play(player_list)
    print("Game has ended!")
    for player in player_list:
        print(player.get_final_results())


if __name__ == '__main__':
    INPUT_DATA_FILE = "ListaParticipanti.txt"
    play_game(INPUT_DATA_FILE)
