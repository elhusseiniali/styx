"""Application entry point for the Styx web application.

This module initializes and runs the Flask application
using the factory pattern. The application is created using
the create_app factory function from the styx package.

Usage:
    python run.py

The application will start in debug mode if configured in config.py.
Debug mode should not be used in production environments.
"""
from styx import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=app.debug)
