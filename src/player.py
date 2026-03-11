class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = []
        self.bet = 0
    
    def add_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []
    
    def get_score(self):
        score = 0
        aces = 0

        for card in self.hand:
            score += card.get_numeric_value()
            if card.value == 'A':
                aces += 1
        
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
        
        return score
    
    def place_bet(self, amount):
        self.bet += amount
        self.balance -= amount
    
    def win(self, multiplier):
        self.balance += self.bet * multiplier