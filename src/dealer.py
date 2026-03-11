class Dealer:
    def __init__(self):
        self.hand = []
        self.hidden_card = None

    def add_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def get_score(self):
        score = 0
        aces = 0

        for card in self.hand:
            score += card.get_numeric_value()
            if card.value == "A":
                aces += 1

        while score > 21 and aces > 0:
            score -= 10
            aces -= 1

        return score

    def reveal(self):
        if self.hidden_card is not None:
            self.hand.append(self.hidden_card)

    def should_hit(self):
        return self.get_score() < 17
