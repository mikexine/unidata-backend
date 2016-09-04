# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment
from webassets.loaders import PythonLoader
from flask_migrate import Migrate
from uniopen import assets

app = Flask(__name__)
# The environment variable, either 'prod' or 'dev'
env = os.environ.get("UNIOPEN_ENV", "prod")
# Use the appropriate environment-specific settings
app.config.from_object('uniopen.settings.{env}Config'
                        .format(env=env.capitalize()))
app.config['ENV'] = env
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register asset bundles
assets_env = Environment()
assets_env.init_app(app)
assets_loader = PythonLoader(assets)
for name, bundle in assets_loader.load_bundles().iteritems():
    assets_env.register(name, bundle)
