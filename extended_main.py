# extended_main.py - Enhanced main application with AI and stats tracking
import sys
import random
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from game_controller import TicTacBoomGame
from game_stats import GameStats
from game_ai import GameAI

class EnhancedTicTacBoomGame(TicTacBoomGame):
    """
    Enhanced version of the Tic Tac Boom game with AI opponent and statistics tracking.
    """
    
    def __init__(self, ai_enabled=False, ai_difficulty="medium", track_stats=True):
        """
        Initialize the enhanced game.
        
        Args:
            ai_enabled (bool): Whether to enable AI opponent
            ai_difficulty (str): AI difficulty level ("easy", "medium", or "hard")
            track_stats (bool): Whether to track game statistics
        """
        # Call parent constructor first
        super().__init__()
        
        self.ai_enabled = ai_enabled
        if ai_enabled:
            self.ai = GameAI(difficulty=ai_difficulty)
        
        self.track_stats = track_stats
        if track_stats:
            self.stats = GameStats()
            
        self.move_count = 0
        self.had_boom = False
    
    def make_move(self, row, col):
        """
        Override the make_move method to add AI and statistics functionality.
        
        Args:
            row (int): Row index (0-2)
            col (int): Column index (0-2)
        """
        if self.game_model.game_over:
            return
            
        # Track move if stats are enabled
        current_player = self.game_model.current_player
        self.move_count += 1
        
        # Make the move in the base game model
        if self.game_model.make_move(row, col):
            # Update UI to reflect the move
            button_index = row * 3 + col
            self.buttons[button_index].setText(self.game_model.board[row][col])
            
            # Record the move in stats
            if self.track_stats:
                self.stats.record_move(current_player, row, col, self.move_count)
            
            # Check if game has ended
            if self.game_model.game_over:
                if self.game_model.winner:
                    self.status_text.setText(f"Player {self.game_model.winner} wins!")
                    
                    # Random chance for boom effect (30%)
                    if random.random() < 0.3:
                        print("Triggering boom in enhanced game")  # Debug
                        self.show_boom_effect()
                        self.had_boom = True
                else:
                    self.status_text.setText("It's a draw!")
            else:
                # Continue to next player's turn
                self.status_text.setText(f"Player {self.game_model.current_player}'s turn")
                
                # AI move if enabled and it's AI's turn
                if (self.ai_enabled and self.game_model.current_player == "O"):
                    QTimer.singleShot(500, self._make_ai_move)
    
    def _make_ai_move(self):
        """Have the AI make a move."""
        ai_row, ai_col = self.ai.get_move(self.game_model.board, "O")
        if ai_row is not None and ai_col is not None:
            self.make_move(ai_row, ai_col)
    
    def restart_game(self):
        """Override to record game results in stats before restarting."""
        if self.track_stats and self.game_model.game_over:
            self.stats.record_game_result(
                winner=self.game_model.winner,
                had_boom=self.had_boom
            )
            
            # Show statistics after every 5 games
            if self.stats.games_played % 5 == 0:
                self._show_stats()
        
        # Reset tracking variables
        self.move_count = 0
        self.had_boom = False
        
        # Call the parent restart_game method
        super().restart_game()
    
    def _show_stats(self):
        """Display a message box with current game statistics."""
        msg = QMessageBox()
        msg.setWindowTitle("Game Statistics")
        
        # Build statistics message
        text = f"Games Played: {self.stats.games_played}\n"
        text += f"Player X Wins: {self.stats.x_wins} ({self.stats.get_win_percentage('X'):.1f}%)\n"
        text += f"Player O Wins: {self.stats.o_wins} ({self.stats.get_win_percentage('O'):.1f}%)\n"
        text += f"Draws: {self.stats.draws}\n"
        text += f"Boom Occurrences: {self.stats.boom_occurrences} ({self.stats.get_boom_percentage():.1f}%)\n"
        text += f"Average Moves Per Game: {self.stats.get_average_moves_per_game():.1f}"
        
        msg.setText(text)
        msg.exec_()

def main():
    """Main entry point for the enhanced Tic Tac Boom game."""
    app = QApplication(sys.argv)
    
    # Create game with AI and stats tracking enabled
    window = EnhancedTicTacBoomGame(ai_enabled=True, ai_difficulty="medium", track_stats=True)
    window.setWindowTitle("Tic Tac Boom with AI")
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()