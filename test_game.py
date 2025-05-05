# test_game.py
import unittest
from game_model import GameModel
from game_stats import GameStats
from game_ai import GameAI

class TestGameModel(unittest.TestCase):
    def setUp(self):
        self.model = GameModel()

    def test_initial_player(self):
        """Test that the initial player is 'X'."""
        self.assertEqual(self.model.current_player, "X")

    def test_game_not_over_at_start(self):
        """Test that the game is not over at the beginning."""
        self.assertFalse(self.model.game_over)

    def test_make_valid_move_updates_board(self):
        """Test that a valid move updates the board."""
        self.model.make_move(0, 0)
        self.assertEqual(self.model.board[0][0], "X")

    def test_switch_player_after_move(self):
        """Test that the player switches after a valid move."""
        self.model.make_move(0, 0)
        self.assertEqual(self.model.current_player, "O")

class TestGameStats(unittest.TestCase):
    def setUp(self):
        self.stats = GameStats()

    def test_initial_games_played_is_zero(self):
        """Test that the initial number of games played is 0."""
        self.assertEqual(self.stats.games_played, 0)

    def test_initial_x_wins_is_zero(self):
        """Test that the initial number of X wins is 0."""
        self.assertEqual(self.stats.x_wins, 0)

    def test_record_game_result_increments_games_played(self):
        """Test that recording a game result increments games_played."""
        self.stats.record_game_result()
        self.assertEqual(self.stats.games_played, 1)

    def test_record_x_win(self):
        self.stats.record_game_result(winner="X")
        self.assertEqual(self.stats.x_wins, 1)

class TestGameAI(unittest.TestCase):
    def setUp(self):
        self.ai_easy = GameAI(difficulty="easy")
        self.empty_board = [["", "", ""], ["", "", ""], ["", "", ""]]

    def test_easy_ai_returns_a_move(self):
        """Test that the easy AI returns a move."""
        move = self.ai_easy.get_move(self.empty_board, "O")
        self.assertIsNotNone(move)  # Check that it doesn't return None

if __name__ == '__main__':
    unittest.main()