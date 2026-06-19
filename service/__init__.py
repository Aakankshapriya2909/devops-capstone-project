import os
import logging
from flask import Flask
from flask_talisman import Talisman

# Initialize Flask Application
app = Flask(__name__)

# Initialize Talisman with Security Headers
talisman = Talisman(
    app,
    content_security_policy=None,  # Disabled for testing purposes
    force_https=False              # Disabled for local development/testing
)

# Configuration settings
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'a-very-secret-key')
