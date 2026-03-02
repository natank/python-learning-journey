import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import hangman
from unittest.mock import patch
import io
import sys

def test_winning_game():
    """Test a complete winning game scenario."""
    print("Testing winning game scenario...")
    
    test_word = "apple"
    inputs = ['a', 'p', 'l', 'e']
    
    with patch('random.choice', return_value=test_word):
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                hangman.play_hangman()
                output = mock_stdout.getvalue()
                
                assert "Congratulations! You won!" in output, "Should show win message"
                assert test_word in output, "Should show the word"
                print("✓ Winning game test passed")


def test_losing_game():
    """Test a complete losing game scenario."""
    print("Testing losing game scenario...")
    
    test_word = "python"
    wrong_guesses = ['a', 'b', 'c', 'd', 'e', 'f']
    
    with patch('random.choice', return_value=test_word):
        with patch('builtins.input', side_effect=wrong_guesses):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                hangman.play_hangman()
                output = mock_stdout.getvalue()
                
                assert "Game Over! You lost" in output, "Should show lose message"
                assert test_word in output, "Should reveal the word"
                assert "6/6 LIVES LEFT" in output, "Should show initial lives"
                print("✓ Losing game test passed")


def test_mixed_game():
    """Test a game with both correct and incorrect guesses."""
    print("Testing mixed game scenario...")
    
    test_word = "cat"
    inputs = ['c', 'x', 'a', 'y', 't']
    
    with patch('random.choice', return_value=test_word):
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                hangman.play_hangman()
                output = mock_stdout.getvalue()
                
                assert "You lose a life" in output, "Should show life loss message"
                assert "Congratulations! You won!" in output, "Should win eventually"
                assert "4/6 LIVES LEFT" in output, "Should show decreased lives"
                print("✓ Mixed game test passed")


def test_duplicate_guess():
    """Test handling of duplicate letter guesses."""
    print("Testing duplicate guess handling...")
    
    test_word = "dog"
    inputs = ['d', 'd', 'o', 'g']
    
    with patch('random.choice', return_value=test_word):
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                hangman.play_hangman()
                output = mock_stdout.getvalue()
                
                assert "already guessed" in output, "Should warn about duplicate"
                print("✓ Duplicate guess test passed")


if __name__ == "__main__":
    print("Running Hangman Integration Tests...\n")
    test_winning_game()
    test_losing_game()
    test_mixed_game()
    test_duplicate_guess()
    print("\n✅ All integration tests passed!")
