#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Docstring
~~~~~~~~~~

High Level Overview
1.
2.
3.
"""

from flask import (
    Flask,
    make_response,
    render_template
)
from werkzeug.debug import DebuggedApplication

import app_config
from .logger import Logger
import oauth
import static
from render_utils import make_context, smarty_filter, urlencode_filter

app = Flask(__name__)
app.debug = app_config.DEBUG

app.add_template_filter(smarty_filter, name='smarty')
app.add_template_filter(urlencode_filter, name='urlencode')

app.register_blueprint(static.static)
app.register_blueprint(oauth.oauth)

log = Logger(
    name=__name__,
    level=app_config.LOG_LEVEL,
    file_handler=__name__
)


@app.route('/')
@oauth.oauth_required
def index():
    """
    Example view demonstrating rendering a simple HTML page.
    """
    context = make_context()

    return make_response(render_template('index.html', **context))


# Enable Werkzeug debug pages
if app_config.DEBUG:
    wsgi_app = DebuggedApplication(app, evalex=False)
else:
    wsgi_app = app


# Catch attempts to run the app directly
if __name__ == "__main__":
    log.error("This command has been removed! Please run 'fab app' instead!")