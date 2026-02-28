"""
Python Exercises Package

A collection of practice exercises for learning Python concepts including:
- Basic arithmetic operations
- String manipulation utilities
- Data structure implementations
"""

from .calculator import add, subtract, multiply, divide
from .string_utils import reverse_string, is_palindrome, count_vowels, capitalize_words
from .data_structures import Stack, Queue
from .coin_flip import flip_coin, flip_and_print, flip_multiple_times

__all__ = [
    'add', 'subtract', 'multiply', 'divide',
    'reverse_string', 'is_palindrome', 'count_vowels', 'capitalize_words',
    'Stack', 'Queue',
    'flip_coin', 'flip_and_print', 'flip_multiple_times'
]
