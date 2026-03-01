import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import hurdle_race_v4
from hurdle_race_v4 import (
    jump_hurdle, run_race, climb_up, climb_down, turn_around
)


class TestHurdleRaceV4(unittest.TestCase):
    
    def setUp(self):
        """Reset the robot state before each test."""
        hurdle_race_v4.position = 0
        hurdle_race_v4.height = 0
        hurdle_race_v4.goal_position = 14
        hurdle_race_v4.hurdles = {2: 2, 5: 1, 8: 3, 11: 2}
    
    def test_turn_around(self):
        """Test that turn_around calls turn_left twice."""
        with patch('hurdle_race_v4.turn_left') as mock_turn_left:
            turn_around()
            self.assertEqual(mock_turn_left.call_count, 2)
    
    def test_climb_up_sequence(self):
        """Test that climb_up calls functions in correct sequence."""
        with patch('hurdle_race_v4.move') as mock_move, \
             patch('hurdle_race_v4.turn_left') as mock_turn_left:
            
            climb_up()
            
            # Should call turn_left 4 times (1 + 3)
            self.assertEqual(mock_turn_left.call_count, 4)
            # Should call move once
            self.assertEqual(mock_move.call_count, 1)
    
    def test_climb_down_sequence(self):
        """Test that climb_down calls functions in correct sequence."""
        with patch('hurdle_race_v4.move') as mock_move, \
             patch('hurdle_race_v4.turn_left') as mock_turn_left:
            
            climb_down()
            
            # Should call turn_left 4 times (3 + 1)
            self.assertEqual(mock_turn_left.call_count, 4)
            # Should call move once
            self.assertEqual(mock_move.call_count, 1)
    
    def test_front_is_clear_no_hurdle(self):
        """Test front_is_clear returns True when no hurdle ahead."""
        hurdle_race_v4.position = 0
        hurdle_race_v4.height = 0
        self.assertTrue(hurdle_race_v4.front_is_clear())
        
        hurdle_race_v4.position = 1
        self.assertTrue(hurdle_race_v4.front_is_clear())
    
    def test_front_is_clear_with_hurdle(self):
        """Test front_is_clear returns False when hurdle ahead."""
        hurdle_race_v4.position = 2
        hurdle_race_v4.height = 0
        self.assertFalse(hurdle_race_v4.front_is_clear())
        
        hurdle_race_v4.position = 5
        hurdle_race_v4.height = 0
        self.assertFalse(hurdle_race_v4.front_is_clear())
    
    def test_front_is_clear_when_elevated(self):
        """Test front_is_clear returns True when robot is elevated."""
        hurdle_race_v4.position = 2
        hurdle_race_v4.height = 1
        self.assertTrue(hurdle_race_v4.front_is_clear())
    
    def test_wall_in_front_no_hurdle(self):
        """Test wall_in_front returns False when no hurdle."""
        hurdle_race_v4.position = 0
        hurdle_race_v4.height = 0
        self.assertFalse(hurdle_race_v4.wall_in_front())
    
    def test_wall_in_front_with_hurdle(self):
        """Test wall_in_front returns True when hurdle present."""
        hurdle_race_v4.position = 2
        hurdle_race_v4.height = 0
        self.assertTrue(hurdle_race_v4.wall_in_front())
    
    def test_wall_in_front_when_elevated(self):
        """Test wall_in_front returns False when robot is elevated."""
        hurdle_race_v4.position = 2
        hurdle_race_v4.height = 1
        self.assertFalse(hurdle_race_v4.wall_in_front())
    
    def test_at_goal_not_reached(self):
        """Test at_goal returns False when not at goal."""
        hurdle_race_v4.position = 0
        self.assertFalse(hurdle_race_v4.at_goal())
        
        hurdle_race_v4.position = 10
        self.assertFalse(hurdle_race_v4.at_goal())
    
    def test_at_goal_reached(self):
        """Test at_goal returns True when goal reached."""
        hurdle_race_v4.position = 14
        self.assertTrue(hurdle_race_v4.at_goal())
        
        hurdle_race_v4.position = 15
        self.assertTrue(hurdle_race_v4.at_goal())
    
    def test_right_is_clear_no_hurdle(self):
        """Test right_is_clear when not at hurdle."""
        hurdle_race_v4.position = 0
        hurdle_race_v4.height = 0
        self.assertTrue(hurdle_race_v4.right_is_clear())
    
    def test_right_is_clear_at_hurdle_top(self):
        """Test right_is_clear when at top of hurdle."""
        hurdle_race_v4.position = 2
        hurdle_race_v4.height = 2
        self.assertTrue(hurdle_race_v4.right_is_clear())
    
    def test_wall_on_right_at_hurdle_base(self):
        """Test wall_on_right when at base of hurdle."""
        hurdle_race_v4.position = 2
        hurdle_race_v4.height = 0
        self.assertTrue(hurdle_race_v4.wall_on_right())
    
    def test_move_increments_position(self):
        """Test that move increments position."""
        hurdle_race_v4.position = 0
        hurdle_race_v4.move()
        self.assertEqual(hurdle_race_v4.position, 1)
    
    def test_run_race_completes(self):
        """Test that run_race reaches the goal."""
        hurdle_race_v4.position = 0
        hurdle_race_v4.height = 0
        hurdle_race_v4.goal_position = 14
        hurdle_race_v4.hurdles = {2: 2, 5: 1, 8: 3, 11: 2}
        
        run_race()
        
        self.assertTrue(hurdle_race_v4.at_goal())
        self.assertGreaterEqual(hurdle_race_v4.position, 14)
    
    def test_run_race_no_hurdles(self):
        """Test run_race with no hurdles (Hurdles 1 compatibility)."""
        hurdle_race_v4.position = 0
        hurdle_race_v4.height = 0
        hurdle_race_v4.goal_position = 5
        hurdle_race_v4.hurdles = {}
        
        run_race()
        
        self.assertTrue(hurdle_race_v4.at_goal())
        self.assertEqual(hurdle_race_v4.position, 5)
    
    def test_run_race_fixed_height_hurdles(self):
        """Test run_race with fixed height hurdles (Hurdles 3 compatibility)."""
        hurdle_race_v4.position = 0
        hurdle_race_v4.height = 0
        hurdle_race_v4.goal_position = 10
        hurdle_race_v4.hurdles = {2: 1, 5: 1, 8: 1}
        
        run_race()
        
        self.assertTrue(hurdle_race_v4.at_goal())
        self.assertGreaterEqual(hurdle_race_v4.position, 10)
    
    def test_run_race_variable_height_hurdles(self):
        """Test run_race with variable height hurdles (Hurdles 4)."""
        hurdle_race_v4.position = 0
        hurdle_race_v4.height = 0
        hurdle_race_v4.goal_position = 12
        hurdle_race_v4.hurdles = {2: 1, 5: 3, 8: 2}
        
        run_race()
        
        self.assertTrue(hurdle_race_v4.at_goal())
        self.assertGreaterEqual(hurdle_race_v4.position, 12)
    
    def test_run_race_tall_hurdle(self):
        """Test run_race with a very tall hurdle."""
        hurdle_race_v4.position = 0
        hurdle_race_v4.height = 0
        hurdle_race_v4.goal_position = 5
        hurdle_race_v4.hurdles = {2: 5}
        
        run_race()
        
        self.assertTrue(hurdle_race_v4.at_goal())
        self.assertGreaterEqual(hurdle_race_v4.position, 5)
    
    def test_run_race_different_configurations(self):
        """Test run_race with different hurdle configurations."""
        test_cases = [
            (10, {2: 1, 5: 2}),
            (15, {3: 2, 7: 1, 11: 3}),
            (8, {2: 4}),
            (20, {2: 1, 5: 2, 8: 1, 11: 3, 14: 2, 17: 1}),
        ]
        
        for goal, hurdles in test_cases:
            with self.subTest(goal=goal, hurdles=hurdles):
                hurdle_race_v4.position = 0
                hurdle_race_v4.height = 0
                hurdle_race_v4.goal_position = goal
                hurdle_race_v4.hurdles = hurdles
                
                run_race()
                
                self.assertTrue(hurdle_race_v4.at_goal())
                self.assertGreaterEqual(hurdle_race_v4.position, goal)


if __name__ == '__main__':
    unittest.main()
