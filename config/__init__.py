"""Flask application configuration settings.

This package defines configuration classes for different environments
(development, and  testing). It handles environment variables
and sets default values for Flask application settings.

The hierarchy of where to choose variables are:
    1. Environment variables.
    2. config.toml (user set config. file).
    3. hard-coded values (reasonable default values).

"""
from .config import Config
from .dev_config import DevConfig
from .testing_config import TestingConfig

__all__ = ["Config", "DevConfig", "TestingConfig"]
