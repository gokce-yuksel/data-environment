# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    env = os.getenv("FLASK_ENV")

    if env == "development":
        return "Starting in development mode..."
    if env == "production":
        return "Starting in production mode..."

    return "Starting in empty mode..."

if __name__ == "__main__":
    print(start())
