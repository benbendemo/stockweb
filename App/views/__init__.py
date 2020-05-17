from flask import (Blueprint, 
                    render_template, 
                    redirect, 
                    url_for, 
                    request, 
                    flash,
                    send_from_directory,
                    make_response,
                    Response,
                    abort,
                    session,
                    g,
                    current_app,
                    jsonify)
import os
from .views import blue

basepath = os.path.dirname(__file__)

def init_views(app):
    app.register_blueprint(blue)