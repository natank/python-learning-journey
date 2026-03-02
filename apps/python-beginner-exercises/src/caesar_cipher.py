def caesar_encoder(text: str, shift: int) -> str:
    """
    Encode text using Caesar cipher by shifting each letter forward by shift amount.
    
    Args:
        text: The text to encode
        shift: Number of positions to shift letters forward (1-25)
    
    Returns:
        The encoded text
    """
    result = []
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Calculate shifted position (wrap around using modulo 26)
            shifted_pos = (ord(char) - start + shift) % 26
            # Convert back to character
            result.append(chr(start + shifted_pos))
        else:
            # Keep non-alphabetic characters unchanged
            result.append(char)
    
    return ''.join(result)


def caesar_decoder(text: str, shift: int) -> str:
    """
    Decode text using Caesar cipher by shifting each letter backward by shift amount.
    
    Args:
        text: The text to decode
        shift: Number of positions to shift letters backward (1-25)
    
    Returns:
        The decoded text
    """
    result = []
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Calculate shifted position (wrap around using modulo 26)
            shifted_pos = (ord(char) - start - shift) % 26
            # Convert back to character
            result.append(chr(start + shifted_pos))
        else:
            # Keep non-alphabetic characters unchanged
            result.append(char)
    
    return ''.join(result)


def caesar_cli():
    """
    Command-line interface for testing Caesar cipher functions.
    """
    print("=== Caesar Cipher Tool ===")
    print("1. Encode text")
    print("2. Decode text")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '3':
            print("Goodbye!")
            break
        elif choice in ['1', '2']:
            text = input("Enter text: ").strip()
            
            while True:
                try:
                    shift = int(input("Enter shift amount (1-25): ").strip())
                    if 1 <= shift <= 25:
                        break
                    else:
                        print("Shift must be between 1 and 25")
                except ValueError:
                    print("Please enter a valid number")
            
            if choice == '1':
                result = caesar_encoder(text, shift)
                print(f"Encoded: {result}")
            else:
                result = caesar_decoder(text, shift)
                print(f"Decoded: {result}")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    caesar_cli()
