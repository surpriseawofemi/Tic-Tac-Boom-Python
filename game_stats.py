# game_stats.py - Handles numerical tracking of game statistics
class GameStats:
    """
    Tracks and analyzes numerical data about game play.
    Demonstrates numerical programming concepts.
    """
    
    def __init__(self):
        """Initialize game statistics tracking."""
        self.games_played = 0
        self.x_wins = 0
        self.o_wins = 0
        self.draws = 0
        self.boom_occurrences = 0
        self.move_history = []
    
    def record_game_result(self, winner=None, had_boom=False):
        """
        Record the result of a completed game.
        
        Args:
            winner (str, optional): The winning player ("X" or "O"), or None for a draw
            had_boom (bool, optional): Whether the boom effect occurred
        """
        self.games_played += 1
        
        if winner == "X":
            self.x_wins += 1
        elif winner == "O":
            self.o_wins += 1
        else:
            self.draws += 1
            
        if had_boom:
            self.boom_occurrences += 1
    
    def record_move(self, player, row, col, move_number):
        """
        Record a move in the move history.
        
        Args:
            player (str): The player making the move ("X" or "O")
            row (int): Row index of the move
            col (int): Column index of the move
            move_number (int): The sequential number of this move in the game
        """
        self.move_history.append({
            'player': player,
            'row': row,
            'col': col,
            'move_number': move_number
        })
    
    def get_win_percentage(self, player):
        """
        Calculate the win percentage for a specific player.
        
        Args:
            player (str): The player to calculate for ("X" or "O")
            
        Returns:
            float: Win percentage (0-100)
        """
        if self.games_played == 0:
            return 0.0
            
        wins = self.x_wins if player == "X" else self.o_wins
        return (wins / self.games_played) * 100
    
    def get_boom_percentage(self):
        """
        Calculate the percentage of games that ended with a boom.
        
        Returns:
            float: Boom occurrence percentage (0-100)
        """
        if self.games_played == 0:
            return 0.0
            
        return (self.boom_occurrences / self.games_played) * 100
    
    def get_move_frequency_by_position(self):
        """
        Analyze the frequency of moves in each position of the board.
        
        Returns:
            dict: A dictionary mapping positions to move counts
        """
        position_counts = {(r, c): 0 for r in range(3) for c in range(3)}
        
        for move in self.move_history:
            position = (move['row'], move['col'])
            position_counts[position] += 1
            
        return position_counts
    
    def get_average_moves_per_game(self):
        """
        Calculate the average number of moves per game.
        
        Returns:
            float: Average moves per game
        """
        if self.games_played == 0:
            return 0.0
            
        total_moves = len(self.move_history)
        return total_moves / self.games_played