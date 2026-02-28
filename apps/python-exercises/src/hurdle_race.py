"""
Hurdle Race Exercise

This module provides functions to solve a hurdle race problem using the built-in
functions move() and turn_left(). The robot needs to jump over 6 hurdles
following a specific sequence of movements.

Assumptions:
- move() and turn_left() functions are already implemented
- Robot starts facing the first hurdle
- Each hurdle requires the same sequence of movements to jump over
"""

# Mock functions for testing (in real scenario these would be provided)
def move():
    """Move the robot forward one step."""
    print("move()")
    pass


def turn_left():
    """Turn the robot 90 degrees to the left."""
    print("turn_left()")
    pass


def jump_hurdle():
    """
    Execute the sequence to jump over a single hurdle.
    
    The required sequence is:
    1. move() - approach hurdle
    2. turn_left() - turn to face hurdle
    3. move() - jump over hurdle
    4. turn_left() - turn left (3 times to complete 270 degrees)
    5. turn_left()
    6. turn_left()
    7. move() - move past hurdle
    8. turn_left() - turn left (3 times to complete 270 degrees)
    9. turn_left()
    10. turn_left()
    11. move() - position for next hurdle
    11. turn_left() - face forward again
    """
    # Approach and jump over hurdle
    move()
    turn_left()
    move()
    
    # Turn around (270 degrees left = 3 left turns)
    turn_left()
    turn_left()
    turn_left()
    
    # Move past hurdle
    move()
    
    # Turn around again (270 degrees left = 3 left turns)
    turn_left()
    turn_left()
    turn_left()
    
    # Position for next hurdle
    move()
    turn_left()


def race_course():
    """
    Complete the entire hurdle race course with 6 hurdles.
    
    This function calls jump_hurdle() 6 times to pass all hurdles
    with minimal code repetition using a loop.
    """
    print("🏃 Starting Hurdle Race with 6 hurdles!")
    print("=" * 50)
    
    for hurdle_num in range(1, 7):
        print(f"\n--- Jumping Hurdle {hurdle_num} ---")
        jump_hurdle()
        print(f"--- Hurdle {hurdle_num} completed ---")
    
    print("\n🎉 Hurdle Race Completed Successfully!")
    print("🏆 All 6 hurdles cleared!")


def race_course_no_loop():
    """
    Alternative implementation without using loops.
    This demonstrates the same logic but with explicit function calls.
    """
    print("🏃 Starting Hurdle Race with 6 hurdles (No Loop Version)!")
    print("=" * 50)
    
    print("\n--- Jumping Hurdle 1 ---")
    jump_hurdle()
    print("--- Hurdle 1 completed ---")
    
    print("\n--- Jumping Hurdle 2 ---")
    jump_hurdle()
    print("--- Hurdle 2 completed ---")
    
    print("\n--- Jumping Hurdle 3 ---")
    jump_hurdle()
    print("--- Hurdle 3 completed ---")
    
    print("\n--- Jumping Hurdle 4 ---")
    jump_hurdle()
    print("--- Hurdle 4 completed ---")
    
    print("\n--- Jumping Hurdle 5 ---")
    jump_hurdle()
    print("--- Hurdle 5 completed ---")
    
    print("\n--- Jumping Hurdle 6 ---")
    jump_hurdle()
    print("--- Hurdle 6 completed ---")
    
    print("\n🎉 Hurdle Race Completed Successfully!")
    print("🏆 All 6 hurdles cleared!")


def get_jump_sequence():
    """
    Return the sequence of function calls needed to jump one hurdle.
    This is useful for understanding the pattern and for testing.
    
    Returns:
        list: List of function names in order
    """
    return [
        "move",        # approach hurdle
        "turn_left",   # turn to face hurdle
        "move",        # jump over hurdle
        "turn_left",   # start turning around
        "turn_left",   # continue turning
        "turn_left",   # complete 270 degree turn
        "move",        # move past hurdle
        "turn_left",   # start turning back
        "turn_left",   # continue turning
        "turn_left",   # complete 270 degree turn
        "move",        # position for next hurdle
        "turn_left"    # face forward again
    ]


def main():
    """
    Main function to demonstrate the hurdle race solution.
    """
    print("🤖 Hurdle Race Exercise")
    print("=" * 30)
    print("This program demonstrates how to pass 6 hurdles")
    print("using only move() and turn_left() functions.")
    print()
    
    print("Jump sequence for one hurdle:")
    sequence = get_jump_sequence()
    for i, action in enumerate(sequence, 1):
        print(f"{i:2d}. {action}()")
    
    print(f"\nTotal actions per hurdle: {len(sequence)}")
    print(f"Total actions for 6 hurdles: {len(sequence) * 6}")
    
    print("\n" + "=" * 50)
    print("Executing the race course:")
    race_course()


if __name__ == "__main__":
    main()
