# Guess the Number - Flask Web App

A Flask-based web application that implements an interactive number guessing game. The server generates a random number between 1-100, and players submit guesses via URL parameters to receive visual feedback.

## Features

- Interactive number guessing game (1-100)
- Session-based game state persistence
- Visual feedback with GIF animations
- Comprehensive error handling
- 94% test coverage
- Responsive design

## Setup

### 1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. (Optional) Set environment variables:
```bash
export SECRET_KEY="your-secret-key-here"  # For production
export PORT=5000  # Default port
```

## Running the Server

### Using Python directly:
```bash
python src/main.py
```

### Using nx (from monorepo root):
```bash
nx serve flask-server
```

The server will start on `http://localhost:5000`

## How to Play

1. **Start the game**: Navigate to `http://localhost:5000/`
   - You'll see a welcome message and the game initializes a hidden number

2. **Make a guess**: Enter a number (1-100) in the input field and submit
   - **Too Low**: You'll see a "Too low" message with lower.gif
   - **Too High**: You'll see a "Too high" message with higher.gif
   - **Correct**: You'll see a success message with success.gif

3. **Keep guessing**: Use the feedback to narrow down the hidden number

4. **Start new game**: Click "Start New Game" to reset and play again

## URL Structure

- `GET /` - Welcome page (initializes game)
- `GET /?guess=<number>` - Submit a guess
- `GET /health` - Health check endpoint

## Game States

| State | Trigger | Response | GIF |
|-------|---------|----------|-----|
| Welcome | No guess parameter | Welcome message | counter.gif |
| Too Low | guess < hidden_number | "Too low! Try a higher number." | lower.gif |
| Too High | guess > hidden_number | "Too high! Try a lower number." | higher.gif |
| Success | guess == hidden_number | "Congratulations! You guessed it!" | success.gif |
| Error | Invalid input | Error message | counter.gif |

## Session Management

- **Persistence**: Hidden number persists across requests within the same browser session
- **Cleanup**: Session is cleared when the browser/tab is closed
- **Security**: Session data is cryptographically signed using Flask's secure cookies

## Project Structure

```
apps/flask-server/
├── src/
│   ├── main.py              # Main Flask application
│   ├── templates/
│   │   └── game.html        # Game page template
│   └── static/
│       ├── counter.gif      # Welcome state image
│       ├── lower.gif        # Too low feedback image
│       ├── higher.gif       # Too high feedback image
│       └── success.gif      # Success celebration image
├── tests/
│   ├── test_game.py         # Unit tests
│   └── test_integration.py  # Integration tests
├── requirements.txt         # Python dependencies
├── pytest.ini              # Pytest configuration
└── README.md               # This file
```

## Testing

### Run all tests:
```bash
pytest tests/ -v
```

### Run with coverage:
```bash
pytest tests/ -v --cov=src --cov-report=term-missing
```

### Run specific test file:
```bash
pytest tests/test_game.py -v
pytest tests/test_integration.py -v
```

### Current Test Coverage: 94%

**Test Suite Includes**:
- Unit tests for game logic functions
- Integration tests for HTTP endpoints
- Session persistence tests
- Error handling tests
- Edge case tests

## Manual Testing

See `docs/guess-the-number/manual-test-checklist.md` for comprehensive manual testing scenarios.

## Development

### Creating Placeholder GIFs

If you need to recreate the placeholder GIF files:

```bash
python create_placeholders.py
```

This will generate all four required GIF files in `src/static/`.

### Code Style

- Follow PEP 8 guidelines
- Use docstrings for functions
- Keep functions focused and single-purpose
- Write tests for new features

## Configuration

### Environment Variables

- `SECRET_KEY`: Flask session encryption key (required for production)
- `PORT`: Server port (default: 5000)
- `DEBUG`: Debug mode (default: True in development)

### Security Notes

- The default SECRET_KEY is for development only
- In production, set a strong SECRET_KEY via environment variable
- Session cookies are signed to prevent tampering
- Consider using HTTPS in production for cookie security

## Troubleshooting

### Issue: Session not persisting
- **Solution**: Ensure SECRET_KEY is set and consistent across requests

### Issue: GIF images not loading
- **Solution**: Verify files exist in `src/static/` directory
- Run `python create_placeholders.py` to regenerate

### Issue: Tests failing
- **Solution**: Ensure virtual environment is activated and dependencies installed
- Run `pip install -r requirements.txt`

### Issue: Port already in use
- **Solution**: Change PORT environment variable or kill process using port 5000
- `lsof -ti:5000 | xargs kill -9` (macOS/Linux)

## Documentation

- **Product Specification**: `docs/guess-the-number/product-specification.md`
- **Design Document**: `docs/guess-the-number/design-document.md`
- **Implementation Plan**: `docs/guess-the-number/implementation-plan.md`
- **Manual Test Checklist**: `docs/guess-the-number/manual-test-checklist.md`

## License

This is a learning project for educational purposes.
