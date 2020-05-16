
'''This is card class, with 4 kinds of suits * 13 kinds of ranks (total 52 cards)'''

from enum import Enum
from typing import List

class Suit(Enum):
    SPADE = 'Spade'
    CLUB = 'Club'
    HEART = 'Heart'
    DIAMOND = 'Diamond'

class Card:
    __rankValueDict = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6
                    , '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
    def __init__(self, suit: Suit, rank: int):
        self.__suit = suit
        self.__rank = rank
        self.isFaceUp = True

    def __str__(self):
        if not self.isFaceUp:
            return '<card hidden>'
        else:
            return (self.__suit.name + ' ' + str(self.__rank))

    @classmethod
    def allSuits(cls) -> list:
        return [Suit.SPADE, Suit.CLUB, Suit.HEART, Suit.DIAMOND]

    @classmethod
    def allRanks(cls) -> list:
        return ['A'] + [str(i) for i in range(2,11)] + ['J', 'Q', 'K']

    def rankValue(self) -> int:
        if self.__rank in Card.__rankValueDict:
            return Card.__rankValueDict[self.__rank]
        else:
            return 0




