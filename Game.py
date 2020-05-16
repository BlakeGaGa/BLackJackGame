
from Player import Player
from Deck import Deck
from Card import Card

BlackJackPoint = 21
DealerReachPoint = 17

class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Player()
        self.dealer.hit(self.deck.draw(False))
        self.dealer.hit(self.deck.draw())
        self.player = Player()
        self.player.hit(self.deck.draw())
        self.player.hit(self.deck.draw())
        self.player.takeBet()

    def updateStatus(self):
        print('Dealer\'s Hand:')
        for card in self.dealer.cards:
            print(card)
        print('Dealer\'s Hand = ' + str(self.dealer.points))
        print('Player\'s Hand:')
        for card in self.player.cards:
            print(card)
        print('Player\'s Hand = ' + str(self.player.points))

    def playerHit(self):
        self.player.hit(self.deck.draw())

    def playerPoints(self) -> int:
        return self.player.points

    def dealerHit(self):
        self.dealer.hit(self.deck.draw())

    def dealerPoints(self) -> int:
        return self.dealer.points


if __name__ == '__main__':

    # initialize
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n Dealer hits until she reaches 17. Aces count as 1 or 11.\n')
    BlackJackGame = Game()
    BlackJackGame.updateStatus()

    # game starts
    while BlackJackGame.playerPoints() < BlackJackPoint and BlackJackGame.dealerPoints() < BlackJackPoint:
        action = input('Would you like to Hit or Stand? Enter \'h\' or \'s\' ').lower()
        if action == 'h':
            BlackJackGame.playerHit()
            BlackJackGame.updateStatus()
        elif action == 's':
            BlackJackGame.dealer.allFaceUp()
            print('Player stands. Dealer is playing.')
            BlackJackGame.updateStatus()
            while BlackJackGame.dealerPoints() < DealerReachPoint:
                BlackJackGame.dealerHit()
                BlackJackGame.updateStatus()
            break

    # game over
    if BlackJackGame.dealer.allFaceUp():
        BlackJackGame.updateStatus()
    if BlackJackGame.playerPoints() > BlackJackPoint:
        print('Player busts!')
        print('Dealer wins!')
        BlackJackGame.player.chips.lose_Bet()
    elif BlackJackGame.dealerPoints() > BlackJackPoint:
        print('Dealer busts!')
        print('Player wins!')
        BlackJackGame.player.chips.win_Bet()
    elif BlackJackGame.playerPoints() < BlackJackGame.dealerPoints():
        print('Dealer wins!')
        BlackJackGame.player.chips.lose_Bet()
    elif BlackJackGame.playerPoints() > BlackJackGame.dealerPoints():
        print('Player wins!')
        BlackJackGame.player.chips.win_Bet()
    else:
        print('No winner!')
    print('Player\'s winnings stand at ' + str(BlackJackGame.player.chips.total))




