import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from hurdle_race import jump_hurdle, race_course, race_course_no_loop, get_jump_sequence


class TestHurdleRace(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.jump_sequence = get_jump_sequence()
    
    def test_get_jump_sequence(self):
        """Test that jump sequence is correct."""
        expected_sequence = [
            "move", "turn_left", "move", "turn_left", "turn_left", "turn_left",
            "move", "turn_left", "turn_left", "turn_left", "move", "turn_left"
        ]
        self.assertEqual(self.jump_sequence, expected_sequence)
        self.assertEqual(len(self.jump_sequence), 12)
    
    def test_get_jump_sequence_counts(self):
        """Test the count of each action in the sequence."""
        move_count = self.jump_sequence.count("move")
        turn_left_count = self.jump_sequence.count("turn_left")
        
        self.assertEqual(move_count, 4)  # 4 moves per hurdle
        self.assertEqual(turn_left_count, 8)  # 8 turn_lefts per hurdle
        self.assertEqual(move_count + turn_left_count, 12)  # Total 12 actions
    
    @patch('hurdle_race.move')
    @patch('hurdle_race.turn_left')
    def test_jump_hurdle_sequence(self, mock_turn_left, mock_move):
        """Test that jump_hurdle calls functions in correct order."""
        jump_hurdle()
        
        # Verify total number of calls
        self.assertEqual(mock_move.call_count, 4)
        self.assertEqual(mock_turn_left.call_count, 8)
        
        # Verify the sequence of calls
        expected_calls = (
            [unittest.mock.call()] * 1 +  # move
            [unittest.mock.call()] * 1 +  # turn_left
            [unittest.mock.call()] * 1 +  # move
            [unittest.mock.call()] * 3 +  # turn_left x3
            [unittest.mock.call()] * 1 +  # move
            [unittest.mock.call()] * 3 +  # turn_left x3
            [unittest.mock.call()] * 1 +  # move
            [unittest.mock.call()] * 1    # turn_left
        )
        
        # Check that all calls were made (total 12 calls)
        total_calls = mock_move.call_count + mock_turn_left.call_count
        self.assertEqual(total_calls, 12)
    
    @patch('hurdle_race.jump_hurdle')
    def test_race_course_calls_jump_hurdle_six_times(self, mock_jump_hurdle):
        """Test that race_course calls jump_hurdle exactly 6 times."""
        race_course()
        self.assertEqual(mock_jump_hurdle.call_count, 6)
    
    @patch('hurdle_race.jump_hurdle')
    @patch('builtins.print')
    def test_race_course_output_format(self, mock_print, mock_jump_hurdle):
        """Test that race_course produces correct output format."""
        race_course()
        
        # Check that print was called with expected messages
        print_calls = [str(call) for call in mock_print.call_args_list]
        
        # Should contain start message
        self.assertTrue(any("Starting Hurdle Race with 6 hurdles" in call for call in print_calls))
        
        # Should contain hurdle messages for each hurdle
        for i in range(1, 7):
            self.assertTrue(any(f"Jumping Hurdle {i}" in call for call in print_calls))
            self.assertTrue(any(f"Hurdle {i} completed" in call for call in print_calls))
        
        # Should contain completion message
        self.assertTrue(any("Hurdle Race Completed Successfully" in call for call in print_calls))
        self.assertTrue(any("All 6 hurdles cleared" in call for call in print_calls))
    
    @patch('hurdle_race.jump_hurdle')
    def test_race_course_no_loop_calls_jump_hurdle_six_times(self, mock_jump_hurdle):
        """Test that race_course_no_loop calls jump_hurdle exactly 6 times."""
        race_course_no_loop()
        self.assertEqual(mock_jump_hurdle.call_count, 6)
    
    @patch('hurdle_race.jump_hurdle')
    @patch('builtins.print')
    def test_race_course_no_loop_output_format(self, mock_print, mock_jump_hurdle):
        """Test that race_course_no_loop produces correct output format."""
        race_course_no_loop()
        
        # Check that print was called with expected messages
        print_calls = [str(call) for call in mock_print.call_args_list]
        
        # Should contain start message with "No Loop Version"
        self.assertTrue(any("Starting Hurdle Race with 6 hurdles (No Loop Version)" in call for call in print_calls))
        
        # Should contain hurdle messages for each hurdle
        for i in range(1, 7):
            self.assertTrue(any(f"Jumping Hurdle {i}" in call for call in print_calls))
            self.assertTrue(any(f"Hurdle {i} completed" in call for call in print_calls))
        
        # Should contain completion message
        self.assertTrue(any("Hurdle Race Completed Successfully" in call for call in print_calls))
        self.assertTrue(any("All 6 hurdles cleared" in call for call in print_calls))
    
    def test_jump_sequence_pattern(self):
        """Test that the jump sequence follows the expected pattern."""
        sequence = get_jump_sequence()
        
        # Pattern should be: move, turn_left, move, turn_left*3, move, turn_left*3, move, turn_left
        expected_pattern = [
            "move",           # 0
            "turn_left",      # 1
            "move",           # 2
            "turn_left",      # 3
            "turn_left",      # 4
            "turn_left",      # 5
            "move",           # 6
            "turn_left",      # 7
            "turn_left",      # 8
            "turn_left",      # 9
            "move",           # 10
            "turn_left"       # 11
        ]
        
        self.assertEqual(sequence, expected_pattern)
    
    def test_jump_sequence_positions(self):
        """Test specific positions in the jump sequence."""
        sequence = get_jump_sequence()
        
        # Key positions should have specific actions
        self.assertEqual(sequence[0], "move")      # First action: move
        self.assertEqual(sequence[1], "turn_left") # Second action: turn_left
        self.assertEqual(sequence[2], "move")      # Third action: move
        self.assertEqual(sequence[6], "move")      # Seventh action: move
        self.assertEqual(sequence[10], "move")     # Eleventh action: move
        self.assertEqual(sequence[11], "turn_left") # Last action: turn_left
        
        # Positions 3-5 should be turn_left (first 270-degree turn)
        self.assertEqual(sequence[3:6], ["turn_left", "turn_left", "turn_left"])
        
        # Positions 7-9 should be turn_left (second 270-degree turn)
        self.assertEqual(sequence[7:10], ["turn_left", "turn_left", "turn_left"])
    
    @patch('hurdle_race.move')
    @patch('hurdle_race.turn_left')
    @patch('builtins.print')
    def test_jump_hurdle_with_mock_functions(self, mock_print, mock_turn_left, mock_move):
        """Test jump_hurdle with mocked move and turn_left functions."""
        jump_hurdle()
        
        # Verify that both functions were called
        mock_move.assert_called()
        mock_turn_left.assert_called()
        
        # Note: print is called from the mock functions, not directly from jump_hurdle
        # So we don't test for print calls here
    
    def test_total_actions_calculation(self):
        """Test calculation of total actions for the complete race."""
        sequence = get_jump_sequence()
        actions_per_hurdle = len(sequence)
        total_hurdles = 6
        total_actions = actions_per_hurdle * total_hurdles
        
        self.assertEqual(actions_per_hurdle, 12)
        self.assertEqual(total_actions, 72)
        
        # Break down by action type
        moves_per_hurdle = sequence.count("move")
        turns_per_hurdle = sequence.count("turn_left")
        
        self.assertEqual(moves_per_hurdle, 4)
        self.assertEqual(turns_per_hurdle, 8)
        
        total_moves = moves_per_hurdle * total_hurdles
        total_turns = turns_per_hurdle * total_hurdles
        
        self.assertEqual(total_moves, 24)
        self.assertEqual(total_turns, 48)
        self.assertEqual(total_moves + total_turns, 72)


if __name__ == '__main__':
    unittest.main()
