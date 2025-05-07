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

# if __name__ == '__main__':

#     # Use Azure Web App settings if available, otherwise use local dev settings
#     # HOST = environ.get('WEBSITE_HOSTNAME', 'localhost')
#     try:
#         PORT = int(environ.get('WEBSITE_PORT', '8000'))
#         # port = int(os.environ.get('PORT', 8000))
#         app.run(host='0.0.0.0', port=port)
#     except ValueError:
#         PORT = 8000
        
#     # Use ssl_context only in local development
#     if HOST == 'localhost':
#         app.run(HOST, PORT, ssl_context='adhoc')
#     else:
#         app.run(HOST, PORT)
