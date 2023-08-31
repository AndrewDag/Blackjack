from card import Card
import random


class Deck:
    """
    Class representing a deck of cards
    """
    __slots__ = "deck"

    def __init__(self):
        """
        Initializes the deck with the 52 cards and associated values
        """
        self.deck = []
        for i in range(2, 15):
            if i == 14:  # ACE Condition
                card1 = Card(11, "C", "A")
                card2 = Card(11, "D", "A")
                card3 = Card(11, "H", "A")
                card4 = Card(11, "S", "A")
            elif i == 13:  # King Condition
                card1 = Card(10, "C", "K")
                card2 = Card(10, "D", "K")
                card3 = Card(10, "H", "K")
                card4 = Card(10, "S", "K")
            elif i == 12:  # Queen condition
                card1 = Card(10, "C", "Q")
                card2 = Card(10, "D", "Q")
                card3 = Card(10, "H", "Q")
                card4 = Card(10, "S", "Q")
            elif i == 11:  # Jack condition
                card1 = Card(10, "C", "J")
                card2 = Card(10, "D", "J")
                card3 = Card(10, "H", "J")
                card4 = Card(10, "S", "J")
            else:  # Number cards
                card1 = Card(i, "C", str(i))
                card2 = Card(i, "D", str(i))
                card3 = Card(i, "H", str(i))
                card4 = Card(i, "S", str(i))

            self.deck.append(card1)
            self.deck.append(card2)
            self.deck.append(card3)
            self.deck.append(card4)

    def __repr__(self):
        """
        Represents the deck in a string form
        :return: String representation of the deck
        """
        total = "["
        for i in range(len(self.deck)):
            total += str(self.deck[i]) + ", "
            if (i + 1) % 4 == 0:
                total += "\n"
        total = total[:-2]
        total += "]"

        return total

    def shuffle(self, flip: bool = False):
        """
        Shuffles the deck randomly
        :param flip: If "True", flips each card in the deck
        :return: None
        """
        if flip:
            for card in self.deck:
                card.flip()
        random.shuffle(self.deck)
        print("\nDeck shuffled!\n")

    def draw(self, flip: bool = False):
        """
        Draws a card from the deck
        :param flip: Draws the card flipped
        :return: Card drew from deck
        """
        if flip:
            return self.deck.pop().flip()
        return self.deck.pop()

    def add(self, card: Card):
        """
        Adds a card to the deck
        :param card: Card to be added
        :return: The deck
        """
        self.deck.append(card)
        return self

    def d_split_shuffle(self, flip: bool = False):
        if flip:
            for card in self.deck:
                card.flip()
        random.shuffle(self.deck)
        start_card = self.deck[0]
        for i in range(1, len(self.deck)):
            if self.deck[i] == start_card:
                self.deck.append(start_card)
                self.deck.append(self.deck[i])
                break
        print("\nSplit Scenario shuffle!\n")
