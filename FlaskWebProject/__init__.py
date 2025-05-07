"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from dotenv import load_dotenv
import os

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# Set up logging
logging.basicConfig(
    level=logging.INFO,  # Set logging level to INFO
    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
)
app.logger.setLevel(logging.INFO)

# Add the handler to the app's logger
app.logger.addHandler(handler)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)

# Defer importing views after app initialization to avoid circular imports
from FlaskWebProject import views , models  # Import views here

@login.user_loader
def load_user(id):
    return models.User.query.get(int(id))


