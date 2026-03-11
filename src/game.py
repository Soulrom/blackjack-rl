from deck import Deck
from dealer import Dealer


class Game:
    def __init__(self, player):
        self.player = player
        self.deck = Deck()
        self.dealer = Dealer()

    def start_round(self):
        self.deck.shuffle()
        self.player.clear_hand()
        self.dealer.clear_hand()
        self.player.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.dealer.hidden_card = self.deck.deal()

    def player_turn(self):
        while True:
            print(f"Your hand: {[str(card) for card in self.player.hand]}")
            print(f"Score: {self.player.get_score()}")
            print(f"Dealer shows: {str(self.dealer.hand[0])}")

            action = input("Hit or Stand? (h/s): ").lower()

            if action == "h":
                self.player.add_card(self.deck.deal())
                if self.player.get_score() > 21:
                    print("Bust! You Lose.")
                    print(f"Score: {self.player.get_score()}")
                    break
            elif action == "s":
                break

    def dealer_turn(self):
        self.dealer.reveal()
        print(f"Dealer hand: {[str(card) for card in self.dealer.hand]}")

        while self.dealer.should_hit():
            self.dealer.add_card(self.deck.deal())
            print(f"Dealer draws: {[str(card) for card in self.dealer.hand]}")

    def resolve(self):
        player_score = self.player.get_score()
        dealer_score = self.dealer.get_score()

        if player_score > 21:
            print("You lose!")
        elif dealer_score > 21:
            print("You win!")
            self.player.win(1)
        elif player_score == 21 and len(self.player.hand) == 2:
            print("Blackjack! You win x1.5!")
            self.player.win(1.5)
        elif player_score > dealer_score:
            print("You win!")
            self.player.win(1)
        elif player_score < dealer_score:
            print("You lose!")
        else:
            print("Draw!")
            self.player.win(1)
