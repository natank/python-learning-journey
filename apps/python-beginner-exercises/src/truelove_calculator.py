def calculate_truelove_score(name1: str, name2: str) -> int:
    """
    Calculate a compatibility score based on two names.
    
    The score is a two-digit number where:
    - First digit represents the count of letters from "TRUE" in both names
    - Second digit represents the count of letters from "LOVE" in both names
    
    Args:
        name1: First name
        name2: Second name
        
    Returns:
        Two-digit integer score (e.g., 23, 45, etc.)
    """
    # Combine both names and convert to uppercase for case-insensitive counting
    combined_names = (name1 + name2).upper()
    
    # Count letters from "TRUE"
    true_count = 0
    for letter in "TRUE":
        true_count += combined_names.count(letter)
    
    # Count letters from "LOVE"
    love_count = 0
    for letter in "LOVE":
        love_count += combined_names.count(letter)
    
    # Combine into two-digit score
    return int(f"{true_count}{love_count}")


def play_truelove_game():
    """
    Interactive True Love Calculator game.
    """
    print("💕 True Love Calculator 💕")
    print("=" * 40)
    print("Calculate the compatibility score between two names!")
    print("The score is based on letters from TRUE and LOVE in both names.")
    print()
    
    while True:
        try:
            # Get user input
            name1 = input("Enter first name (or 'quit' to exit): ").strip()
            if name1.lower() in ['quit', 'exit', 'q']:
                print("Thanks for playing! 💕")
                break
                
            name2 = input("Enter second name: ").strip()
            if not name2:
                print("Please enter a second name!")
                continue
            
            # Calculate score
            score = calculate_truelove_score(name1, name2)
            
            # Show result with fun message
            print(f"\n💝 {name1} + {name2} = {score}%")
            
            # Show breakdown
            combined = (name1 + name2).upper()
            true_letters = sum(combined.count(letter) for letter in "TRUE")
            love_letters = sum(combined.count(letter) for letter in "LOVE")
            print(f"   TRUE letters: {true_letters}, LOVE letters: {love_letters}")
            
            # Add fun interpretation
            if score >= 80:
                print("   💕 Perfect match! Made for each other!")
            elif score >= 60:
                print("   💗 Strong connection! Great compatibility!")
            elif score >= 40:
                print("   💚 Good potential! Worth exploring!")
            elif score >= 20:
                print("   💛 Some sparks! Give it a try!")
            else:
                print("   💙 Every love story starts somewhere!")
            
            print("\n" + "-" * 40 + "\n")
            
        except KeyboardInterrupt:
            print("\n\nThanks for playing! 💕")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again!\n")


if __name__ == "__main__":
    play_truelove_game()
