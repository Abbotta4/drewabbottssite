from os import urandom
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for

application = Flask(__name__)
application.secret_key = urandom(12)

@application.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
