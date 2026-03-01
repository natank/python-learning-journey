import pytest
from src.string_utils import reverse_string, is_palindrome, count_vowels, capitalize_words

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("Racecar") == True  # Case insensitive
    assert is_palindrome("A man a plan a canal Panama") == True  # Spaces ignored
    assert is_palindrome("hello") == False

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("bcdfg") == 0
    assert count_vowels("") == 0

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python exercises") == "Python Exercises"
    assert capitalize_words("") == ""
    assert capitalize_words("single") == "Single"
