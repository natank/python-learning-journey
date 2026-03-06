from flask import Flask, session, request, render_template
import random
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, 
            static_folder=os.path.join(basedir, 'static'),
            template_folder=os.path.join(basedir, 'templates'))
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

def initialize_game():
    """Initialize or retrieve the hidden number from session."""
    if 'hidden_number' not in session:
        session['hidden_number'] = random.randint(1, 100)
    return session['hidden_number']

def evaluate_guess(guess, hidden_number):
    """Evaluate the user's guess and return appropriate message and GIF."""
    if guess < hidden_number:
        return {
            'message': 'Too low! Try a higher number.',
            'gif_filename': 'lower.gif'
        }
    elif guess > hidden_number:
        return {
            'message': 'Too high! Try a lower number.',
            'gif_filename': 'higher.gif'
        }
    else:
        return {
            'message': 'Congratulations! You guessed it!',
            'gif_filename': 'success.gif'
        }

@app.route('/')
def index():
    """Welcome page - initializes the game."""
    initialize_game()
    return render_template(
        'game.html',
        message='Welcome to Guess the Number! I\'m thinking of a number between 1 and 100.',
        gif_filename='counter.gif',
        guess=None
    )

@app.route('/<int:guess>')
def guess_number(guess):
    """Handle guess with path parameter."""
    hidden_number = initialize_game()
    result = evaluate_guess(guess, hidden_number)
    
    return render_template(
        'game.html',
        message=result['message'],
        gif_filename=result['gif_filename'],
        guess=guess
    )

@app.route('/<guess>')
def invalid_guess(guess):
    """Handle invalid (non-integer) guess."""
    initialize_game()
    return render_template(
        'game.html',
        message='Error: Please enter a valid number.',
        gif_filename='counter.gif',
        guess=None
    ), 400

@app.route('/health')
def health():
    """Health check endpoint."""
    return {'status': 'healthy'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
