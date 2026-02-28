"""
Variable Hurdle Race Implementation

This version handles hurdles at variable positions using conditional logic.
The robot must navigate to the goal, jumping over hurdles when encountered.

Available functions:
- move() - move forward one step
- turn_left() - turn 90 degrees left
- front_is_clear() - returns True if no wall in front
- wall_in_front() - returns True if wall in front
- at_goal() - returns True if at the goal position
"""

# Mock functions (would be provided in actual environment)
position = 0
goal_position = 14
hurdles = [2, 5, 8, 11]  # Example hurdle positions

def move():
    """Move the robot forward one step."""
    global position
    position += 1

def turn_left():
    """Turn the robot 90 degrees to the left."""
    pass

def front_is_clear():
    """Check if the path in front is clear."""
    return position not in hurdles

def wall_in_front():
    """Check if there is a wall in front."""
    return position in hurdles

def at_goal():
    """Check if robot has reached the goal."""
    return position >= goal_position


def turn_right():
    """Turn right by turning left three times."""
    turn_left()
    turn_left()
    turn_left()


def jump_hurdle():
    """Jump over a single hurdle."""
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def run_race():
    """
    Navigate the race course, jumping hurdles when encountered.
    Uses while loop and conditionals to handle variable hurdle positions.
    """
    while not at_goal():
        if front_is_clear():
            move()
        else:
            jump_hurdle()


if __name__ == "__main__":
    run_race()
