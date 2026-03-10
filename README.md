# 🃏 Playing With Cards

> A CLI Blackjack game written in Python. Future plans include an AI dealer powered by reinforcement learning.

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=flat-square)

---

## 🎮 About

**Playing With Cards** is a terminal-based Blackjack game where you play against a dealer. Place bets, manage your balance, and try to beat the house — all from your terminal.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+

### Run the game
```bash
git clone https://github.com/your-username/playing-with-cards.git
cd playing-with-cards
python main.py
```

---

## 🕹️ How to Play

1. Enter your name
2. Place a bet
3. Choose `hit` (take a card) or `stand` (stop)
4. Try to get closer to **21** than the dealer without going over
5. Dealer draws until score ≥ 17

### Payouts
| Result | Payout |
|--------|--------|
| Win | x1 |
| Blackjack (21 from 2 cards) | x1.5 |
| Lose | -bet |
| Draw | bet returned |

---

## 📁 Project Structure

```
playing_with_cards/
├── main.py       # CLI interface
├── game.py       # Game logic
├── deck.py       # Card and Deck classes
├── player.py     # Player class
└── dealer.py     # Dealer class
```

---

## 🛣️ Roadmap

- [x] Project structure
- [ ] Deck and Card classes
- [ ] Player logic
- [ ] Dealer logic
- [ ] Game loop
- [ ] CLI interface
- [ ] AI dealer powered by Reinforcement Learning

---

## 📄 License

MIT © Soulrom
