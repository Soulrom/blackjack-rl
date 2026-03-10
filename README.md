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

*A CLI Blackjack game written in Python. Future plans include an AI dealer powered by reinforcement learning.*

</div>

---

## 📖 About

**Playing With Cards** is a terminal-based Blackjack game where you play against a dealer.
Place bets, manage your balance, and try to beat the house — all from your terminal.

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.11+

### Installation

```bash
git clone https://github.com/Soulrom/playing-with-cards.git
cd playing-with-cards
```

### Run

```bash
python main.py
```

---

## 🕹️ How to Play

1. Enter your name
2. Place a bet
3. Choose your action:
   - `hit` — take another card
   - `stand` — stop and let the dealer play
4. Try to get closer to **21** than the dealer without going over
5. Dealer draws cards until score ≥ 17

### Payouts

| Result | Payout |
|--------|--------|
| Win | +bet |
| Blackjack (21 from 2 cards) | +bet × 1.5 |
| Lose | −bet |
| Draw | bet returned |

---

## 📁 Project Structure

```
playing_with_cards/
├── main.py       # CLI interface & game loop
├── game.py       # Core game logic
├── deck.py       # Card and Deck classes
├── player.py     # Player class
└── dealer.py     # Dealer class
```

---

## 🛣️ Roadmap

- [x] Project setup
- [ ] Deck & Card classes
- [ ] Player logic
- [ ] Dealer logic
- [ ] Game loop
- [ ] CLI interface
- [ ] AI dealer via Reinforcement Learning

---

## 📄 License

Distributed under the MIT License. See [LICENSE](./LICENSE) for more information.

© 2026 Roman Mokrii
