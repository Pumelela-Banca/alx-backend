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
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Gets locale for page
    """
    locale = request.args.get("locale")
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])
