from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config:
    """
    Veja configurações do flask em
    https://flask.palletsprojects.com/en/1.1.x/config/
    """
    # Uma forma de gerar essa chave
    # python3 -c 'import os; print(os.urandom(16))'
    SECRET_KEY=environ.get('SECRET_KEY')

    FLASK_ENV=environ.get('FLASK_ENV')
    SQLALCHEMY_DATABASE_URI=environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
