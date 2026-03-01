import unittest
from unittest.mock import patch
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from bill_payer import select_bill_payer


class TestBillPayer(unittest.TestCase):
    
    def test_select_bill_payer_valid_list(self):
        """Test selecting a bill payer from a valid list of friends."""
        friends = ["Alice", "Bob", "Charlie"]
        with patch('random.choice', return_value="Bob"):
            with patch('builtins.print') as mock_print:
                result = select_bill_payer(friends)
                self.assertEqual(result, "Bob")
                mock_print.assert_called_once_with("Bob will pay the bill!")
    
    def test_select_bill_payer_empty_list(self):
        """Test that empty list raises ValueError."""
        with self.assertRaises(ValueError) as context:
            select_bill_payer([])
        self.assertEqual(str(context.exception), "Friends list cannot be empty")
    
    def test_select_bill_payer_not_list(self):
        """Test that non-list input raises ValueError."""
        with self.assertRaises(ValueError) as context:
            select_bill_payer("Alice, Bob, Charlie")
        self.assertEqual(str(context.exception), "Friends must be provided as a list")
    
    def test_select_bill_payer_with_empty_strings(self):
        """Test handling of empty strings in the list."""
        friends = ["Alice", "", "Bob", None, "Charlie"]
        with patch('random.choice', return_value="Charlie"):
            with patch('builtins.print') as mock_print:
                result = select_bill_payer(friends)
                self.assertEqual(result, "Charlie")
                mock_print.assert_called_once_with("Charlie will pay the bill!")
    
    def test_select_bill_payer_all_invalid(self):
        """Test that list with only invalid entries raises ValueError."""
        friends = ["", None, "", ""]
        with self.assertRaises(ValueError) as context:
            select_bill_payer(friends)
        self.assertEqual(str(context.exception), "Friends list must contain valid names")
    
    def test_select_bill_payer_single_friend(self):
        """Test selecting from a list with only one friend."""
        friends = ["Alice"]
        with patch('builtins.print') as mock_print:
            result = select_bill_payer(friends)
            self.assertEqual(result, "Alice")
            mock_print.assert_called_once_with("Alice will pay the bill!")
    
    def test_select_bill_payer_random_distribution(self):
        """Test that the selection is random (statistical test)."""
        friends = ["Alice", "Bob", "Charlie"]
        results = {"Alice": 0, "Bob": 0, "Charlie": 0}
        
        # Run multiple times to test randomness
        for _ in range(100):
            result = select_bill_payer(friends)
            results[result] += 1
        
        # Each friend should be chosen at least once (very high probability)
        for friend, count in results.items():
            self.assertGreater(count, 0, f"Friend {friend} was never chosen")
    
    def test_select_bill_payer_non_string_entries(self):
        """Test handling of non-string entries in the list."""
        friends = ["Alice", 123, "Bob", True, "Charlie"]
        # Should filter out non-string entries
        valid_friends = [friend for friend in friends if isinstance(friend, str)]
        self.assertEqual(len(valid_friends), 3)
        
        with patch('random.choice', return_value="Bob"):
            with patch('builtins.print') as mock_print:
                result = select_bill_payer(friends)
                self.assertEqual(result, "Bob")
                mock_print.assert_called_once_with("Bob will pay the bill!")


if __name__ == '__main__':
    unittest.main()
