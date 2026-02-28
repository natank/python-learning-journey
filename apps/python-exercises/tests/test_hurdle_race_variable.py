import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import hurdle_race_variable
from hurdle_race_variable import jump_hurdle, run_race, turn_right


class TestHurdleRaceVariable(unittest.TestCase):
    
    def setUp(self):
        """Reset the robot state before each test."""
        hurdle_race_variable.position = 0
        hurdle_race_variable.goal_position = 14
        hurdle_race_variable.hurdles = [2, 5, 8, 11]
    
    def test_turn_right(self):
        """Test that turn_right calls turn_left three times."""
        with patch('hurdle_race_variable.turn_left') as mock_turn_left:
            turn_right()
            self.assertEqual(mock_turn_left.call_count, 3)
    
    def test_jump_hurdle_sequence(self):
        """Test that jump_hurdle calls functions in correct sequence."""
        with patch('hurdle_race_variable.move') as mock_move, \
             patch('hurdle_race_variable.turn_left') as mock_turn_left:
            
            jump_hurdle()
            
            # Should call turn_left 4 times total (1 + 3 for turn_right twice + 1)
            # turn_left, turn_right (3x turn_left), turn_right (3x turn_left), turn_left
            self.assertEqual(mock_turn_left.call_count, 8)
            
            # Should call move 3 times
            self.assertEqual(mock_move.call_count, 3)
    
    def test_front_is_clear_no_hurdle(self):
        """Test front_is_clear returns True when no hurdle ahead."""
        hurdle_race_variable.position = 0
        self.assertTrue(hurdle_race_variable.front_is_clear())
        
        hurdle_race_variable.position = 1
        self.assertTrue(hurdle_race_variable.front_is_clear())
    
    def test_front_is_clear_with_hurdle(self):
        """Test front_is_clear returns False when hurdle ahead."""
        hurdle_race_variable.position = 2
        self.assertFalse(hurdle_race_variable.front_is_clear())
        
        hurdle_race_variable.position = 5
        self.assertFalse(hurdle_race_variable.front_is_clear())
    
    def test_wall_in_front_no_hurdle(self):
        """Test wall_in_front returns False when no hurdle."""
        hurdle_race_variable.position = 0
        self.assertFalse(hurdle_race_variable.wall_in_front())
        
        hurdle_race_variable.position = 3
        self.assertFalse(hurdle_race_variable.wall_in_front())
    
    def test_wall_in_front_with_hurdle(self):
        """Test wall_in_front returns True when hurdle present."""
        hurdle_race_variable.position = 2
        self.assertTrue(hurdle_race_variable.wall_in_front())
        
        hurdle_race_variable.position = 8
        self.assertTrue(hurdle_race_variable.wall_in_front())
    
    def test_at_goal_not_reached(self):
        """Test at_goal returns False when not at goal."""
        hurdle_race_variable.position = 0
        self.assertFalse(hurdle_race_variable.at_goal())
        
        hurdle_race_variable.position = 10
        self.assertFalse(hurdle_race_variable.at_goal())
    
    def test_at_goal_reached(self):
        """Test at_goal returns True when goal reached."""
        hurdle_race_variable.position = 14
        self.assertTrue(hurdle_race_variable.at_goal())
        
        hurdle_race_variable.position = 15
        self.assertTrue(hurdle_race_variable.at_goal())
    
    def test_move_increments_position(self):
        """Test that move increments position."""
        hurdle_race_variable.position = 0
        hurdle_race_variable.move()
        self.assertEqual(hurdle_race_variable.position, 1)
        
        hurdle_race_variable.move()
        self.assertEqual(hurdle_race_variable.position, 2)
    
    def test_run_race_completes(self):
        """Test that run_race reaches the goal."""
        hurdle_race_variable.position = 0
        hurdle_race_variable.goal_position = 14
        hurdle_race_variable.hurdles = [2, 5, 8, 11]
        
        run_race()
        
        self.assertTrue(hurdle_race_variable.at_goal())
        self.assertGreaterEqual(hurdle_race_variable.position, 14)
    
    def test_run_race_no_hurdles(self):
        """Test run_race with no hurdles."""
        hurdle_race_variable.position = 0
        hurdle_race_variable.goal_position = 5
        hurdle_race_variable.hurdles = []
        
        run_race()
        
        self.assertTrue(hurdle_race_variable.at_goal())
        self.assertEqual(hurdle_race_variable.position, 5)
    
    def test_run_race_all_hurdles(self):
        """Test run_race with hurdles at every position."""
        hurdle_race_variable.position = 0
        hurdle_race_variable.goal_position = 4
        hurdle_race_variable.hurdles = [0, 1, 2, 3]
        
        run_race()
        
        self.assertTrue(hurdle_race_variable.at_goal())
        self.assertGreaterEqual(hurdle_race_variable.position, 4)
    
    def test_run_race_single_hurdle(self):
        """Test run_race with a single hurdle."""
        hurdle_race_variable.position = 0
        hurdle_race_variable.goal_position = 5
        hurdle_race_variable.hurdles = [2]
        
        run_race()
        
        self.assertTrue(hurdle_race_variable.at_goal())
        self.assertGreaterEqual(hurdle_race_variable.position, 5)
    
    def test_run_race_uses_conditionals(self):
        """Test that run_race uses conditional logic."""
        hurdle_race_variable.position = 0
        hurdle_race_variable.goal_position = 10
        hurdle_race_variable.hurdles = [2, 6]
        
        with patch('hurdle_race_variable.move', wraps=hurdle_race_variable.move) as mock_move, \
             patch('hurdle_race_variable.jump_hurdle', wraps=jump_hurdle) as mock_jump:
            
            run_race()
            
            # Should call move for clear positions and jump_hurdle for hurdles
            self.assertGreater(mock_move.call_count, 0)
            self.assertEqual(mock_jump.call_count, 2)  # 2 hurdles at positions 2 and 6
    
    def test_run_race_different_goal_positions(self):
        """Test run_race with different goal positions."""
        test_cases = [
            (10, [2, 5]),
            (20, [3, 7, 11, 15]),
            (5, [1]),
        ]
        
        for goal, hurdles in test_cases:
            with self.subTest(goal=goal, hurdles=hurdles):
                hurdle_race_variable.position = 0
                hurdle_race_variable.goal_position = goal
                hurdle_race_variable.hurdles = hurdles
                
                run_race()
                
                self.assertTrue(hurdle_race_variable.at_goal())
                self.assertGreaterEqual(hurdle_race_variable.position, goal)


if __name__ == '__main__':
    unittest.main()
