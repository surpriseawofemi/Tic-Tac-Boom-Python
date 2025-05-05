# game_controller.py - Controls the game flow and connects model with view
import random
from PyQt5.QtWidgets import (QMainWindow, QGridLayout, QVBoxLayout, 
                            QPushButton, QLabel, QWidget)
from PyQt5.QtCore import Qt, QPropertyAnimation, QSize, QTimer
from PyQt5.QtGui import QFont

from game_model import GameModel

class TicTacBoomGame(QMainWindow):
    """
    Main game controller class that manages the UI and interacts with the game model.
    Implements the Tic Tac Boom game with a random chance for a boom effect on wins.
    """
    
    def __init__(self):
        """Initialize the game window, UI components, and game model."""
        super().__init__()
        
        # Setup the game model
        self.game_model = GameModel()
        
        # Setup window properties
        self.setWindowTitle("Tic Tac Boom")
        self.setGeometry(100, 100, 800, 450)
        
        # Create UI components
        self._setup_ui()
        
    def _setup_ui(self):
        """Set up the user interface components."""
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # Create layout
        main_layout = QVBoxLayout(main_widget)
        
        # Status text
        self.status_text = QLabel(f"Player {self.game_model.current_player}'s turn")
        self.status_text.setAlignment(Qt.AlignCenter)
        self.status_text.setFont(QFont("Arial", 20))
        main_layout.addWidget(self.status_text)
        
        # Game grid
        game_widget = QWidget()
        self.game_grid = QGridLayout(game_widget)
        self.game_grid.setSpacing(10)
        main_layout.addWidget(game_widget)
        
        # Initialize buttons
        self.buttons = []
        for row in range(3):
            for col in range(3):
                button = QPushButton()
                button.setFixedSize(120, 120)
                button.setFont(QFont("Arial", 36, QFont.Bold))
                button.clicked.connect(lambda checked, r=row, c=col: self.make_move(r, c))
                self.game_grid.addWidget(button, row, col)
                self.buttons.append(button)
        
        # Restart button
        self.restart_button = QPushButton("Restart")
        self.restart_button.setFixedSize(100, 40)
        self.restart_button.clicked.connect(self.restart_game)
        main_layout.addWidget(self.restart_button, 0, Qt.AlignCenter)
        
        # Boom text
        self.boom_text = QLabel("💥 BOOM! 💥")
        self.boom_text.setFont(QFont("Arial", 72, QFont.Bold))
        self.boom_text.setStyleSheet("color: red;")
        self.boom_text.setAlignment(Qt.AlignCenter)
        self.boom_text.hide()
        
        # Position boom text over the grid
        main_layout.addWidget(self.boom_text)
    
    def make_move(self, row, col):
        """
        Handle a player's move.
        
        Args:
            row (int): Row index (0-2)
            col (int): Column index (0-2)
        """
        # Attempt to make a move in the model
        if self.game_model.make_move(row, col):
            # Update UI to reflect the move
            button_index = row * 3 + col
            self.buttons[button_index].setText(self.game_model.board[row][col])
            
            # Check if game has ended
            if self.game_model.game_over:
                if self.game_model.winner:
                    self.status_text.setText(f"Player {self.game_model.winner} wins!")
                    
                    # Random chance for boom effect (30%)
                    if random.random() < 0.3:
                        self.show_boom_effect()
                else:
                    self.status_text.setText("It's a draw!")
            else:
                # Continue to next player's turn
                self.status_text.setText(f"Player {self.game_model.current_player}'s turn")
    
    def show_boom_effect(self):
        """Display the boom animation effect."""
        print("Showing boom effect in base game!")  # Debug statement
        self.boom_text.show()
        self.boom_text.raise_()  # Ensure the boom text is on top
        
        # Use a timer-based animation approach
        def animate_size(size):
            self.boom_text.setFont(QFont("Arial", size, QFont.Bold))
        
        # Animation sequence
        QTimer.singleShot(100, lambda: animate_size(48))
        QTimer.singleShot(200, lambda: animate_size(60))
        QTimer.singleShot(300, lambda: animate_size(72))
        QTimer.singleShot(400, lambda: animate_size(84))
        QTimer.singleShot(500, lambda: animate_size(96))
        QTimer.singleShot(600, lambda: animate_size(84))
        QTimer.singleShot(700, lambda: animate_size(72))
        QTimer.singleShot(800, lambda: animate_size(60))
        
        # Hide boom text after animation
        QTimer.singleShot(2000, lambda: self.boom_text.hide())
    
    def restart_game(self):
        """Reset the game to its initial state."""
        # Reset the model
        self.game_model.reset_game()
        
        # Reset UI
        for button in self.buttons:
            button.setText("")
        
        self.status_text.setText(f"Player {self.game_model.current_player}'s turn")
        self.boom_text.hide()