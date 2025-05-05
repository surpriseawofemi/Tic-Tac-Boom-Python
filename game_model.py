# game_model.py - Contains the game logic and state
class GameModel:
    """Represents the logical state and rules of the Tic Tac Boom game."""
    
    def __init__(self):
        """Initialize a new game model with an empty board."""
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.winner = None
    
    def make_move(self, row, col):
        """
        Attempt to make a move at the specified position.
        
        Args:
            row (int): Row index (0-2)
            col (int): Column index (0-2)
            
        Returns:
            bool: True if the move was valid and made, False otherwise
        """
        if self.game_over or self.board[row][col] != "":
            return False
        
        # Update the board
        self.board[row][col] = self.current_player
        
        # Check for win or draw
        if self.check_winner(row, col):
            self.game_over = True
            self.winner = self.current_player
            return True
        
        # Check for draw
        if all(self.board[r][c] != "" for r in range(3) for c in range(3)):
            self.game_over = True
            return True
        
        # Switch player
        self.current_player = "O" if self.current_player == "X" else "X"
        return True
    
    def check_winner(self, row, col):
        """
        Check if the current move resulted in a win.
        
        Args:
            row (int): Row of the last move
            col (int): Column of the last move
            
        Returns:
            bool: True if the current player has won, False otherwise
        """
        player = self.board[row][col]
        
        # Check row
        if all(self.board[row][c] == player for c in range(3)):
            return True
        
        # Check column
        if all(self.board[r][col] == player for r in range(3)):
            return True
        
        # Check diagonals
        if row == col and all(self.board[i][i] == player for i in range(3)):
            return True
        
        if row + col == 2 and all(self.board[i][2-i] == player for i in range(3)):
            return True
        
        return False
    
    def reset_game(self):
        """Reset the game to its initial state."""
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.winner = None