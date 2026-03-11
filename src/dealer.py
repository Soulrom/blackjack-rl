from hand import Hand


class Dealer(Hand):
    def __init__(self):
        super().__init__()
        self.hidden_card = None

    def clear_hand(self):
        super().clear_hand()
        self.hidden_card = None

    def reveal(self):
        if self.hidden_card is not None:
            self.hand.append(self.hidden_card)

    def should_hit(self):
        return self.get_score() < 17

    def take_turn(self, deck, _player_score):
        while self.should_hit():
            self.add_card(deck.deal())
            print(f"Dealer draws: {[str(card) for card in self.hand]}")
