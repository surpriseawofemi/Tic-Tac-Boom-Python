# game_ai.py - Simple AI opponent implementation (symbolic programming example)
import random

class GameAI:
    """
    Implements a simple AI for Tic Tac Boom.
    Demonstrates symbolic programming concepts.
    """
    
    def __init__(self, difficulty="medium"):
        """
        Initialize the AI with a specified difficulty level.
        
        Args:
            difficulty (str): The difficulty level - "easy", "medium", or "hard"
        """
        self.difficulty = difficulty
    
    def get_move(self, board, player):
        """
        Determine the best move for the AI based on the current board state.
        
        Args:
            board (list): 2D list representing the game board
            player (str): The AI's player symbol ("X" or "O")
            
        Returns:
            tuple: (row, col) coordinates for the AI's move
        """
        # Easy difficulty: random move
        if self.difficulty == "easy":
            return self._get_random_move(board)
        
        # Medium difficulty: win if possible, block opponent, otherwise random
        elif self.difficulty == "medium":
            # Try to win
            winning_move = self._find_winning_move(board, player)
            if winning_move:
                return winning_move
                
            # Try to block opponent
            opponent = "O" if player == "X" else "X"
            blocking_move = self._find_winning_move(board, opponent)
            if blocking_move:
                return blocking_move
                
            # Otherwise random
            return self._get_random_move(board)
        
        # Hard difficulty: win if possible, block opponent, center, corners, then sides
        elif self.difficulty == "hard":
            # Try to win
            winning_move = self._find_winning_move(board, player)
            if winning_move:
                return winning_move
                
            # Try to block opponent
            opponent = "O" if player == "X" else "X"
            blocking_move = self._find_winning_move(board, opponent)
            if blocking_move:
                return blocking_move
            
            # Take center if available
            if board[1][1] == "":
                return (1, 1)
                
            # Take corners if available
            corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
            random.shuffle(corners)
            for corner in corners:
                r, c = corner
                if board[r][c] == "":
                    return corner
            
            # Take sides if available
            sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
            random.shuffle(sides)
            for side in sides:
                r, c = side
                if board[r][c] == "":
                    return side
        
        # Fallback
        return self._get_random_move(board)
    
    def _get_random_move(self, board):
        """
        Choose a random empty cell on the board.
        
        Args:
            board (list): 2D list representing the game board
            
        Returns:
            tuple: (row, col) coordinates for a random valid move
        """
        empty_cells = []
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    empty_cells.append((r, c))
        
        if empty_cells:
            return random.choice(empty_cells)
        return None
    
    def _find_winning_move(self, board, player):
        """
        Find a move that would result in a win for the specified player.
        
        Args:
            board (list): 2D list representing the game board
            player (str): The player symbol to check winning moves for
            
        Returns:
            tuple: (row, col) coordinates for a winning move, or None if no winning move exists
        """
        # Check rows
        for r in range(3):
            if board[r].count(player) == 2 and "" in board[r]:
                c = board[r].index("")
                return (r, c)
        
        # Check columns
        for c in range(3):
            column = [board[r][c] for r in range(3)]
            if column.count(player) == 2 and "" in column:
                r = column.index("")
                return (r, c)
        
        # Check main diagonal
        diagonal = [board[i][i] for i in range(3)]
        if diagonal.count(player) == 2 and "" in diagonal:
            i = diagonal.index("")
            return (i, i)
        
        # Check other diagonal
        diagonal = [board[i][2-i] for i in range(3)]
        if diagonal.count(player) == 2 and "" in diagonal:
            i = diagonal.index("")
            return (i, 2-i)
        
        return None