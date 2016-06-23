import os
from flask import Flask

app = Flask(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, '../pancake.db'),
    SECRET_KEY=b'my super s33kr1t key',
    USERNAME='admin',
    PASSWORD='default',
    DEBUG=1,
))
app.config.from_envvar('APP_SETTINGS', silent=True)

# import view modules for the side effects (URL regisration)

from app import (   # nopep8
    login,
    views,
)
