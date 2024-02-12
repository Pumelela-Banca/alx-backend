#!/usr/bin/env python3
"""
Flask start app and add babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configures languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def index():
    """
    renders index.html
    """
    return render_template('index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Gets locale for page
    """
    if request.args.get("locale") in app.config["LANGUAGES"]:
        return request.args.get("locale")
    return (
        request.accept_languages.best_match(app.config["LANGUAGES"]))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
