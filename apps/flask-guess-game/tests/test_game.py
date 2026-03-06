"""Unit tests for the guess the number game functions."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import evaluate_guess, initialize_game, app


class TestEvaluateGuess:
    """Test the evaluate_guess function."""
    
    def test_guess_too_low(self):
        """Test when guess is lower than hidden number."""
        result = evaluate_guess(30, 50)
        assert result['message'] == 'Too low! Try a higher number.'
        assert result['gif_filename'] == 'lower.gif'
    
    def test_guess_too_high(self):
        """Test when guess is higher than hidden number."""
        result = evaluate_guess(70, 50)
        assert result['message'] == 'Too high! Try a lower number.'
        assert result['gif_filename'] == 'higher.gif'
    
    def test_guess_correct(self):
        """Test when guess equals hidden number."""
        result = evaluate_guess(50, 50)
        assert result['message'] == 'Congratulations! You guessed it!'
        assert result['gif_filename'] == 'success.gif'
    
    def test_guess_edge_case_min(self):
        """Test with minimum value."""
        result = evaluate_guess(1, 1)
        assert result['message'] == 'Congratulations! You guessed it!'
        assert result['gif_filename'] == 'success.gif'
    
    def test_guess_edge_case_max(self):
        """Test with maximum value."""
        result = evaluate_guess(100, 100)
        assert result['message'] == 'Congratulations! You guessed it!'
        assert result['gif_filename'] == 'success.gif'


class TestInitializeGame:
    """Test the initialize_game function."""
    
    def test_initialize_creates_hidden_number(self):
        """Test that initialize_game creates a hidden number in session."""
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess.clear()
            
            client.get('/')
            with client.session_transaction() as sess:
                assert 'hidden_number' in sess
                assert 1 <= sess['hidden_number'] <= 100
    
    def test_initialize_preserves_existing_number(self):
        """Test that initialize_game doesn't change existing hidden number."""
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['hidden_number'] = 42
            
            client.get('/')
            with client.session_transaction() as sess:
                assert sess['hidden_number'] == 42
    
    def test_random_number_range(self):
        """Test that generated numbers are within valid range."""
        for _ in range(10):
            with app.test_client() as client:
                with client.session_transaction() as sess:
                    sess.clear()
                
                client.get('/')
                with client.session_transaction() as sess:
                    assert 1 <= sess['hidden_number'] <= 100
