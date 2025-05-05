# main.py - The entry point of the application
import sys
from PyQt5.QtWidgets import QApplication
from game_controller import TicTacBoomGame

def main():
    """Main entry point for the Tic Tac Boom game."""
    app = QApplication(sys.argv)
    window = TicTacBoomGame()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()