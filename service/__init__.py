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

# Configuration settings (if any)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'a-very-secret-key')

# Import routes here to avoid circular imports later
# from service import routes
