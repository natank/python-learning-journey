import random


def select_bill_payer(friends):
    """
    Randomly select who will pay the bill from a list of friends.
    
    Args:
        friends (list): A list of friend names (strings)
        
    Returns:
        str: The name of the friend who will pay the bill
        
    Raises:
        ValueError: If friends list is empty or not a list
    """
    if not isinstance(friends, list):
        raise ValueError("Friends must be provided as a list")
    
    if not friends:
        raise ValueError("Friends list cannot be empty")
    
    # Filter out empty strings and None values
    valid_friends = [friend for friend in friends if friend and isinstance(friend, str)]
    
    if not valid_friends:
        raise ValueError("Friends list must contain valid names")
    
    chosen_friend = random.choice(valid_friends)
    print(f"{chosen_friend} will pay the bill!")
    return chosen_friend


def main():
    """
    Example usage of the bill payer selector.
    """
    friends = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    select_bill_payer(friends)


if __name__ == "__main__":
    main()
