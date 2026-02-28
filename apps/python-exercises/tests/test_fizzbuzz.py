import unittest
from unittest.mock import patch
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from fizzbuzz import fizzbuzz, fizzbuzz_range, print_fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    
    def test_fizzbuzz_divisible_by_3(self):
        """Test numbers divisible by 3 return Fizz."""
        test_numbers = [3, 6, 9, 12, 18, 21, 24, 27, 33, 36, 39, 42, 48, 51, 54, 57, 63, 66, 69, 72, 78, 81, 84, 87, 93, 96, 99]
        for num in test_numbers:
            with self.subTest(number=num):
                result = fizzbuzz(num)
                self.assertEqual(result, "Fizz")
    
    def test_fizzbuzz_divisible_by_5(self):
        """Test numbers divisible by 5 return Buzz."""
        test_numbers = [5, 10, 20, 25, 35, 40, 50, 55, 65, 70, 80, 85, 95, 100]
        for num in test_numbers:
            with self.subTest(number=num):
                result = fizzbuzz(num)
                self.assertEqual(result, "Buzz")
    
    def test_fizzbuzz_divisible_by_both_3_and_5(self):
        """Test numbers divisible by both 3 and 5 return FizzBuzz."""
        test_numbers = [15, 30, 45, 60, 75, 90]
        for num in test_numbers:
            with self.subTest(number=num):
                result = fizzbuzz(num)
                self.assertEqual(result, "FizzBuzz")
    
    def test_fizzbuzz_regular_numbers(self):
        """Test regular numbers return as string."""
        test_numbers = [1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19, 22, 23, 26, 28, 29, 31, 32, 34, 37, 38, 41, 43, 44, 46, 47, 49, 52, 53, 56, 58, 59, 61, 62, 64, 67, 68, 71, 73, 74, 76, 77, 79, 82, 83, 86, 88, 89, 91, 92, 94, 97, 98]
        for num in test_numbers:
            with self.subTest(number=num):
                result = fizzbuzz(num)
                self.assertEqual(result, str(num))
    
    def test_fizzbuzz_invalid_input_not_integer(self):
        """Test that non-integer input raises ValueError."""
        invalid_inputs = [3.5, "3", None, [3], {"number": 3}]
        for invalid_input in invalid_inputs:
            with self.subTest(input=invalid_input):
                with self.assertRaises(ValueError) as context:
                    fizzbuzz(invalid_input)
                self.assertEqual(str(context.exception), "Input must be an integer")
    
    def test_fizzbuzz_invalid_input_non_positive(self):
        """Test that non-positive integers raise ValueError."""
        invalid_inputs = [0, -1, -5, -10]
        for invalid_input in invalid_inputs:
            with self.subTest(input=invalid_input):
                with self.assertRaises(ValueError) as context:
                    fizzbuzz(invalid_input)
                self.assertEqual(str(context.exception), "Input must be a positive integer")
    
    def test_fizzbuzz_range_default(self):
        """Test default range (1-100)."""
        result = fizzbuzz_range()
        self.assertEqual(len(result), 100)
        self.assertEqual(result[0], "1")  # 1
        self.assertEqual(result[2], "Fizz")  # 3
        self.assertEqual(result[4], "Buzz")  # 5
        self.assertEqual(result[14], "FizzBuzz")  # 15
        self.assertEqual(result[98], "Fizz")  # 99
        self.assertEqual(result[99], "Buzz")  # 100
    
    def test_fizzbuzz_range_custom(self):
        """Test custom range."""
        result = fizzbuzz_range(1, 15)
        self.assertEqual(len(result), 15)
        expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
        self.assertEqual(result, expected)
    
    def test_fizzbuzz_range_single_number(self):
        """Test range with single number."""
        result = fizzbuzz_range(5, 5)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "Buzz")
    
    def test_fizzbuzz_range_invalid_start_end_not_integers(self):
        """Test invalid start/end types."""
        invalid_pairs = [(1.5, 10), ("1", 10), (1, "10"), (None, 10), (1, None)]
        for start, end in invalid_pairs:
            with self.subTest(start=start, end=end):
                with self.assertRaises(ValueError) as context:
                    fizzbuzz_range(start, end)
                self.assertEqual(str(context.exception), "Start and end must be integers")
    
    def test_fizzbuzz_range_invalid_non_positive(self):
        """Test non-positive start/end values."""
        invalid_pairs = [(0, 10), (-1, 10), (1, 0), (1, -5), (-5, -1)]
        for start, end in invalid_pairs:
            with self.subTest(start=start, end=end):
                with self.assertRaises(ValueError) as context:
                    fizzbuzz_range(start, end)
                self.assertEqual(str(context.exception), "Start and end must be positive integers")
    
    def test_fizzbuzz_range_start_greater_than_end(self):
        """Test start greater than end."""
        with self.assertRaises(ValueError) as context:
            fizzbuzz_range(10, 5)
        self.assertEqual(str(context.exception), "Start must be less than or equal to end")
    
    def test_fizzbuzz_range_edge_cases(self):
        """Test edge cases for range."""
        # Test range 1-1
        result = fizzbuzz_range(1, 1)
        self.assertEqual(result, ["1"])
        
        # Test range 15-15 (FizzBuzz)
        result = fizzbuzz_range(15, 15)
        self.assertEqual(result, ["FizzBuzz"])
        
        # Test range 3-3 (Fizz)
        result = fizzbuzz_range(3, 3)
        self.assertEqual(result, ["Fizz"])
    
    def test_fizzbuzz_comprehensive_1_to_20(self):
        """Test comprehensive results for numbers 1-20."""
        expected = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz"
        ]
        result = fizzbuzz_range(1, 20)
        self.assertEqual(result, expected)
    
    def test_fizzbuzz_specific_cases(self):
        """Test specific important cases."""
        test_cases = [
            (1, "1"),
            (2, "2"),
            (3, "Fizz"),
            (4, "4"),
            (5, "Buzz"),
            (6, "Fizz"),
            (9, "Fizz"),
            (10, "Buzz"),
            (12, "Fizz"),
            (15, "FizzBuzz"),
            (18, "Fizz"),
            (20, "Buzz"),
            (21, "Fizz"),
            (24, "Fizz"),
            (25, "Buzz"),
            (27, "Fizz"),
            (30, "FizzBuzz"),
            (33, "Fizz"),
            (35, "Buzz"),
            (36, "Fizz"),
            (39, "Fizz"),
            (40, "Buzz"),
            (42, "Fizz"),
            (45, "FizzBuzz"),
            (48, "Fizz"),
            (50, "Buzz"),
            (51, "Fizz"),
            (54, "Fizz"),
            (55, "Buzz"),
            (57, "Fizz"),
            (60, "FizzBuzz"),
            (63, "Fizz"),
            (65, "Buzz"),
            (66, "Fizz"),
            (69, "Fizz"),
            (70, "Buzz"),
            (72, "Fizz"),
            (75, "FizzBuzz"),
            (78, "Fizz"),
            (80, "Buzz"),
            (81, "Fizz"),
            (84, "Fizz"),
            (85, "Buzz"),
            (87, "Fizz"),
            (90, "FizzBuzz"),
            (93, "Fizz"),
            (95, "Buzz"),
            (96, "Fizz"),
            (99, "Fizz"),
            (100, "Buzz")
        ]
        
        for num, expected in test_cases:
            with self.subTest(number=num):
                result = fizzbuzz(num)
                self.assertEqual(result, expected)
    
    @patch('builtins.print')
    def test_print_fizzbuzz(self, mock_print):
        """Test print_fizzbuzz function."""
        print_fizzbuzz(1, 5)
        
        # Check that print was called correct number of times
        self.assertEqual(mock_print.call_count, 5)
        
        # Check specific calls
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertIn("call('1: 1')", calls)
        self.assertIn("call('2: 2')", calls)
        self.assertIn("call('3: Fizz')", calls)
        self.assertIn("call('4: 4')", calls)
        self.assertIn("call('5: Buzz')", calls)


if __name__ == '__main__':
    unittest.main()
