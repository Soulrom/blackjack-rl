```
██████╗ ██╗      █████╗ ██╗   ██╗██╗███╗   ██╗ ██████╗
██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██║████╗  ██║██╔════╝
██████╔╝██║     ███████║ ╚████╔╝ ██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██║██║╚██╗██║██║   ██║
██║     ███████╗██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝
╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝

        ██╗    ██╗██╗████████╗██╗  ██╗     ██████╗ █████╗ ██████╗ ██████╗ ███████╗
        ██║    ██║██║╚══██╔══╝██║  ██║    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
        ██║ █╗ ██║██║   ██║   ███████║    ██║     ███████║██████╔╝██║  ██║███████╗
        ██║███╗██║██║   ██║   ██╔══██║    ██║     ██╔══██║██╔══██╗██║  ██║╚════██║
        ╚███╔███╔╝██║   ██║   ██║  ██║    ╚██████╗██║  ██║██║  ██║██████╔╝███████║
         ╚══╝╚══╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝
```

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=flat-square)

*A CLI Blackjack game with a Q-learning AI dealer, written in Python.*

</div>

---

## About

**Playing With Cards** is a terminal-based Blackjack game where you play against an AI dealer trained using reinforcement learning. Place bets, manage your balance, and try to beat an opponent that learns from experience — all from your terminal.

---

## Getting Started

### Prerequisites

- Python 3.11+

### Installation

```bash
git clone https://github.com/Soulrom/playing-with-cards.git
cd playing-with-cards
```

### Train the AI dealer

The AI dealer requires a trained Q-table before playing. Run the training script once:

```bash
cd src
python train.py
```

Training runs 2 million episodes and saves the Q-table to `models/q_table.json`.

### Play

```bash
python main.py
```

---

## How to Play

1. Enter your name
2. Place a bet
3. On your turn, choose:
   - `h` — hit (take another card)
   - `s` — stand (end your turn)
4. Get closer to **21** than the dealer without going over
5. The AI dealer plays automatically based on its trained strategy

### Payouts

| Result | Payout |
|--------|--------|
| Win | `+bet` |
| Blackjack | `+bet × 1.5` |
| Lose | `−bet` |
| Draw | `bet returned` |

---

## Dealer Modes

The game supports two dealer modes, configurable in `main.py`:

```python
# AI dealer — uses trained Q-table
game = Game(player, use_ai=True)

# Classic dealer — hits until score ≥ 17
game = Game(player)
```

---

## AI Dealer

The dealer is powered by **Q-learning** — a model-free reinforcement learning algorithm. During training, the agent plays millions of games and learns which actions (hit or stand) maximize its long-term reward.

| Parameter | Value |
|-----------|-------|
| Algorithm | Q-learning |
| Episodes | 2,000,000 |
| State space | `(dealer_score, player_score, has_ace)` |
| Actions | `hit` / `stand` |
| Exploration | ε-greedy (`ε` from `1.0` → `0.05`) |

---

## License

Distributed under the MIT License. See [LICENSE](./LICENSE) for more information.

© 2026 Roman Mokrii
