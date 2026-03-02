import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from rock_paper_scissors import RockPaperScissors


class TestRockPaperScissors(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.game = RockPaperScissors()
    
    def test_initialization(self):
        """Test game initialization."""
        self.assertEqual(self.game.user_score, 0)
        self.assertEqual(self.game.computer_score, 0)
        self.assertEqual(self.game.draws, 0)
        self.assertEqual(len(self.game.CHOICES), 3)
        self.assertEqual(len(self.game.WINNING_COMBINATIONS), 3)
    
    def test_choices_mapping(self):
        """Test choices mapping is correct."""
        expected_choices = {1: "rock", 2: "paper", 3: "scissors"}
        self.assertEqual(self.game.CHOICES, expected_choices)
    
    def test_winning_combinations(self):
        """Test winning combinations are correct."""
        expected_combinations = {
            ("rock", "scissors"),
            ("paper", "rock"),
            ("scissors", "paper")
        }
        self.assertEqual(self.game.WINNING_COMBINATIONS, expected_combinations)
    
    def test_get_computer_choice(self):
        """Test computer choice generation."""
        choices = []
        for _ in range(100):  # Run multiple times to test randomness
            choice = self.game.get_computer_choice()
            self.assertIn(choice, ["rock", "paper", "scissors"])
            choices.append(choice)
        
        # Ensure all choices appear at least once (very high probability)
        self.assertIn("rock", choices)
        self.assertIn("paper", choices)
        self.assertIn("scissors", choices)
    
    @patch('builtins.input', return_value='1')
    def test_get_user_choice_valid(self, mock_input):
        """Test valid user input."""
        choice = self.game.get_user_choice()
        self.assertEqual(choice, "rock")
        mock_input.assert_called_once_with("Enter your choice (1-3): ")
    
    @patch('builtins.input', return_value='2')
    def test_get_user_choice_valid_paper(self, mock_input):
        """Test valid user input for paper."""
        choice = self.game.get_user_choice()
        self.assertEqual(choice, "paper")
    
    @patch('builtins.input', return_value='3')
    def test_get_user_choice_valid_scissors(self, mock_input):
        """Test valid user input for scissors."""
        choice = self.game.get_user_choice()
        self.assertEqual(choice, "scissors")
    
    @patch('builtins.input', return_value='4')
    def test_get_user_choice_invalid_number(self, mock_input):
        """Test invalid number input."""
        with self.assertRaises(ValueError) as context:
            self.game.get_user_choice()
        self.assertEqual(str(context.exception), "Choice must be 1, 2, or 3")
    
    @patch('builtins.input', return_value='abc')
    def test_get_user_choice_invalid_text(self, mock_input):
        """Test invalid text input."""
        with self.assertRaises(ValueError) as context:
            self.game.get_user_choice()
        self.assertEqual(str(context.exception), "Please enter a number (1, 2, or 3)")
    
    def test_determine_winner_user_wins_rock(self):
        """Test user wins with rock vs scissors."""
        result = self.game.determine_winner("rock", "scissors")
        self.assertEqual(result, "user")
    
    def test_determine_winner_user_wins_paper(self):
        """Test user wins with paper vs rock."""
        result = self.game.determine_winner("paper", "rock")
        self.assertEqual(result, "user")
    
    def test_determine_winner_user_wins_scissors(self):
        """Test user wins with scissors vs paper."""
        result = self.game.determine_winner("scissors", "paper")
        self.assertEqual(result, "user")
    
    def test_determine_winner_computer_wins_rock(self):
        """Test computer wins with rock vs scissors."""
        result = self.game.determine_winner("scissors", "rock")
        self.assertEqual(result, "computer")
    
    def test_determine_winner_computer_wins_paper(self):
        """Test computer wins with paper vs rock."""
        result = self.game.determine_winner("rock", "paper")
        self.assertEqual(result, "computer")
    
    def test_determine_winner_computer_wins_scissors(self):
        """Test computer wins with scissors vs paper."""
        result = self.game.determine_winner("paper", "scissors")
        self.assertEqual(result, "computer")
    
    def test_determine_winner_draw_rock(self):
        """Test draw with rock vs rock."""
        result = self.game.determine_winner("rock", "rock")
        self.assertEqual(result, "draw")
    
    def test_determine_winner_draw_paper(self):
        """Test draw with paper vs paper."""
        result = self.game.determine_winner("paper", "paper")
        self.assertEqual(result, "draw")
    
    def test_determine_winner_draw_scissors(self):
        """Test draw with scissors vs scissors."""
        result = self.game.determine_winner("scissors", "scissors")
        self.assertEqual(result, "draw")
    
    @patch('random.choice', return_value='rock')
    @patch('builtins.input', return_value='2')
    @patch('builtins.print')
    def test_play_round_user_wins(self, mock_print, mock_input, mock_random):
        """Test playing a round where user wins."""
        result = self.game.play_round()
        self.assertEqual(result, "user")
        self.assertEqual(self.game.user_score, 1)
        self.assertEqual(self.game.computer_score, 0)
        self.assertEqual(self.game.draws, 0)
    
    @patch('random.choice', return_value='paper')
    @patch('builtins.input', return_value='1')
    @patch('builtins.print')
    def test_play_round_computer_wins(self, mock_print, mock_input, mock_random):
        """Test playing a round where computer wins."""
        result = self.game.play_round()
        self.assertEqual(result, "computer")
        self.assertEqual(self.game.user_score, 0)
        self.assertEqual(self.game.computer_score, 1)
        self.assertEqual(self.game.draws, 0)
    
    @patch('random.choice', return_value='scissors')
    @patch('builtins.input', return_value='3')
    @patch('builtins.print')
    def test_play_round_draw(self, mock_print, mock_input, mock_random):
        """Test playing a round that ends in a draw."""
        result = self.game.play_round()
        self.assertEqual(result, "draw")
        self.assertEqual(self.game.user_score, 0)
        self.assertEqual(self.game.computer_score, 0)
        self.assertEqual(self.game.draws, 1)
    
    @patch('builtins.input', return_value='invalid')
    def test_play_round_invalid_input(self, mock_input):
        """Test playing a round with invalid input."""
        result = self.game.play_round()
        self.assertIsNone(result)
        self.assertEqual(self.game.user_score, 0)
        self.assertEqual(self.game.computer_score, 0)
        self.assertEqual(self.game.draws, 0)
    
    @patch('builtins.print')
    def test_display_scores(self, mock_print):
        """Test score display."""
        self.game.user_score = 3
        self.game.computer_score = 2
        self.game.draws = 1
        
        self.game.display_scores()
        
        # Check that print was called with score information
        calls = [str(call) for call in mock_print.call_args_list]
        score_output = ' '.join(calls)
        self.assertIn("You: 3", score_output)
        self.assertIn("Computer: 2", score_output)
        self.assertIn("Draws: 1", score_output)
    
    def test_all_possible_outcomes(self):
        """Test all possible game outcomes systematically."""
        choices = ["rock", "paper", "scissors"]
        
        for user_choice in choices:
            for computer_choice in choices:
                result = self.game.determine_winner(user_choice, computer_choice)
                
                if user_choice == computer_choice:
                    self.assertEqual(result, "draw")
                elif (user_choice, computer_choice) in self.game.WINNING_COMBINATIONS:
                    self.assertEqual(result, "user")
                else:
                    self.assertEqual(result, "computer")
    
    def test_score_tracking_across_rounds(self):
        """Test score tracking across multiple rounds."""
        # Simulate multiple rounds
        results = ["user", "computer", "draw", "user", "computer"]
        
        for result in results:
            if result == "user":
                self.game.user_score += 1
            elif result == "computer":
                self.game.computer_score += 1
            else:
                self.game.draws += 1
        
        self.assertEqual(self.game.user_score, 2)
        self.assertEqual(self.game.computer_score, 2)
        self.assertEqual(self.game.draws, 1)


if __name__ == '__main__':
    unittest.main()
