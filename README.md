![build](https://github.com/elhusseiniali/flask-boilerplate/workflows/build/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/elhusseiniali/flask-boilerplate/badge.svg?branch=master)](https://coveralls.io/github/elhusseiniali/flask-boilerplate?branch=master)
![Python Version](https://img.shields.io/badge/python-%3E=3.13.1-blue)
# Styx
Styx is meant to be a Flask app where users can log their workouts. The feature list will grow as the project evolves.

# Setup Guide

1. Create a `.env` file and copy the contents from `.env.example` and update the values according to the instructions in the template file.

2. Install project dependencies with:
    ```python
    pip install -r requirements.txt
    ```

## Running the Application

Start the application with:
```python
python run.py
```

## Database Management

The following commands are available for database management:
- `create-db`: Create the tables defined in models module.
- `delete-db`: Drop the tables defined in models module.

## Testing

Run the tests with:
```python
python -m pytest
```
