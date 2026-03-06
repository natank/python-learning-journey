"""Integration tests for the guess the number web app."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestWelcomePage:
    """Test the welcome/initial page."""
    
    def test_welcome_page_loads(self, client):
        """Test that the welcome page loads successfully."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Welcome to Guess the Number' in response.data
        assert b'counter.gif' in response.data
    
    def test_welcome_page_initializes_session(self, client):
        """Test that visiting welcome page initializes session."""
        response = client.get('/')
        with client.session_transaction() as sess:
            assert 'hidden_number' in sess
            assert 1 <= sess['hidden_number'] <= 100


class TestGuessTooLow:
    """Test the 'guess too low' scenario."""
    
    def test_guess_too_low_response(self, client):
        """Test response when guess is too low."""
        with client.session_transaction() as sess:
            sess['hidden_number'] = 50
        
        response = client.get('/30')
        assert response.status_code == 200
        assert b'Too low' in response.data
        assert b'lower.gif' in response.data
    
    def test_guess_minimum_value(self, client):
        """Test guessing minimum value when it's too low."""
        with client.session_transaction() as sess:
            sess['hidden_number'] = 50
        
        response = client.get('/1')
        assert response.status_code == 200
        assert b'Too low' in response.data


class TestGuessTooHigh:
    """Test the 'guess too high' scenario."""
    
    def test_guess_too_high_response(self, client):
        """Test response when guess is too high."""
        with client.session_transaction() as sess:
            sess['hidden_number'] = 50
        
        response = client.get('/70')
        assert response.status_code == 200
        assert b'Too high' in response.data
        assert b'higher.gif' in response.data
    
    def test_guess_maximum_value(self, client):
        """Test guessing maximum value when it's too high."""
        with client.session_transaction() as sess:
            sess['hidden_number'] = 50
        
        response = client.get('/100')
        assert response.status_code == 200
        assert b'Too high' in response.data


class TestCorrectGuess:
    """Test the correct guess scenario."""
    
    def test_correct_guess_response(self, client):
        """Test response when guess is correct."""
        with client.session_transaction() as sess:
            sess['hidden_number'] = 50
        
        response = client.get('/50')
        assert response.status_code == 200
        assert b'Congratulations' in response.data
        assert b'success.gif' in response.data
    
    def test_correct_guess_edge_cases(self, client):
        """Test correct guess at edge values."""
        with client.session_transaction() as sess:
            sess['hidden_number'] = 1
        
        response = client.get('/1')
        assert response.status_code == 200
        assert b'Congratulations' in response.data
        
        with client.session_transaction() as sess:
            sess['hidden_number'] = 100
        
        response = client.get('/100')
        assert response.status_code == 200
        assert b'Congratulations' in response.data


class TestSessionPersistence:
    """Test that session persists across requests."""
    
    def test_hidden_number_persists(self, client):
        """Test that hidden number stays the same across multiple guesses."""
        client.get('/')
        
        with client.session_transaction() as sess:
            hidden = sess['hidden_number']
        
        client.get('/10')
        
        with client.session_transaction() as sess:
            assert sess['hidden_number'] == hidden
        
        client.get('/50')
        
        with client.session_transaction() as sess:
            assert sess['hidden_number'] == hidden
    
    def test_multiple_guesses_same_session(self, client):
        """Test making multiple guesses in the same session."""
        with client.session_transaction() as sess:
            sess['hidden_number'] = 50
        
        response1 = client.get('/30')
        assert b'Too low' in response1.data
        
        response2 = client.get('/70')
        assert b'Too high' in response2.data
        
        response3 = client.get('/50')
        assert b'Congratulations' in response3.data


class TestInvalidInput:
    """Test error handling for invalid input."""
    
    def test_non_numeric_guess(self, client):
        """Test that non-numeric input returns error."""
        response = client.get('/abc')
        assert response.status_code == 400
        assert b'Error' in response.data or b'valid number' in response.data
    
    def test_empty_guess_parameter(self, client):
        """Test that root path shows welcome (no error for empty)."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Welcome' in response.data
    
    def test_float_guess(self, client):
        """Test that float values return error (path parameter won't match int route)."""
        with client.session_transaction() as sess:
            sess['hidden_number'] = 50
        
        response = client.get('/50.5')
        assert response.status_code == 400


class TestHealthEndpoint:
    """Test the health check endpoint."""
    
    def test_health_endpoint(self, client):
        """Test that health endpoint returns healthy status."""
        response = client.get('/health')
        assert response.status_code == 200
        assert b'healthy' in response.data


class TestGameFlow:
    """Test complete game flow from start to finish."""
    
    def test_complete_game_flow(self, client):
        """Test a complete game from welcome to success."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Welcome' in response.data
        
        with client.session_transaction() as sess:
            hidden = sess['hidden_number']
        
        if hidden > 50:
            response = client.get('/50')
            assert b'Too low' in response.data
        elif hidden < 50:
            response = client.get('/50')
            assert b'Too high' in response.data
        
        response = client.get(f'/{hidden}')
        assert response.status_code == 200
        assert b'Congratulations' in response.data
