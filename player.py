from card import Card
from time import sleep


class Player:
    """
    Class representing a player of blackjack
    """
    __slots__ = ["hand", "second_hand", "split"]

    def __init__(self):
        """
        Initializes a player
        """
        self.hand = []
        self.second_hand = []

        self.split = False

    def display_hand(self):
        """
        Displays the current hand(s) of the player
        :return: None
        """

        if self.split:
            print("\nHand 1: [", end='')

            if self.joker_status():
                for i in range(len(self.hand) - 2):
                    print(self.hand[i], end=' ')
                    print(",", end=' ')
                print(self.hand[-2], end='')
                print("]\n")
            else:
                for i in range(len(self.hand) - 1):
                    print(self.hand[i], end=' ')
                    print(",", end=' ')
                print(self.hand[-1], end='')
                print("]\n")
            # print("TOTAL HAND VAL =", self.total()[0])
            print("Hand 2: [", end='')
            for i in range(len(self.second_hand) - 1):
                print(self.second_hand[i], end=' ')
                print(",", end=' ')
            print(self.second_hand[-1], end='')
            print("]\n")
            # print("TOTAL HAND VAL =", self.total()[1])

        else:
            print("[", end='')
            for i in range(len(self.hand) - 1):
                print(self.hand[i], end=' ')
                print(",", end=' ')
            print(self.hand[-1], end='')
            print("]")
        # print("TOTAL HAND VAL =", self.total())

    def deal_initial(self, card1: Card, card2: Card):
        """
        Deals the initial two cards to a player, if split, then deals one card to the first hand and another to the
        second
        :param card1: First card
        :param card2: Second card
        :return: None
        """
        if self.split:
            self.hand.append(card1)
            self.second_hand.append(card2)
        else:
            self.hand.append(card1)
            self.hand.append(card2)

    def deal(self, card1: Card):
        """
        Deals one card to a player and adjusts a player's total value if an Ace would create a bust score based on
        whether the hand is split or if one of the first two cards dealt were aces
        :param card1: Card to deal
        :return: None
        """
        if self.joker_status() is False and self.split is False:  # Dealing to single hand
            if card1.is_ace() and self.total() + card1.value > 21:
                card1.value = 1
            elif self.total() + card1.value > 21:
                if self.hand[0].is_ace() and self.hand[0].value != 1:
                    self.hand[0].value = 1
                elif self.hand[1].is_ace() and self.hand[1].value != 1:
                    self.hand[1].value = 1
            self.hand.append(card1)
        elif self.split and self.joker_status() is False:    # If dealing to first hand in split scenario
            if card1.is_ace() and self.total()[0] + card1.value > 21:
                card1.value = 1
            elif self.total()[0] + card1.value > 21:
                if self.hand[0].is_ace() and self.hand[0].value != 1:
                    self.hand[0].value = 1
                elif self.hand[1].is_ace() and self.hand[1].value != 1:
                    self.hand[1].value = 1
            self.hand.append(card1)
        elif self.joker_status() and self.split:            # If dealing to second hand
            if card1.is_ace() and self.total()[1] + card1.value > 21:
                card1.value = 1
            elif self.total()[1] + card1.value > 21:
                if self.second_hand[0].is_ace() and self.second_hand[0].value != 1:
                    self.second_hand[0].value = 1
                elif self.second_hand[1].is_ace() and self.second_hand[1].value != 1:
                    self.second_hand[1].value = 1
            self.second_hand.append(card1)
        else:
            print("ERROR")

    def total(self):
        """
        Returns the total value of the player's hand
        :return: Int value of player's hand if not split or a list value with the player's first hand and the player's
        second hand if split
        """
        total = 0
        if self.split is False:
            for card in self.hand:
                total += card.value
            return total
        elif self.split:
            total2 = 0
            for card in self.hand:
                total += card.value
            for card in self.second_hand:
                total2 += card.value
            return [total, total2]

    def dealer_unflip(self):
        """
        Unflips the second dealer card
        :return: Dealer
        """
        if self.hand[1].flipped:
            self.hand[1].flip()
        return self

    def split_hand(self):
        """
        Checks if the two initial cards are equal and gives the player the option to split their hand into two different
        hands
        :return: None
        """
        if self.hand[0] == self.hand[1]:
            while True:
                c = input("Your initial cards are equal, would you like to split them? [Y] or [N] ").upper().strip()
                if c == 'Y' or c == "YES":
                    self.split = True
                    self.second_hand.append(self.hand.pop())
                    sleep(1)
                    return True
                elif c == 'N' or c == "NO":
                    print("")
                    if self.hand[0].is_ace() and self.hand[1].is_ace():
                        self.hand[1].value = 1
                    return False
                else:
                    print("\nERROR: Invalid input\n")

    def is_split(self):
        """
        Checks if the player has a split hand
        :return: True if split, false otherwise
        """
        if self.split:
            return True
        return False

    def joker(self):
        """
        Adds a "joker" card to the player's hand as a placeholder card to check if the first hand is done dealing cards
        in a split hand scenario
        :return: None
        """
        joker = Card(0, "X", "X")
        self.hand.append(joker)

    def joker_status(self):
        """
        Checks if the player's hand has a joker
        :return: True if joker, false otherwise
        """
        if self.hand[-1].is_joker():
            return True
        else:
            return False
