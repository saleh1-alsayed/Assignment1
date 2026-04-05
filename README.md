# Assignment1
saleh Alsayed
....................

Features
Play Tic Tac Toe against an intelligent AI
AI uses Minimax + Alpha-Beta Pruning for optimal moves
Clean graphical interface using Pygame
Option to play as X or O
Detects:
Wins
Losses
Ties
Restart game functionality
🧠 How the AI Works

The AI evaluates all possible future game states and chooses the best move using:

Minimax Algorithm
Alpha-Beta Pruning (optimization to reduce computation)

Scoring system:

+1 → X wins
-1 → O wins
0 → Draw
📂 Project Structure
.
├── runner.py        # Main game loop and UI (Pygame)
├── tictactoe.py    # Game logic + Minimax AI
├── requirements.txt
├── OpenSans-Regular.ttf
🚀 Installation
Clone the repository:
git clone https://github.com/yourusername/tictactoe-ai.git
cd tictactoe-ai
Install dependencies:
pip install -r requirements.txt

Dependencies include:

pygame
▶️ Run the Game
python runner.py
🎯 How to Play
Choose whether to play as X or O
Click on a square to make your move
The AI will automatically respond
Game ends when:
A player wins
The board is full (tie)
