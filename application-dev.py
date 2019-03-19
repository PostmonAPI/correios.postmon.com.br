# coding: utf-8
from __future__ import absolute_import

from flask import current_app, Flask

import postmon_correios

app = Flask(__name__)
app.debug = True
postmon_correios.init_app(app)

@app.route('/crossdomain.xml')
def crossdomain():
    return current_app.send_static_file('crossdomain.xml')
    return app
