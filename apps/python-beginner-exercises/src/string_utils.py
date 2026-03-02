def reverse_string(s):
    """Reverse a string"""
    return s[::-1]

def is_palindrome(s):
    """Check if a string is a palindrome (ignoring case and spaces)"""
    cleaned = s.lower().replace(' ', '')
    return cleaned == cleaned[::-1]

def count_vowels(s):
    """Count vowels in a string"""
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char in vowels)

def capitalize_words(s):
    """Capitalize first letter of each word"""
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    # Test string utilities
    test_string = "hello world"
    print(f"Original: {test_string}")
    print(f"Reversed: {reverse_string(test_string)}")
    print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")
    print(f"Vowels in '{test_string}': {count_vowels(test_string)}")
    print(f"Capitalized: {capitalize_words(test_string)}")
