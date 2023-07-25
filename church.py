#!/usr/bin/env python

from flask_bootstrap import Bootstrap5
from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
bootstrap = Bootstrap5(app)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/faq")
def faq():
    return render_template('faq.html')