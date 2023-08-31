from deck import Deck
from player import Player
from time import sleep
from data_boss import DataBoss


def dealer_unflip_display(dealer: Player):
    """
    Utility function that unflips the dealer's hand and prints it
    :param dealer: Current dealer
    :return: None
    """
    sleep(1)
    dealer.dealer_unflip()
    print("Dealer Hand: ", end='')
    dealer.display_hand()
    print("")
    sleep(1)
    return


def determine_initial_split_results(player: Player, dealer: Player, first_results: bool):
    """
    Determines results for if the player has a split hand
    :param player: Current player
    :param dealer: Current dealer
    :param first_results: If True, does not check for if the hands are equal, if False, does check
    :return: Returns a list the contains the results. First item: 0 if the dealer wins, 1 if the player wins, 2 if it
    is a push, 10 otherwise. Second item: Numbered specific scenarios for data collection
    """
    dealer_total = dealer.total()
    player_total = player.total()

    if player_total[0] == 21 and dealer_total == 21 or player_total[1] == 21 and dealer_total == 21:
        dealer_unflip_display(dealer)
        print("Both the dealer and the player (in at least one of the split hands) have blackjack, it's a push!")
        return [2, 13]
    elif dealer_total == 21:
        dealer_unflip_display(dealer)
        print("Dealer has blackjack. You lose.")
        return [0, 1]
    elif player_total[0] == 21:
        dealer_unflip_display(dealer)
        print("Player has blackjack in hand 1. You win!")
        return [1, 15]
    elif player_total[1] == 21:
        dealer_unflip_display(dealer)
        print("Player has blackjack in hand 2. You win!")
        return [1, 16]
    elif player_total[0] == dealer_total and player_total[1] == dealer_total and first_results is False:
        dealer_unflip_display(dealer)
        print("Both hands of the player are equal to the dealer's hand. It's a push")
        return [2, 9]
    elif player_total[0] > 21 and player_total[1] > 21:
        dealer_unflip_display(dealer)
        print("You're bust in both hands. You lose.")
        return [0, 18]
    elif player_total[0] > 21:
        if player.joker_status() is False:
            player.joker()
            print("You're bust in the first hand")
            sleep(2)
            print("\nYour Hands:")
        else:
            sleep(1)
            print("Your Hands:")
        player.display_hand()
        return [10, None]
    elif player_total[1] > 21:
        dealer_unflip_display(dealer)
        print("You're bust in the second hand")
        sleep(1)
        player.display_hand()
        return [3, None]
    else:
        return [10, None]


def determine_initial_results(player: Player, dealer: Player, first_results: bool = False):
    """
    Determines the result of the game before the dealer starts drawing cards
    :param player: Current player
    :param dealer: Current dealer
    :param first_results: If True, does not check for if the hands are equal, if False, does check
    :return: Returns a list the contains the results. First item: 0 if the dealer wins, 1 if the player wins, 2 if it
    is a push, 10 otherwise. Second item: Numbered specific scenarios for data collection
    """
    if player.is_split():
        return determine_initial_split_results(player, dealer, first_results)
    else:
        if dealer.total() == player.total() and player.total() == 21:
            dealer_unflip_display(dealer)
            print("Both the dealer and the player have blackjack, it's a push!")
            return [2, 10]
        elif dealer.total() == 21:
            dealer_unflip_display(dealer)
            print("Dealer has blackjack. You lose.")
            return [0, 1]
        elif player.total() == 21:
            dealer_unflip_display(dealer)
            print("You have blackjack! You win!")
            return [1, 11]
        elif player.total() == dealer.total() and first_results is False:
            dealer_unflip_display(dealer)
            print("The player and the dealer are equal. It's a push.")
            return [2, 3]
        elif player.total() > 21:
            sleep(1)
            print("You're bust! You lose.")
            return [0, 12]
        else:
            return [10, None]


def determine_results_dealer_draw_split(player: Player, dealer: Player, deck: Deck):
    """
    Determines the results of the current game and allows the dealer to continuously draw cards in a scenario where
    the player's hand is split
    :param player: Current player
    :param dealer: Current dealer
    :param deck: Current deck
    :return: Returns a list the contains the results. First item: 0 if the dealer wins, 1 if the player wins, 2 if it
    is a push, 10 otherwise. Second item: Numbered specific scenarios for data collection
    """
    while True:
        if dealer.total() > 21:
            sleep(1)
            print("Dealer is bust. You win!")
            return [1, 0]
        elif dealer.total() == 21:
            sleep(1)
            print("Dealer has blackjack. You lose.")
            return [0, 1]
        elif dealer.total() > player.total()[0] and player.total()[1] > 21:
            sleep(1)
            print("Dealer has a higher hand value than player's first hand. You lose.")
            return [0, 4]
        elif dealer.total() > player.total()[1] and player.total()[0] > 21:
            sleep(1)
            print("Dealer has a higher hand value than player's second hand. You lose.")
            return [0, 5]
        elif dealer.total() > player.total()[0] and dealer.total() > player.total()[1]:
            sleep(1)
            print("Dealer has a higher hand value than both hands. You lose.")
            return [0, 6]
        elif dealer.total() == player.total()[0] and (player.total()[0] > player.total()[1] or player.total()[1] > 21):
            sleep(1)
            print("The dealer is equal to the player's first hand. It's a push.")
            return [2, 7]
        elif dealer.total() == player.total()[1] and (player.total()[1] > player.total()[0] or player.total()[0] > 21):
            sleep(1)
            print("The dealer is equal to the player's second hand. It's a push.")
            return [2, 8]
        elif dealer.total() == player.total()[1] and player.total()[1] == player.total()[0]:
            sleep(1)
            print("Both hands of the player are equal to the dealer's hand. It's a push")
            return [2, 9]

        dealer.dealer_unflip()
        sleep(1)
        dealer.deal(deck.draw())
        print("Dealer Draw: ", end='')
        dealer.display_hand()
        print("")


def determine_results_dealer_draw(player: Player, dealer: Player, deck: Deck):
    """
    Determines the results of the current game and allows the dealer to continuously draw cards
    :param player: Current player
    :param dealer: Current dealer
    :param deck: Current deck
    :return: 0 if the dealer won, 1 if the player won, and 2 if there was a tie
    """
    dealer.dealer_unflip()
    print("Dealer Hand: ", end='')
    dealer.display_hand()
    print("")

    if player.is_split():
        return determine_results_dealer_draw_split(player, dealer, deck)

    while dealer.total() < 21 and dealer.total() < player.total():
        sleep(1)
        dealer.deal(deck.draw())
        print("Dealer Draw: ", end='')
        dealer.display_hand()
        print("")

    sleep(1)
    if dealer.total() > 21:
        print("Dealer is bust. You win!")
        return [1, 0]
    elif dealer.total() == 21:
        print("Dealer has blackjack. You lose.")
        return [0, 1]
    elif dealer.total() > player.total():
        print("Dealer has a higher hand value. You lose.")
        return [0, 2]
    elif dealer.total() == player.total():
        print("The player and the dealer are equal. It's a push.")
        return [2, 3]
    else:
        print("Unknown error")


def hit(player: Player, dealer: Player, deck: Deck):
    """
    Deals a card to the player and displays the dealer's and player's cards
    :param player: Current player
    :param dealer: Current dealer
    :param deck: Current deck
    :return: None
    """
    player.deal(deck.draw())
    print("Dealer Hand:", end=' ')
    dealer.display_hand()
    sleep(1)
    if player.is_split():
        print("\nYour Hands:")
        player.display_hand()
    else:
        print("Your Hand:", end=' ')
        player.display_hand()
        print("")


def next_move():
    """
    Allows the player to select their next move after initial cards are dealt
    :return: None
    """
    move = None
    while move != 'H' or move != 'S' or move != "HIT" or move != "STAY":
        move = input("Would you like to hit [H] or stay [S]? ").upper().strip()
        print("")
        if move == 'S' or move == "STAY":
            return False
        elif move == 'H' or move == "HIT":
            return True
        else:
            print("ERROR: Invalid input\n")


def initial(deck: Deck):
    """
    Initial game start function that shuffles the deck and deals cards to the dealer and player
    :param deck: Deck being used in play
    :return: 0 if the dealer won, 1 if the player won, and 2 if there was a tie
    """
    deck.shuffle()
    player = Player()
    dealer = Player()

    player.deal_initial(deck.draw(), deck.draw())
    dealer.deal_initial(deck.draw(), deck.draw(True))

    print("Dealer Hand:", end=' ')
    dealer.display_hand()
    print("Your Hand:", end=' ')
    player.display_hand()
    print("")

    split = player.split_hand()                     # Determining if player can split hand
    if split:
        player.deal_initial(deck.draw(), deck.draw())
        player.display_hand()

    results = determine_initial_results(player, dealer, True)
    if results[0] != 10:
        return results

    while True:
        if player.joker_status() is False and player.is_split():    # On hand 1
            print("Deciding Hand 1...\n")
        elif player.joker_status() and player.is_split():           # On hand 2
            print("Deciding Hand 2...\n")
        cont = next_move()
        if cont is False:  # If the player stayed

            if player.joker_status() is False and player.is_split():    # Skips determining results if  on hand 1
                print("Dealer Hand:", end=' ')
                dealer.display_hand()
                sleep(1)
                print("\nYour Hands:")
                player.display_hand()
                player.joker()
                continue

            results = determine_initial_results(player, dealer)
            if results[0] != 10:
                return results

            break

        hit(player, dealer, deck)

        results = determine_initial_results(player, dealer, True)
        if results[0] == 3:
            break
        elif results[0] != 10:
            return results

    return determine_results_dealer_draw(player, dealer, deck)


def start_game(current_score):
    """
    Gets input for if the player wants to continue playing or see the data, adjusts the current score, and logs data
    :param current_score: Current score of the game
    :return: True if continuing play, False otherwise
    """
    data = DataBoss()
    while True:
        c = input("Play Blackjack? ([Y] or [N]) Or See All Data ([D]) ").upper().strip()
        if c == 'Y' or c == "YES":
            deck = Deck()
            result = initial(deck)
            current_score[result[0]] += 1
            data.write_result(result)
            return True
        elif c == 'N' or c == "NO":
            return False
        elif c == 'D' or c == "DATA":
            data.print_file()
        else:
            print("\nERROR: Invalid input\n")


def main():
    """
    Main function of the game that handles continuous blackjack play and prints the score
    :return: None
    """
    current_score = [0, 0, 0]
    cont = True
    while cont is True:
        cont = start_game(current_score)

        sleep(1)
        print("\nSCORE:", end=' ')
        print("Dealer:", str(current_score[0]) + ", Player:", str(current_score[1]) + ", Pushes:", current_score[2],
              "\n")
        sleep(1)

    print("Game is ended")


if __name__ == '__main__':
    main()
#
