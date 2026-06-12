from flask import Flask
from connection.connect import engine, Session, Base
from connection.models import Account
from blueprints.frontpage import frontpage
from blueprints.homepage import homepage
import secrets
import os

app = Flask(__name__)

app.secret_key = secrets.token_hex(32)

UPLOAD_FOLDER = 'static/PostIMG'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

app.register_blueprint(frontpage)
app.register_blueprint(homepage)

Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True)