# Python Chess Game with Graphical User Interface

This project implements a simple chess game using Python and the Tkinter library for the graphical user interface.

The chess game provides a visual representation of a chess board and allows two players to take turns moving pieces according to basic chess rules. The game features a graphical board with clickable squares, piece movement validation, and turn-based gameplay.

## Repository Structure

The repository contains a single Python file:

- `chess_game.py`: The main script that implements the chess game logic and GUI.

## Usage Instructions

### Installation

1. Ensure you have Python 3.x installed on your system.
2. No additional libraries need to be installed as the game uses the built-in Tkinter library.

### Running the Game

To start the chess game, run the following command in your terminal:

```bash
python chess_game.py
```

### How to Play

1. The game starts with the white player's turn.
2. Click on a piece to select it. The selected piece's square will be highlighted in yellow.
3. Click on a destination square to move the selected piece.
4. If the move is valid, the piece will move to the new square, and the turn will switch to the other player.
5. If the move is invalid, the piece selection will be reset, and you can try again.
6. The current player's turn is displayed below the chess board.

### Game Rules

The game implements basic movement rules for each piece type:

- Pawns: Can move forward one square (or two on their first move) and capture diagonally.
- Rooks: Can move any number of squares horizontally or vertically.
- Knights: Move in an L-shape (two squares in one direction and one square perpendicular to that).
- Bishops: Can move any number of squares diagonally.
- Queens: Can move any number of squares horizontally, vertically, or diagonally.
- Kings: Can move one square in any direction.

Note that this implementation includes simplified rules and does not include advanced chess concepts like check, checkmate, castling, or en passant.

### Troubleshooting

If you encounter any issues running the game:

1. Ensure you're using Python 3.x.
2. Check that Tkinter is properly installed with your Python distribution.
3. If you see any error messages, verify that you're running the script from the correct directory.

## Data Flow

The chess game follows this basic data flow:

1. The game initializes the board state and creates the GUI.
2. Player clicks are captured by the button event handlers.
3. Click events are processed to select pieces and make moves.
4. The game logic validates moves and updates the board state.
5. The GUI is updated to reflect the new board state.
6. The turn switches to the other player.

```
[Player Input] -> [Event Handler] -> [Game Logic] -> [Board State] -> [GUI Update]
     ^                                                                    |
     |                                                                    |
     +--------------------------------------------------------------------+
```

This cycle repeats for each move until the game is finished.