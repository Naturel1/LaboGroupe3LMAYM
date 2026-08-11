import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

load_dotenv()

env_path = Path().cwd() / '.env.local'
if os.path.exists(env_path):
    load_dotenv(env_path, override=True)

app = Flask("app")
app.debug = os.environ.get("DEBUG", "False").lower() in ("1", "true", "yes")

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "TestAsdf1234=")

csrf = CSRFProtect(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import *
