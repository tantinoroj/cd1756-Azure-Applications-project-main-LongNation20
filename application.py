"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ
from FlaskWebProject import app
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT, ssl_context='adhoc')
