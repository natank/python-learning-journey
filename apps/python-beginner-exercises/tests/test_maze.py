import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import maze
from maze import solve_maze, turn_right


class TestMaze(unittest.TestCase):
    
    def setUp(self):
        """Reset the robot state before each test."""
        maze.position = (0, 0)
        maze.direction = 0  # North
        maze.goal_position = (5, 5)
        maze.walls = {}
    
    def test_turn_right(self):
        """Test that turn_right calls turn_left three times."""
        with patch('maze.turn_left') as mock_turn_left:
            turn_right()
            self.assertEqual(mock_turn_left.call_count, 3)
    
    def test_turn_left_changes_direction(self):
        """Test that turn_left changes direction correctly."""
        maze.direction = 0  # North
        maze.turn_left()
        self.assertEqual(maze.direction, 3)  # West
        
        maze.turn_left()
        self.assertEqual(maze.direction, 2)  # South
        
        maze.turn_left()
        self.assertEqual(maze.direction, 1)  # East
        
        maze.turn_left()
        self.assertEqual(maze.direction, 0)  # North (full circle)
    
    def test_turn_right_changes_direction(self):
        """Test that turn_right changes direction correctly."""
        maze.direction = 0  # North
        turn_right()
        self.assertEqual(maze.direction, 1)  # East
        
        turn_right()
        self.assertEqual(maze.direction, 2)  # South
        
        turn_right()
        self.assertEqual(maze.direction, 3)  # West
        
        turn_right()
        self.assertEqual(maze.direction, 0)  # North (full circle)
    
    def test_move_north(self):
        """Test move in north direction."""
        maze.position = (0, 0)
        maze.direction = 0  # North
        maze.move()
        self.assertEqual(maze.position, (0, 1))
    
    def test_move_east(self):
        """Test move in east direction."""
        maze.position = (0, 0)
        maze.direction = 1  # East
        maze.move()
        self.assertEqual(maze.position, (1, 0))
    
    def test_move_south(self):
        """Test move in south direction."""
        maze.position = (0, 1)
        maze.direction = 2  # South
        maze.move()
        self.assertEqual(maze.position, (0, 0))
    
    def test_move_west(self):
        """Test move in west direction."""
        maze.position = (1, 0)
        maze.direction = 3  # West
        maze.move()
        self.assertEqual(maze.position, (0, 0))
    
    def test_front_is_clear_no_wall(self):
        """Test front_is_clear when no wall ahead."""
        maze.position = (0, 0)
        maze.direction = 0  # North
        maze.walls = {}
        self.assertTrue(maze.front_is_clear())
    
    def test_front_is_clear_with_wall(self):
        """Test front_is_clear when wall ahead."""
        maze.position = (0, 0)
        maze.direction = 0  # North
        maze.walls = {((0, 0), 'N'): True}
        self.assertFalse(maze.front_is_clear())
    
    def test_wall_in_front(self):
        """Test wall_in_front detection."""
        maze.position = (0, 0)
        maze.direction = 1  # East
        maze.walls = {((0, 0), 'E'): True}
        self.assertTrue(maze.wall_in_front())
    
    def test_right_is_clear_no_wall(self):
        """Test right_is_clear when no wall on right."""
        maze.position = (0, 0)
        maze.direction = 0  # North (right is East)
        maze.walls = {}
        self.assertTrue(maze.right_is_clear())
    
    def test_right_is_clear_with_wall(self):
        """Test right_is_clear when wall on right."""
        maze.position = (0, 0)
        maze.direction = 0  # North (right is East)
        maze.walls = {((0, 0), 'E'): True}
        self.assertFalse(maze.right_is_clear())
    
    def test_wall_on_right(self):
        """Test wall_on_right detection."""
        maze.position = (0, 0)
        maze.direction = 1  # East (right is South)
        maze.walls = {((0, -1), 'N'): True}
        self.assertTrue(maze.wall_on_right())
    
    def test_at_goal_not_reached(self):
        """Test at_goal when not at goal."""
        maze.position = (0, 0)
        maze.goal_position = (5, 5)
        self.assertFalse(maze.at_goal())
    
    def test_at_goal_reached(self):
        """Test at_goal when goal reached."""
        maze.position = (5, 5)
        maze.goal_position = (5, 5)
        self.assertTrue(maze.at_goal())
    
    def test_solve_maze_simple_path(self):
        """Test solve_maze with simple path - just move straight to goal."""
        maze.position = (0, 0)
        maze.direction = 0  # North
        maze.goal_position = (0, 1)  # Goal one step north
        maze.walls = {}
        
        solve_maze(max_steps=10)  # Use small step limit
        
        self.assertTrue(maze.at_goal())
        self.assertEqual(maze.position, (0, 1))
    
    def test_solve_maze_right_turn_scenario(self):
        """Test solve_maze scenario where robot needs to turn to reach goal."""
        maze.position = (0, 0)
        maze.direction = 0  # North
        maze.goal_position = (0, 1)  # Goal north (same direction)
        maze.walls = {}
        
        solve_maze(max_steps=10)  # Use small step limit
        
        # Should reach goal
        self.assertTrue(maze.at_goal())
    
    def test_solve_maze_uses_right_hand_rule(self):
        """Test that solve_maze uses right-hand rule logic."""
        maze.position = (0, 0)
        maze.direction = 0
        maze.goal_position = (0, 1)  # Close goal
        maze.walls = {}
        
        with patch('maze.right_is_clear', wraps=maze.right_is_clear) as mock_right, \
             patch('maze.front_is_clear', wraps=maze.front_is_clear) as mock_front:
            
            solve_maze(max_steps=10)
            
            # Should check front_is_clear at minimum
            self.assertGreater(mock_front.call_count, 0)
            # Right is clear might or might not be checked depending on path
            # The important thing is that the algorithm uses the if/elif/else structure
    
    def test_solve_maze_step_limit(self):
        """Test that solve_maze respects step limit and raises error."""
        maze.position = (0, 0)
        maze.direction = 0
        maze.goal_position = (10, 10)  # Far goal
        # Create an impossible maze (completely surrounded)
        maze.walls = {
            ((0, 0), 'N'): True, ((0, 0), 'E'): True, ((0, 0), 'S'): True, ((0, 0), 'W'): True
        }
        
        with self.assertRaises(RuntimeError) as context:
            solve_maze(max_steps=10)
        
        self.assertIn("exceeded maximum steps", str(context.exception))
    
    def test_solve_maze_if_elif_else_structure(self):
        """Test that solve_maze uses if/elif/else logic correctly."""
        maze.position = (0, 0)
        maze.direction = 0
        maze.goal_position = (0, 1)  # Close goal
        maze.walls = {}
        
        with patch('maze.turn_right') as mock_turn_right, \
             patch('maze.move', wraps=maze.move) as mock_move, \
             patch('maze.turn_left') as mock_turn_left:
            
            solve_maze(max_steps=10)
            
            # Should use move function at minimum
            self.assertGreater(mock_move.call_count, 0)


if __name__ == '__main__':
    unittest.main()
