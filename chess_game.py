import tkinter as tk
from tkinter import messagebox

class ChessGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chess Game")
        
        # Colors for the chess board
        self.colors = ["white", "gray"]
        
        # Initialize the board state
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        
        # Game state variables
        self.selected_piece = None
        # Who starts first; can be white or black
        self.current_player = "white"
        
        # Create the chess board
        self.buttons = [[None for _ in range(8)] for _ in range(8)]
        self.create_board()
        
        # Status label
        self.status_label = tk.Label(self.window, text=f"{self.current_player}'s turn")
        self.status_label.pack()
        
    def create_board(self):
        board_frame = tk.Frame(self.window)
        board_frame.pack()
        
        for row in range(8):
            for col in range(8):
                color = self.colors[(row + col) % 2]
                button = tk.Button(board_frame, width=5, height=2, bg=color)
                button.grid(row=row, column=col)
                button.config(command=lambda r=row, c=col: self.button_click(r, c))
                self.buttons[row][col] = button
                
                # Set initial piece text
                piece = self.board[row][col]
                if piece:
                    self.update_button_text(row, col)
    
    def update_button_text(self, row, col):
        piece = self.board[row][col]
        piece_symbols = {
            'wK': '♔', 'wQ': '♕', 'wR': '♖', 'wB': '♗', 'wN': '♘', 'wP': '♙',
            'bK': '♚', 'bQ': '♛', 'bR': '♜', 'bB': '♝', 'bN': '♞', 'bP': '♟'
        }
        text = piece_symbols.get(piece, '')
        self.buttons[row][col].config(text=text)
    
    def button_click(self, row, col):
        piece = self.board[row][col]
        
        # First click - select piece
        if self.selected_piece is None:
            if piece and piece[0] == ('w' if self.current_player == 'white' else 'b'):
                self.selected_piece = (row, col)
                self.buttons[row][col].config(bg='yellow')
            return
        
        # Second click - move piece
        if self.selected_piece:
            old_row, old_col = self.selected_piece
            
            # Reset the color of the previously selected square
            self.buttons[old_row][old_col].config(bg=self.colors[(old_row + old_col) % 2])
            
            # If valid move, update the board
            if self.is_valid_move(old_row, old_col, row, col):
                self.board[row][col] = self.board[old_row][old_col]
                self.board[old_row][old_col] = ""
                self.update_button_text(row, col)
                self.update_button_text(old_row, old_col)
                
                # Check for game end conditions
                if self.is_checkmate():
                    winner = "White" if self.current_player == "black" else "Black"
                    messagebox.showinfo("Game Over", f"Checkmate! {winner} wins!")
                    self.window.quit()
                elif self.is_stalemate():
                    messagebox.showinfo("Game Over", "Stalemate! The game is a draw!")
                    self.window.quit()
                else:
                    # Switch players
                    self.current_player = "black" if self.current_player == "white" else "white"
                    self.status_label.config(text=f"{self.current_player}'s turn")
            
            self.selected_piece = None
    
    def is_valid_move(self, from_row, from_col, to_row, to_col):
        piece = self.board[from_row][from_col]
        target = self.board[to_row][to_col]
        
        # Basic validation - Prevent Illegal Move
        if target and target[0] == piece[0]:  # Can't capture own pieces
            return False
        
        # Prevent king capture - the game should end via checkmate instead
        if target and target[1] == 'K':
            return False
            
        piece_type = piece[1]
        
        # Pawn movement
        if piece_type == 'P':
            direction = -1 if piece[0] == 'w' else 1
            if from_col == to_col and not target:  # Regular move
                if to_row == from_row + direction:
                    return True
                if (from_row == 1 and piece[0] == 'b') or (from_row == 6 and piece[0] == 'w'):
                    if to_row == from_row + 2 * direction and not self.board[from_row + direction][from_col]:
                        return True
            # Capture
            if abs(to_col - from_col) == 1 and to_row == from_row + direction:
                if target:
                    return True
        
        # Other pieces have simplified movement rules for this basic implementation
        elif piece_type == 'R':  # Rook
            return from_row == to_row or from_col == to_col
        elif piece_type == 'N':  # Knight
            row_diff = abs(to_row - from_row)
            col_diff = abs(to_col - from_col)
            return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)
        elif piece_type == 'B':  # Bishop
            return abs(to_row - from_row) == abs(to_col - from_col)
        elif piece_type == 'Q':  # Queen
            return (from_row == to_row or from_col == to_col or 
                   abs(to_row - from_row) == abs(to_col - from_col))
        elif piece_type == 'K':  # King
            return abs(to_row - from_row) <= 1 and abs(to_col - from_col) <= 1
            
        return False

    def is_in_check(self, player):
        # Find the king's position
        king_pos = None
        king_piece = 'wK' if player == 'white' else 'bK'
        for row in range(8):
            for col in range(8):
                if self.board[row][col] == king_piece:
                    king_pos = (row, col)
                    break
            if king_pos:
                break
        
        if not king_pos:
            return False
        
        # Check if any opponent's piece can capture the king
        opponent = 'black' if player == 'white' else 'white'
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece[0] == ('b' if opponent == 'black' else 'w'):
                    if self.is_valid_move(row, col, king_pos[0], king_pos[1]):
                        return True
        return False

    def get_all_legal_moves(self, player):
        moves = []
        for from_row in range(8):
            for from_col in range(8):
                piece = self.board[from_row][from_col]
                if piece and piece[0] == ('w' if player == 'white' else 'b'):
                    for to_row in range(8):
                        for to_col in range(8):
                            if self.is_valid_move(from_row, from_col, to_row, to_col):
                                # Try the move
                                original_target = self.board[to_row][to_col]
                                self.board[to_row][to_col] = piece
                                self.board[from_row][from_col] = ""
                                
                                # If the move doesn't leave/put the king in check, it's legal
                                if not self.is_in_check(player):
                                    moves.append((from_row, from_col, to_row, to_col))
                                
                                # Undo the move
                                self.board[from_row][from_col] = piece
                                self.board[to_row][to_col] = original_target
        return moves

    def is_checkmate(self):
        return self.is_in_check(self.current_player) and not self.get_all_legal_moves(self.current_player)

    def is_stalemate(self):
        return not self.is_in_check(self.current_player) and not self.get_all_legal_moves(self.current_player)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = ChessGame()
    game.run()