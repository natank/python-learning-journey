"""
Minimal Hurdle Race Implementation

Clean implementation without printing statements.
Assumes move() and turn_left() functions are already implemented.
"""

# These functions would be provided in the actual environment
def move():
    """Move the robot forward one step."""
    pass


def turn_left():
    """Turn the robot 90 degrees to the left."""
    pass


def jump_hurdle():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()


def race_course():
    for _ in range(6):
        jump_hurdle()


race_course()

