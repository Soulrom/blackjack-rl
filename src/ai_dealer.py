import random
import json
import ast

from dealer import Dealer


class AIDealer(Dealer):
    def __init__(self):
        super().__init__()
        self.q_table = {}
        self.alpha = 0.05
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 0.05
        self.epsilon_decay = 0.999997

    def get_state(self, player_score):
        has_ace = any(card.value == "A" for card in self.hand)
        return (self.get_score(), player_score, has_ace)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice([0, 1])
        if state in self.q_table:
            return max(self.q_table[state], key=self.q_table[state].get)
        return random.choice([0, 1])

    def update(self, state, action, reward, next_state):
        # if the state is not in the table, create {0: 0.0, 1: 0.0}
        if state not in self.q_table:
            self.q_table[state] = {0: 0.0, 1: 0.0}

        # maximum value of the next state
        if next_state in self.q_table:
            next_max = max(self.q_table[next_state].values())
        else:
            next_max = 0.0

        # update according to the formula
        current = self.q_table[state][action]
        self.q_table[state][action] = current + self.alpha * (
            reward + self.gamma * next_max - current
        )

    def take_turn(self, deck, player_score):
        while True:
            state = self.get_state(player_score)
            action = self.choose_action(state)
            if action == 0:
                break
            self.add_card(deck.deal())
            print(f"Dealer draws: {[str(card) for card in self.hand]}")
            if self.get_score() > 21:
                break

    def decay_epsilon(self):
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)

    def save(self, path):
        with open(path, "w") as f:
            json.dump({str(k): v for k, v in self.q_table.items()}, f)

    def load(self, path):
        with open(path, "r") as f:
            data = json.load(f)
            self.q_table = {
                ast.literal_eval(k): {int(a): q for a, q in v.items()}
                for k, v in data.items()
            }
        self.epsilon = 0.0
