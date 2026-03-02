import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import hangman
from unittest.mock import patch

def demo_game():
    """Demo the game with predetermined inputs to show the UI."""
    test_word = "apple"
    inputs = ['a', 'g', 'p', 'l', 'e']
    
    with patch('random.choice', return_value=test_word):
        with patch('builtins.input', side_effect=inputs):
            hangman.play_hangman()

if __name__ == "__main__":
    print("=== HANGMAN GAME DEMO ===\n")
    demo_game()
