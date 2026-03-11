import os
import random
from deck import Deck
from player import Player
from ai_dealer import AIDealer


def train(episodes=2_000_000):
    ai = AIDealer()
    player = Player("AI_opponent", 0)

    for _ in range(episodes):
        if _ % 500_000 == 0:
            print(f"Episode {_:,} / {episodes:,}  ε={ai.epsilon:.4f}")

        deck = Deck()
        deck.shuffle()
        player.clear_hand()

        player.add_card(deck.deal())
        player.add_card(deck.deal())

        while player.get_score() < random.randint(15, 21):
            player.add_card(deck.deal())

        ai.clear_hand()
        ai.add_card(deck.deal())
        ai.hidden_card = deck.deal()
        ai.reveal()

        player_score = player.get_score()
        state = ai.get_state(player_score)

        while True:
            action = ai.choose_action(state)
            reward = 0

            if action == 1:  # hit
                ai.add_card(deck.deal())

            next_state = ai.get_state(player_score)
            dealer_score = ai.get_score()

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

    os.makedirs("../models", exist_ok=True)
    ai.save("../models/q_table.json")
    print(f"Training complete! States learned: {len(ai.q_table)}")


if __name__ == "__main__":
    train()
