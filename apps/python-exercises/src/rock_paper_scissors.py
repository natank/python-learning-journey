import random


class RockPaperScissors:
    """Interactive Rock, Paper, Scissors game."""
    
    CHOICES = {
        1: "rock",
        2: "paper", 
        3: "scissors"
    }
    
    WINNING_COMBINATIONS = {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper")
    }
    
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.draws = 0
    
    def get_user_choice(self):
        """
        Get user input and validate it.
        
        Returns:
            str: User's choice (rock, paper, or scissors)
            
        Raises:
            ValueError: If input is not valid
        """
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        
        try:
            choice_num = int(input("Enter your choice (1-3): "))
            if choice_num not in self.CHOICES:
                raise ValueError("Choice must be 1, 2, or 3")
            return self.CHOICES[choice_num]
        except ValueError as e:
            if "invalid literal" in str(e):
                raise ValueError("Please enter a number (1, 2, or 3)")
            raise
    
    def get_computer_choice(self):
        """
        Generate random computer choice.
        
        Returns:
            str: Computer's choice (rock, paper, or scissors)
        """
        return random.choice(list(self.CHOICES.values()))
    
    def determine_winner(self, user_choice, computer_choice):
        """
        Determine the winner of a round.
        
        Args:
            user_choice (str): User's choice
            computer_choice (str): Computer's choice
            
        Returns:
            str: "user", "computer", or "draw"
        """
        if user_choice == computer_choice:
            return "draw"
        
        if (user_choice, computer_choice) in self.WINNING_COMBINATIONS:
            return "user"
        else:
            return "computer"
    
    def play_round(self):
        """
        Play a single round of the game.
        
        Returns:
            str: Result of the round ("user", "computer", or "draw")
        """
        try:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            
            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")
            
            result = self.determine_winner(user_choice, computer_choice)
            
            if result == "user":
                print("🎉 You win this round!")
                self.user_score += 1
            elif result == "computer":
                print("💻 Computer wins this round!")
                self.computer_score += 1
            else:
                print("🤝 It's a draw!")
                self.draws += 1
            
            return result
            
        except ValueError as e:
            print(f"❌ Invalid input: {e}")
            return None
    
    def display_scores(self):
        """Display current scores."""
        print(f"\n📊 Score:")
        print(f"You: {self.user_score}")
        print(f"Computer: {self.computer_score}")
        print(f"Draws: {self.draws}")
    
    def play_game(self):
        """
        Play the complete game with multiple rounds.
        """
        print("🎮 Welcome to Rock, Paper, Scissors!")
        print("=====================================")
        
        while True:
            result = self.play_round()
            
            if result is not None:
                self.display_scores()
                
                play_again = input("\nPlay again? (y/n): ").lower().strip()
                if play_again not in ['y', 'yes']:
                    break
            else:
                # Invalid input, ask if they want to try again
                try_again = input("\nTry again? (y/n): ").lower().strip()
                if try_again not in ['y', 'yes']:
                    break
        
        print(f"\n🏁 Final Score:")
        print(f"You: {self.user_score}")
        print(f"Computer: {self.computer_score}")
        print(f"Draws: {self.draws}")
        
        if self.user_score > self.computer_score:
            print("🏆 You are the overall winner!")
        elif self.computer_score > self.user_score:
            print("🤖 Computer is the overall winner!")
        else:
            print("🤝 The game ended in a draw!")


def main():
    """Main function to run the game."""
    game = RockPaperScissors()
    game.play_game()


if __name__ == "__main__":
    main()
