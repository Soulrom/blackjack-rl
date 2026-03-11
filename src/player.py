from hand import Hand


class Player(Hand):
    def __init__(self, name, balance):
        super().__init__()
        self.name = name
        self.balance = balance
        self.bet = 0

    def place_bet(self, amount):
        self.bet = amount
        self.balance -= amount

    def win(self, multiplier):
        self.balance += self.bet + self.bet * multiplier
