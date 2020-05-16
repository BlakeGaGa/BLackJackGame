
'''This is chip class'''

class Chip:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def lose_Bet(self):
        self.total -= self.bet

    def win_Bet(self):
        self.total += self.bet

