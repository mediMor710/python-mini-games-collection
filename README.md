# 🎮 Python Mini-Games Collection

A collection of four Python games developed to practice programming fundamentals, randomization, game logic, graphical interfaces, and basic learning mechanisms.

This repository includes three terminal-based games and one graphical game built with **Pygame**. It also features a Rock Paper Scissors game in which the computer opponent uses a basic learning mechanism to adapt to previous interactions.

## ✨ Projects Included

### 🎲 1. Dice Rolling Game

**File:** `dice_rolling_game.py`

A terminal-based game that uses random dice outcomes to drive gameplay.

**Features:**
- Generate random dice results.
- Practice Python's randomization capabilities.
- Explore how random outcomes can influence game logic.

### 🔢 2. Guess the Number

**File:** `guess_the_number.py`

A number-guessing game in which the player attempts to find a randomly selected number within a specified range.

**How it works:**
1. The game selects a secret number.
2. The player enters a guess.
3. The program indicates whether the guess is too high or too low.
4. The player continues guessing until the correct number is found.

This game demonstrates conditional statements, loops, user input, and random number generation.

### 🎯 3. Hit the Targets

**File:** `hit_targets.py`

A graphical target-shooting game built with **Pygame**.

Unlike the other games, this project opens a game window, providing an interactive graphical experience.

**Features:**
- Graphical gameplay using Pygame.
- Target-based interaction.
- Opportunities to practice event handling, collision detection, and game-loop logic, depending on the implementation.

The objective and scoring mechanics depend on the rules implemented in the game.

### ✊ 4. Rock Paper Scissors — Learning Opponent

**File:** `rock_paper_Scissors.py`

A terminal-based implementation of the classic Rock Paper Scissors game, where the player competes against a computer opponent.

The project goes beyond a standard implementation by incorporating basic learning concepts to help the computer adapt to previous game interactions.

**Features:**
- Play against a computer opponent.
- Apply the traditional Rock Paper Scissors rules.
- Experiment with learning-rate parameters.
- Explore how previous interactions can influence future decisions.

**Learning mechanism:** The program uses a basic learning approach in which configurable learning-rate parameters influence how the opponent adapts based on previous steps.

This provides an introduction to adaptive behavior and machine-learning concepts. It should not be confused with a deep neural network unless the implementation actually uses one.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Random module | Generating random game outcomes |
| Pygame | Creating the graphical target-shooting game |
| Basic learning concepts | Experimenting with an adaptive computer opponent |

The Python `random` module is part of the standard library, so it does not need to be installed separately.

## 📁 Repository Structure

```text
python mini games collection/
│
├── dice_rolling_game.py
├── guess_the_number_game.py
├── hit_targets_game.py
├── rock_paper_scissors_game.py
├── requirements.txt
└── README.md
```

### File Overview

| File | Description | Interface |
|---|---|---|
| `dice_rolling_game.py` | Dice-based game using random outcomes | Terminal |
| `guess_the_number.py` | Number-guessing game | Terminal |
| `hit_targets.py` | Interactive target-shooting game | Graphical window |
| `rock_paper_Scissors.py` | Classic game with an adaptive computer opponent | Terminal |

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/mediMor710/python-mini-games-collection.git
cd python-mini-games-collection
```

### 2. Install Python

Make sure Python is installed on your computer.

Check your installation with:

```bash
python --version
```

### 3. Install Pygame

The first three terminal-based programs may run without external libraries if they use only Python's standard library.

To run the graphical game, install Pygame:

```bash
python -m pip install pygame
```

## 🚀 How to Run the Games

Run each game independently from the repository directory.

**Dice Rolling Game**

```bash
python dice_rolling_game.py
```

**Guess the Number**

```bash
python guess_the_number.py
```

**Hit the Targets**

```bash
python hit_targets.py
```

**Rock Paper Scissors**

```bash
python rock_paper_Scissors.py
```

For the graphical game, make sure your environment supports opening a Pygame window.

## 📚 Learning Objectives

This project collection provides practical experience with several Python concepts:

- **Variables and data types:** Representing game states and player choices.
- **Conditional statements:** Defining game rules and outcomes.
- **Loops:** Repeating gameplay until a stopping condition is reached.
- **User input:** Interacting with players through the terminal.
- **Randomization:** Generating unpredictable game outcomes.
- **Functions and modularity:** Organizing game logic into reusable parts, where implemented.
- **Event handling and graphics:** Building interactive gameplay with Pygame.
- **Adaptive behavior:** Experimenting with learning rates and an opponent that adjusts to previous interactions.

## 🔮 Possible Improvements

Future extensions could include:

- Add score tracking and replay options.
- Introduce difficulty levels to the guessing game.
- Add sound effects, animations, and a high-score system to Hit the Targets.
- Save game statistics between sessions.
- Improve the Rock Paper Scissors opponent with a clearly defined learning algorithm.
- Add automated tests and document the rules of each game.
- Create a common graphical menu to launch all four games.

## 👨‍💻 Author

**Your Name**

- GitHub: (https://github.com/mediMor710)
