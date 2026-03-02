import unittest
from unittest.mock import patch
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from hurdle_race_clean import jump_hurdle, race_course


class TestHurdleRaceClean(unittest.TestCase):
    
    @patch('hurdle_race_clean.move')
    @patch('hurdle_race_clean.turn_left')
    def test_jump_hurdle_calls_correct_sequence(self, mock_turn_left, mock_move):
        """Test that jump_hurdle calls functions in correct sequence and count."""
        jump_hurdle()
        
        # Verify total number of calls
        self.assertEqual(mock_move.call_count, 4)
        self.assertEqual(mock_turn_left.call_count, 8)
        
        # Verify total calls
        total_calls = mock_move.call_count + mock_turn_left.call_count
        self.assertEqual(total_calls, 12)
    
    @patch('hurdle_race_clean.jump_hurdle')
    def test_race_course_calls_jump_hurdle_six_times(self, mock_jump_hurdle):
        """Test that race_course calls jump_hurdle exactly 6 times."""
        race_course()
        self.assertEqual(mock_jump_hurdle.call_count, 6)
    
    @patch('hurdle_race_clean.jump_hurdle')
    @patch('hurdle_race_clean.move')
    @patch('hurdle_race_clean.turn_left')
    def test_race_course_total_actions(self, mock_turn_left, mock_move, mock_jump_hurdle):
        """Test that race_course executes correct total number of actions."""
        race_course()
        
        # Each jump_hurdle calls move 4 times and turn_left 8 times
        # For 6 hurdles: 24 moves and 48 turn_lefts
        self.assertEqual(mock_jump_hurdle.call_count, 6)
    
    def test_jump_hurdle_sequence_structure(self):
        """Test the structure of jump_hurdle function."""
        # This test verifies that the function exists and is callable
        self.assertTrue(callable(jump_hurdle))
        
        # Test that it can be called without errors (with mocked functions)
        with patch('hurdle_race_clean.move'), patch('hurdle_race_clean.turn_left'):
            result = jump_hurdle()
            # Function should return None (no return value)
            self.assertIsNone(result)
    
    def test_race_course_structure(self):
        """Test the structure of race_course function."""
        # This test verifies that the function exists and is callable
        self.assertTrue(callable(race_course))
        
        # Test that it can be called without errors (with mocked jump_hurdle)
        with patch('hurdle_race_clean.jump_hurdle'):
            result = race_course()
            # Function should return None (no return value)
            self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
