import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'xd'

SQLALCHEMY_DATABASE_URI = 'mysql://xd:xd@localhost/xd'

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

OAUTH_CREDENTIALS = {
    'xd': {
        'id': '',
        'secret': ''
    }
}

UPLOAD_FOLDER = os.path.join(basedir, 'uploads')

LOG_FILENAME = "xd.log"

LOG_FORMAT = ""

ALLOWED_EXTENSIONS = ["pdf"]
