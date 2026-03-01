import random

def get_hangman_art(wrong_guesses):
    """Returns the hangman ASCII art based on number of wrong guesses."""
    stages = [
        # 0 wrong guesses - just gallows
        """
  +---+
  |   |
      |
      |
      |
      |
==========""",
        # 1 wrong guess - head
        """
  +---+
  |   |
  O   |
      |
      |
      |
==========""",
        # 2 wrong guesses - body
        """
  +---+
  |   |
  O   |
  |   |
      |
      |
==========""",
        # 3 wrong guesses - left arm
        """
  +---+
  |   |
  O   |
 /|   |
      |
      |
==========""",
        # 4 wrong guesses - right arm
        """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
==========""",
        # 5 wrong guesses - left leg
        """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
==========""",
        # 6 wrong guesses - right leg (game over)
        """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
==========""",
    ]
    return stages[wrong_guesses]


def get_word_list():
    """Returns a list of words for the game."""
    return ["python", "hangman", "programming", "computer", "algorithm", "function", "variable", "loop", "array", "string"]


def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed and underscores for unguessed."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def play_hangman():
    """Main game function."""
    word = random.choice(get_word_list())
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6
    
    print("Welcome to Hangman!")
    print(get_hangman_art(wrong_guesses))
    
    while wrong_guesses < max_wrong_guesses:
        word_display = display_word(word, guessed_letters)
        lives_left = max_wrong_guesses - wrong_guesses
        
        print(f"\n{'*' * 80}")
        print(f"{'*' * 30}{lives_left}/{max_wrong_guesses} LIVES LEFT{'*' * 30}")
        print(f"Word to guess: {word_display}")
        
        if "_" not in word_display:
            print("\nCongratulations! You won! You guessed the word:", word)
            break
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        print(get_hangman_art(wrong_guesses))
    
    if wrong_guesses == max_wrong_guesses:
        print(f"\n{'*' * 80}")
        print("Game Over! You lost. The word was:", word)


if __name__ == "__main__":
    play_hangman()
