![build](https://github.com/elhusseiniali/flask-boilerplate/workflows/build/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/elhusseiniali/styx/badge.svg?branch=master)](https://coveralls.io/github/elhusseiniali/styx?branch=master)
![Python Version](https://img.shields.io/badge/python-%3E%3D3.10-3776AB?logo=python&logoColor=white)
# Styx
Styx is meant to be a Flask app where users can log their workouts. The feature list will grow as the project evolves.

# Setup Guide

1. Copy the contents of config.example.toml to config.toml in the main directory (it doesn't matter because it looks for config.toml or given filename anywhere in the project) and follow the instructions (only needed for customization):
    ```bash
    cp config.example.toml config.toml
    ```

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
- `create`: Create the tables defined in models package.
    ```bash
    flask --app=run.py db create
    ```

- `delete`: Drop the tables defined in models package.
    ```bash
    flask --app=run.py db delete
    ```

- `reset`: Reset the tables defined in models package.
    ```bash
    flask --app=run.py db reset
    ```

## Testing

Run the tests with:
```python
python -m pytest
```