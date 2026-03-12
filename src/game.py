from deck import Deck
from dealer import Dealer
from ai_dealer import AIDealer


class Game:
    def __init__(self, player, use_ai=False):
        self.player = player
        self.deck = Deck()

        if use_ai:
            self.dealer = AIDealer()
            try:
                self.dealer.load("../models/q_table.json")
            except FileNotFoundError:
                print("Warning: q_table.json not found. Run train.py first!")
        else:
            self.dealer = Dealer()

    def start_round(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player.clear_hand()
        self.dealer.clear_hand()
        self.player.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.dealer.hidden_card = self.deck.deal()

    def check_blackjack(self) -> bool:
        player_blackjack = self.player.get_score() == 21 and len(self.player.hand) == 2

        # Peek at dealer's full two-card score without permanently revealing
        hidden = self.dealer.hidden_card
        if hidden:
            self.dealer.hand.append(hidden)
        dealer_blackjack = self.dealer.get_score() == 21 and len(self.dealer.hand) == 2
        if hidden:
            self.dealer.hand.pop()

        if player_blackjack and dealer_blackjack:
            self.dealer.reveal()
            print("Both have Blackjack! Draw!")
            self.player.win(0)
            return True
        elif player_blackjack:
            self.dealer.reveal()
            print("Blackjack! You win x1.5!")
            self.player.win(1.5)
            return True
        elif dealer_blackjack:
            self.dealer.reveal()
            print("Dealer has Blackjack! You lose!")
            return True
        return False

    def player_turn(self) -> bool:
        while True:
            print(f"Your hand: {[str(card) for card in self.player.hand]}")
            print(f"Score: {self.player.get_score()}")
            print(f"Dealer shows: {str(self.dealer.hand[0])}")

            action = input("Hit or Stand? (h/s): ").strip().lower()

            if action == "h":
                self.player.add_card(self.deck.deal())
                if self.player.get_score() > 21:
                    print(f"Bust! Score: {self.player.get_score()}")
                    return True
            elif action == "s":
                return False
            else:
                print("Invalid input. Enter 'h' or 's'.")

    def dealer_turn(self):
        self.dealer.reveal()
        print(f"Dealer hand: {[str(card) for card in self.dealer.hand]}")

        self.dealer.take_turn(self.deck, self.player.get_score())

    def resolve(self):
        player_score = self.player.get_score()
        dealer_score = self.dealer.get_score()

        if player_score > 21:
            print("You lose!")
        elif dealer_score > 21:
            print("You win!")
            self.player.win(1)
        elif player_score > dealer_score:
            print("You win!")
            self.player.win(1)
        elif player_score < dealer_score:
            print("You lose!")
        else:
            print("Draw!")
            self.player.win(0)
