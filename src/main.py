import sys

sys.stdout.reconfigure(encoding="utf-8")

from player import Player
from game import Game
from ui import print_banner


def main():
    print_banner()

    name = input("Enter your name: ").strip() or "Player"
    player = Player(name, 1000)

    while True:
        ai_choice = input("Do you want to play against AI Dealer? (y/n): ").strip().lower()
        if ai_choice == "y":
            game = Game(player, use_ai=True)
            break
        elif ai_choice == "n":
            game = Game(player)
            break
        else:
            print("Invalid input. Enter 'y' or 'n'.")

    while True:
        print(f"\nBalance: ${player.balance}")

        while True:
            try:
                bet = int(input("Place your bet: "))
                if bet <= 0:
                    print("Bet must be greater than 0.")
                elif bet > player.balance:
                    print(f"Not enough balance. Max bet: ${player.balance}")
                else:
                    break
            except ValueError:
                print("Invalid input. Enter a number.")

        player.place_bet(bet)

        game.start_round()
        if not game.check_blackjack():
            busted = game.player_turn()
            if not busted:
                game.dealer_turn()
                game.resolve()

        if player.balance <= 0:
            print("Game over! No balance left.")
            break

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()