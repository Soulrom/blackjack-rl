import sys

sys.stdout.reconfigure(encoding="utf-8")

from player import Player
from game import Game
from ui import print_banner


def main():
    print_banner()
    name = input("Enter your name: ")
    player = Player(name, 1000)

    while True:
        print(f"\nBalance: ${player.balance}")

        while True:
            try:
                bet = int(input("Place your bet: "))
                if bet <= 0:
                    print("bet must be greater than 0.")
                elif bet > player.balance:
                    print(f"Not enough balance. Max bet: ${player.balance}")
                else:
                    break
            except ValueError:
                print("Invalid input. Enter a number.")

        player.place_bet(bet)

        game = Game(player)
        game.start_round()
        game.player_turn()
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
