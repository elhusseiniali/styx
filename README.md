![build](https://github.com/elhusseiniali/flask-boilerplate/workflows/build/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/elhusseiniali/styx/badge.svg?branch=master)](https://coveralls.io/github/elhusseiniali/styx?branch=master)
![Python Version](https://img.shields.io/badge/python-%3E%3D3.9-3776AB?logo=python&logoColor=white)
# Styx
Styx is meant to be a Flask app where users can log their workouts. The feature list will grow as the project evolves.

# Setup Guide

1. Copy the contents of config.example.toml to config.toml inside the config package and follow the instructions (only needed for customization):
    ```bash
    cd config
    cp default_config.toml config.toml
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
- `create-db`: Create the tables defined in models package.
    ```bash
    flask --app=run.py create-db
    ```

- `delete-db`: Drop the tables defined in models package.
    ```bash
    flask --app=run.py delete-db
    ```

## Testing

Run the tests with:
```python
python -m pytest
```