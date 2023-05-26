# This file is the entry point of the application.
# It imports and runs the Flask application from app.py.

from app import app

if __name__ == '__main__':
    app.run(debug=True)
