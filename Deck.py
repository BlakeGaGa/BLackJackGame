
'''This is Deck class'''

from Card import Card
from random import randint

class Deck:
    def __init__(self):
        self.cards = Deck.allCards()

    def allCards() -> list:
        cards = []
        for suit in Card.allSuits():
            for rank in Card.allRanks():
                cards.append(Card(suit,rank))
        return cards

    def draw(self, isFaceUp=True) -> Card:
        card = self.cards.pop(randint(0,len(self.cards)-1)) # error handling here to prevent index out of range
        card.isFaceUp = isFaceUp
        return card

if __name__ == '__main__':
    PlayingDeck = Deck()
    PlayingCard = PlayingDeck.draw()
    rankValue = PlayingCard.rankValue()
    print( str(PlayingCard) + ' value is ' + str(rankValue))
    print("Deck class builds successfully.")
