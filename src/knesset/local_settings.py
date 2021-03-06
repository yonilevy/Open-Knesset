from os import path
from settings import *
DATABASE_ENGINE = 'sqlite3'         # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'dev.db'  # Or path to database file if using sqlite3.
LOCAL_DEV = True
MEDIA_URL = '/static/'
MEDIA_ROOT = path.abspath(path.join(PROJECT_ROOT, 'static', ''))

TEST_DATABASE_CHARSET = 'utf8'
TEST_DATABASE_COLLATION = 'utf8_general_ci'

#DEBUG_TOOLBAR_CONFIG['INTERCEPT_REDIRECTS'] = False

EMAIL_PORT = 1025
