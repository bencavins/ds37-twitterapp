import re
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app_title = "Twitoff DS37!!!!!!"


    @app.route("/")
    def root():
        return render_template('base.html', title='Home')

    @app.route("/test")
    def test():
        return f"<p>This is a page for {app_title}</p>"
    
    return app