import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'xd'

SQLALCHEMY_DATABASE_URI = ''

OAUTH_CREDENTIALS = {
    'xd': {
        'id': '',
        'secret': ''
    }
}

UPLOAD_FOLDER = os.path.join(basedir, '')

LOG_FILENAME = ""

LOG_FORMAT = ""

ALLOWED_EXTENSIONS = []
