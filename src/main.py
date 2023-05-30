"""This file is the entry point of the Flask application."""
from app import app

if __name__ == '__main__':
    """Runs the flask application."""
    app.run(debug=True)
