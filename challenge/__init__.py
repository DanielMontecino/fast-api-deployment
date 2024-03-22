"""
This module serves as the entry point for the FastAPI application.

It imports the `app` object from the `challenge.api` module and assigns it to \
    the `application` variable.

The `application` variable can be used to run the FastAPI application.
"""

from challenge.api import app

application = app
