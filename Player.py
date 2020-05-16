
'''This is player class, could be ethier player or dealer'''

from Deck import Deck
from Chip import Chip

BlackJackPoint = 21
AceMagicPoint = 11

class Player:
    def __init__(self):
        self.cards = [] # cards the player has
        self.aceCount = 0 # Ace card the player has
        self.points = 0 # total value of cards
        self.chips = Chip()

    def hit(self, card):
        self.cards.append(card)
        if card.isFaceUp:
            self.updatePoints(card)

    def allFaceUp(self) -> bool:
        hasNoFaceUp = False
        for card in self.cards:
            if not card.isFaceUp:
                self.updatePoints(card)
                hasNoFaceUp = True
            card.isFaceUp = True
        return hasNoFaceUp

    def updatePoints(self,card):
        if card.rankValue() == AceMagicPoint:
            self.aceCount += 1
        self.points += card.rankValue()
        if self.aceCount > 0 and self.points > BlackJackPoint:
            self.points -= (BlackJackPoint - AceMagicPoint)
            self.aceCount -= 1

    def takeBet(self):
        while True:
            try:
                self.chips.bet = int(input('How many chips would you like to bet? '))
            except ValueError:
                print('Sorry, a bet must be an integer!')
            else:
                if self.chips.bet > self.chips.total:
                    print("Sorry, your bet can't exceed", self.chips.total)
                else:
                    break

if __name__ == '__main__':
    PlayingDeck = Deck()
    BJPlayer = Player()
    BJPlayer.hit(PlayingDeck.draw(False))
    BJPlayer.hit(PlayingDeck.draw())
    BJPlayer.hit(PlayingDeck.draw())
    cardList = ''
    for card in BJPlayer.cards:
        cardList += str(card)
        cardList += ' '
    print(cardList)
    print('Total Points player has is ' + str(BJPlayer.points))
    BJPlayer.allFaceUp()
    cardList = ''
    for card in BJPlayer.cards:
        cardList += str(card)
        cardList += ' '
    print(cardList)
    print('After face up , total Points player has is ' + str(BJPlayer.points))
