# Hangman Game Implementation

## Summary
Implemented a fully functional Hangman game in Python with comprehensive testing suite and proper project structure.

## Features Implemented
- **Complete Hangman Game**: ASCII art gallows with 6 body parts that appear on wrong guesses
- **Word Selection**: Random word picker from predefined list of programming-related words
- **Game Logic**: 
  - Correct guesses reveal letters in their positions
  - Wrong guesses add body parts and decrement lives
  - Win condition: guess all letters before 6 wrong guesses
  - Lose condition: 6 wrong guesses (full hangman)
- **User Interface**:
  - Lives counter display (X/6 LIVES LEFT)
  - Word display with underscores for unguessed letters
  - Clear error messages for wrong guesses
  - Input validation and duplicate guess handling

## Files Added
- `apps/python-beginner-exercises/src/hangman.py` - Main game implementation
- `apps/python-beginner-exercises/tests/test_hangman.py` - Unit tests for core functions
- `apps/python-beginner-exercises/tests/test_hangman_integration.py` - Integration tests for game scenarios
- `apps/python-beginner-exercises/tests/demo_hangman.py` - Demo script for testing

## Testing
- **Unit Tests**: 7 tests covering word display, ASCII art stages, and word list
- **Integration Tests**: 4 tests covering winning, losing, mixed gameplay, and duplicate guesses
- **All tests pass**: Verified functionality works as expected

## Project Structure
- Proper separation of source code (`src/`) and tests (`tests/`)
- Updated import paths to work from new structure
- Clean organization following Python best practices

## How to Play
```bash
cd apps/python-beginner-exercises
python3 src/hangman.py
```

## Game Flow
1. Game selects random word and displays empty gallows
2. User guesses letters one at a time
3. Correct letters reveal their positions
4. Wrong guesses add body parts and show "You lose a life" message
5. Game ends when word is guessed (win) or 6 wrong guesses made (lose)

## Technical Details
- ASCII art with 7 stages (0-6 wrong guesses)
- Input validation for single letters only
- Duplicate guess detection and warning
- Proper game state management
- Clear visual feedback with separator lines

This implementation matches the specification in `docs/hangman.md` and provides a complete, tested Hangman game experience.
