import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import hangman

def test_display_word():
    """Test word display function."""
    word = "python"
    
    guessed = set()
    result = hangman.display_word(word, guessed)
    assert result == "______", f"Expected '______', got '{result}'"
    print("✓ Test 1 passed: Empty guessed letters shows all underscores")
    
    guessed = {'p', 'y'}
    result = hangman.display_word(word, guessed)
    assert result == "py____", f"Expected 'py____', got '{result}'"
    print("✓ Test 2 passed: Partial guesses show correctly")
    
    guessed = {'p', 'y', 't', 'h', 'o', 'n'}
    result = hangman.display_word(word, guessed)
    assert result == "python", f"Expected 'python', got '{result}'"
    print("✓ Test 3 passed: All letters guessed shows full word")


def test_hangman_art():
    """Test hangman art stages."""
    art_0 = hangman.get_hangman_art(0)
    assert "O" not in art_0, "Stage 0 should not have head"
    print("✓ Test 4 passed: Stage 0 has no body parts")
    
    art_1 = hangman.get_hangman_art(1)
    assert "O" in art_1, "Stage 1 should have head"
    print("✓ Test 5 passed: Stage 1 has head")
    
    art_6 = hangman.get_hangman_art(6)
    assert "/" in art_6 and "\\" in art_6, "Stage 6 should have all body parts"
    print("✓ Test 6 passed: Stage 6 has complete hangman")


def test_word_list():
    """Test word list function."""
    words = hangman.get_word_list()
    assert len(words) > 0, "Word list should not be empty"
    assert all(isinstance(word, str) for word in words), "All words should be strings"
    print(f"✓ Test 7 passed: Word list has {len(words)} words")


if __name__ == "__main__":
    print("Running Hangman Tests...\n")
    test_display_word()
    test_hangman_art()
    test_word_list()
    print("\n✅ All tests passed!")
