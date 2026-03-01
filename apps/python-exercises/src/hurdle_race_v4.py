"""
Hurdle Race Version 4 - Variable Position and Height

This version handles hurdles at variable positions with variable heights.
The robot must navigate to the goal, climbing over hurdles of any height.

This solution works for:
- Hurdles 1: Fixed positions, fixed height
- Hurdles 2: Fixed positions, fixed height  
- Hurdles 3: Variable positions, fixed height
- Hurdles 4: Variable positions, variable heights

Available functions:
- move() - move forward one step
- turn_left() - turn 90 degrees left
- front_is_clear() - returns True if no wall in front
- wall_in_front() - returns True if wall in front
- at_goal() - returns True if at the goal position
- right_is_clear() - returns True if no wall on right
- wall_on_right() - returns True if wall on right
"""

# Mock functions (would be provided in actual Reeborg environment)
position = 0
goal_position = 14
height = 0
hurdles = {2: 2, 5: 1, 8: 3, 11: 2}  # position: height mapping

def move():
    """Move the robot forward one step."""
    global position
    position += 1

def turn_left():
    """Turn the robot 90 degrees to the left."""
    pass

def front_is_clear():
    """Check if the path in front is clear (no wall)."""
    global position, height
    if height > 0:
        return True
    return position not in hurdles

def wall_in_front():
    """Check if there is a wall in front."""
    global position, height
    if height > 0:
        return False
    return position in hurdles

def at_goal():
    """Check if robot has reached the goal."""
    return position >= goal_position

def right_is_clear():
    """Check if the right side is clear."""
    global position, height
    if position in hurdles:
        return height >= hurdles[position]
    return True

def wall_on_right():
    """Check if there is a wall on the right."""
    return not right_is_clear()


def turn_right():
    """Turn 90 degrees right by turning left three times."""
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    """Turn 180 degrees."""
    turn_left()
    turn_left()


def climb_up():
    """
    Climb up the hurdle until we can move forward.
    Handles variable height hurdles.
    """
    turn_left()
    move()
    turn_right()


def climb_down():
    """
    Climb down the hurdle after clearing it.
    Descends until back on ground level.
    """
    turn_right()
    move()
    turn_left()


def jump_hurdle():
    """
    Jump over a hurdle of any height.
    Climbs up until top is reached, moves forward, then climbs down.
    """
    # Climb up the hurdle
    while wall_in_front():
        climb_up()
    
    # Move forward over the hurdle
    move()
    
    # Climb down the hurdle
    while right_is_clear() and not at_goal():
        climb_down()


def run_race():
    """
    Navigate the race course, jumping hurdles of variable heights.
    Uses while loop and conditionals to handle variable positions and heights.
    
    This solution works for all Hurdles worlds (1, 2, 3, and 4).
    """
    while not at_goal():
        if front_is_clear():
            move()
        else:
            jump_hurdle()


if __name__ == "__main__":
    run_race()
