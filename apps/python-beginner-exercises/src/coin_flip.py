import random

def flip_coin():
    """
    Simulate a coin flip and return 'Heads' or 'Tails'
    
    Returns:
        str: 'Heads' or 'Tails'
    """
    result = random.choice(['Heads', 'Tails'])
    return result

def flip_and_print():
    """
    Flip a coin and print the result
    """
    result = flip_coin()
    print(result)
    return result

def flip_multiple_times(count):
    """
    Flip a coin multiple times and return results
    
    Args:
        count (int): Number of times to flip the coin
        
    Returns:
        list: List of 'Heads' or 'Tails' results
    """
    results = []
    for _ in range(count):
        results.append(flip_coin())
    return results

if __name__ == '__main__':
    # Test the coin flip when run directly
    print("Coin Flip Simulation:")
    print(f"Single flip: {flip_and_print()}")
    
    # Flip 5 times
    results = flip_multiple_times(5)
    print(f"5 flips: {results}")
    
    # Count results
    heads_count = results.count('Heads')
    tails_count = results.count('Tails')
    print(f"Heads: {heads_count}, Tails: {tails_count}")
