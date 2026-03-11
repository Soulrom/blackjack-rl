from deck import Deck
from player import Player
from ai_dealer import AIDealer


def train(episodes=10_000_000):
    ai = AIDealer()

    for _ in range(episodes):
        deck = Deck()
        deck.shuffle()
        player = Player("Roman", 1000)

        player.add_card(deck.deal())
        player.add_card(deck.deal())

        ai.clear_hand()
        ai.add_card(deck.deal())
        ai.hidden_card = deck.deal()

        state = ai.get_state(player.get_score())

        while True:
            action = ai.choose_action(state)
            reward = 0

            if action == 1:  # hit
                ai.add_card(deck.deal())

            next_state = ai.get_state(player.get_score())
            dealer_score = ai.get_score()
            player_score = player.get_score()

            if dealer_score > 21:
                reward = -1
                ai.update(state, action, reward, next_state)
                break
            elif action == 0:  # stand
                if dealer_score > player_score:
                    reward = 1
                elif dealer_score < player_score:
                    reward = -1
                else:
                    reward = 0
                ai.update(state, action, reward, next_state)
                break
            ai.update(state, action, reward, next_state)
            state = next_state
        ai.decay_epsilon()

    ai.save("../models/q_table.json")
    print(f"Training complete! States learned: {len(ai.q_table)}")


if __name__ == "__main__":
    train()
