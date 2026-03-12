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
![Status](https://img.shields.io/badge/Status-Actively%20Improved-blue?style=flat-square)

*A CLI Blackjack game with a standard dealer and an AI dealer powered by Q-learning.*

</div>

---

## About

**Playing With Cards** is a terminal-based Blackjack game where you play against a dealer of your choice. Place bets, manage your balance, and try to beat the house — all from your terminal.

Choose between a **standard dealer** that follows fixed rules, or an **AI dealer** trained via Q-learning across 5 million simulated games.

---

## Getting Started

### Prerequisites

- Python 3.11+

### Installation

```bash
git clone https://github.com/Soulrom/playing-with-cards.git
cd playing-with-cards/src
```

### Play

```bash
python main.py
```

> **Note:** The game must be run from the `src/` directory.

---

## AI Dealer

The AI dealer uses a Q-learning agent trained on 5 million episodes. Before selecting the AI dealer mode, run the training script once to generate the Q-table:

```bash
python train.py
```

Training takes a few minutes and saves the model to `models/q_table.json`.

### How it works

The agent learns a policy over states `(dealer_score, player_score, has_ace)`. At each step it chooses to **hit** or **stand** to maximise expected reward using the Bellman equation:

```
Q(s, a) ← Q(s, a) + α · (r + γ · max Q(s') − Q(s, a))
```

| Hyperparameter | Value | Role |
|----------------|-------|------|
| α (alpha) | 0.05 | Learning rate |
| γ (gamma) | 0.95 | Future reward discount |
| ε decay | 0.999999 | Exploration → exploitation over ~3M episodes |
| States learned | ~280 | Unique (dealer, player, ace) combinations |

---

## How to Play

1. Enter your name
2. Choose dealer mode: **standard** or **AI**
3. Place a bet (starting balance: $1,000)
4. On your turn, choose:
   - `h` — hit (take another card)
   - `s` — stand (end your turn)
5. Get closer to **21** than the dealer without going over

### Payouts

| Result | Payout |
|--------|--------|
| Win | `+bet` |
| Blackjack | `+bet × 1.5` |
| Lose | `−bet` |
| Draw | `bet returned` |

---

## License

Distributed under the MIT License. See [LICENSE](./LICENSE) for more information.

© 2026 Roman Mokrii
