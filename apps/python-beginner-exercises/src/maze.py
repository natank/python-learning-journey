"""
Maze Solver - Right-Hand Rule Algorithm

Reeborg navigates through a dark maze using the right-hand rule:
1. Turn right if possible
2. Go straight if can't turn right
3. Turn left as a last resort

This algorithm ensures Reeborg follows the right edge of the maze to find the exit.

Available functions:
- move() - move forward one step
- turn_left() - turn 90 degrees left
- front_is_clear() - returns True if no wall in front
- wall_in_front() - returns True if wall in front
- right_is_clear() - returns True if no wall on right
- wall_on_right() - returns True if wall on right
- at_goal() - returns True if at the goal position
"""

# Mock functions (would be provided in actual Reeborg environment)
position = (0, 0)
direction = 0  # 0=North, 1=East, 2=South, 3=West
goal_position = (5, 5)
walls = {
    ((0, 0), 'E'): True,
    ((1, 0), 'N'): True,
    ((2, 0), 'E'): True,
}

def move():
    """Move the robot forward one step in current direction."""
    global position, direction
    x, y = position
    if direction == 0:  # North
        position = (x, y + 1)
    elif direction == 1:  # East
        position = (x + 1, y)
    elif direction == 2:  # South
        position = (x, y - 1)
    elif direction == 3:  # West
        position = (x - 1, y)

def turn_left():
    """Turn the robot 90 degrees to the left."""
    global direction
    direction = (direction - 1) % 4


def front_is_clear():
    """Check if the path in front is clear (no wall)."""
    global position, direction, walls
    x, y = position
    
    # Check for wall in front based on current direction
    if direction == 0:  # North
        return ((x, y), 'N') not in walls
    elif direction == 1:  # East
        return ((x, y), 'E') not in walls
    elif direction == 2:  # South
        return ((x, y - 1), 'N') not in walls
    elif direction == 3:  # West
        return ((x - 1, y), 'E') not in walls
    return True

def wall_in_front():
    """Check if there is a wall in front."""
    return not front_is_clear()

def right_is_clear():
    """Check if the right side is clear (no wall)."""
    global position, direction, walls
    x, y = position
    
    # Check for wall on right based on current direction
    if direction == 0:  # North, right is East
        return ((x, y), 'E') not in walls
    elif direction == 1:  # East, right is South
        return ((x, y - 1), 'N') not in walls
    elif direction == 2:  # South, right is West
        return ((x - 1, y), 'E') not in walls
    elif direction == 3:  # West, right is North
        return ((x, y), 'N') not in walls
    return True

def wall_on_right():
    """Check if there is a wall on the right."""
    return not right_is_clear()

def at_goal():
    """Check if robot has reached the goal."""
    return position == goal_position

def turn_right():
    """Turn 90 degrees right by turning left three times."""
    turn_left()
    turn_left()
    turn_left()

def solve_maze(max_steps=1000):
    """
    Solve the maze using the right-hand rule algorithm.
    
    Strategy:
    1. If front is clear, move straight (prefer straight path)
    2. Elif right is clear, turn right and move
    3. Else turn left (and repeat until can move)
    
    This is a modified right-hand rule that works better in open spaces.
    
    Args:
        max_steps: Maximum number of steps to prevent infinite loops
    """
    steps = 0
    while not at_goal() and steps < max_steps:
        if front_is_clear():
            # Priority 1: Go straight if path is clear
            move()
        elif right_is_clear():
            # Priority 2: Turn right if can't go straight
            turn_right()
            move()
        else:
            # Priority 3: Turn left as last resort
            turn_left()
        steps += 1
    
    if steps >= max_steps and not at_goal():
        raise RuntimeError(f"Maze solver exceeded maximum steps ({max_steps}) without reaching goal")


if __name__ == "__main__":
    solve_maze()
