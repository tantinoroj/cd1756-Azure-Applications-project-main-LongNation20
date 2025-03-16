import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dac1d194-bc21-41a4-ae76-9faf0f2d63cb'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmstan'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'l3dXxrnSbhUWkB4qBZy5bPjzRGeqnK0KXuJbMVTd1OP5+VfMnAZg51MKJsYDpveeMIzb4lVY/+x/+AStUpeGKA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmstan'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'sqladmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '!pwd1234'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = 'gLC8Q~J4L02s014LcQF-rZ4PrjyZBfyF21xrgbnu'
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    # AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/f958e84a-92b8-439f-a62d-4f45996b6d07"

    CLIENT_ID = 'e2b17eb9-7334-4c3a-ba90-bbd09b4aa1d4'

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
