import os

from .config import config
from flask import Flask
from .utils import backup_db

# import logging
# conf = config['Production']
# conf = config['Development']

# Load Configuration
conf = config[os.environ.get('CONFIG', 'Development')]

from ..db_impl.app import SampleDB

app = Flask(__name__)
app.config.from_object(conf)

# handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
# handler.setLevel(app.config['LOGGING_LEVEL'])
# formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
# handler.setFormatter(formatter)
# app.logger.addHandler(handler)

backup_db(conf.DB_PATH, conf.BACKUP_PATH, conf.BACKUP_DATE_FORMAT)

db = SampleDB(conf.SQLALCHEMY_DATABASE_URI)
import views

print "Loading Flask App"
