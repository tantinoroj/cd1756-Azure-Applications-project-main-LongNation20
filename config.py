import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    DEBUG = True
    SECRET_KEY = '2971343e-c5d9-4bce-a664-56e7d292b42e'

    BLOB_ACCOUNT = 'image30'
    BLOB_STORAGE_KEY = '6g1dmgSmM4xJuujBArXCDZnGUe4kmxavKi2qyCc8qJ3RseIHhZRBLg/9xcclMiLY+oustPrFyXE/+AStKi8CwQ=='
    BLOB_CONTAINER = 'image'
    BLOB_CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName=image30;AccountKey=6g1dmgSmM4xJuujBArXCDZnGUe4kmxavKi2qyCc8qJ3RseIHhZRBLg/9xcclMiLY+oustPrFyXE/+AStKi8CwQ==;EndpointSuffix=core.windows.net'

    SQL_SERVER = 'cmstan2.database.windows.net'
    SQL_DATABASE = 'cms'
    SQL_USER_NAME = 'sqladmin'
    SQL_PASSWORD = '!pwd1234'

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/{SQL_DATABASE}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_SECRET = 'kAZ8Q~h21nWxTOyd85KKfkgRsDSeGYGLnLZF7ap3'
    AUTHORITY = "https://login.microsoftonline.com/ff873fe8-6631-416d-9262-bdbd56117dae"

    CLIENT_ID = '416d6f76-eb16-48ac-a864-59b8326309a1'

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
