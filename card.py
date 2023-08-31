from typing import TypeVar

Card = TypeVar('Card')


class Card:
    """
    Class representing a card in a deck of cards
    """
    __slots__ = ["value", "face", "suit", "flipped"]

    def __init__(self, value_in: int, suit_in: str, face_in: str):
        """
        Initializes a card
        :param value_in: Blackjack value of the card
        :param suit_in: Suit of the card
        :param face_in: Face of the card
        """
        self.value = value_in
        self.suit = suit_in
        self.face = face_in

        self.flipped = False

    def __eq__(self, other: Card):
        """
        Determines if one card is equal to another in value
        :param other: Other card to compare to
        :return: True if equal, False otherwise
        """
        if self.value == other.value and self.face == other.face:
            return True
        return False

    def __repr__(self):
        """
        Represents a card in string form
        :return: If flipped, returns a censored version of the card, otherwise it will return the face of the card next
        to the suit of the card represented by a unicode character
        """
        if self.flipped:
            return "--"
        display_suit = None
        if self.suit == "H":
            display_suit = "♥"
        elif self.suit == "C":
            display_suit = "♣"
        elif self.suit == "D":
            display_suit = "♦"
        elif self.suit == "S":
            display_suit = "♠"
        elif self.suit == "J":
            return ""
        return self.face + display_suit

    __str__ = __repr__

    def flip(self):
        """
        Flips a card, which censors the face and suit
        :return: The card
        """
        if self.flipped:
            self.flipped = False
        else:
            self.flipped = True
        return self

    def is_ace(self):
        """
        Determines if a given card is an ace
        :return: True if an Ace, False otherwise
        """
        if self.face == 'A':
            return True
        return False

    def is_joker(self):
        """
        Determines if a given card is a joker
        :return: True if joker, False otherwise
        """
        if self.face == 'X':
            return True
        return False
