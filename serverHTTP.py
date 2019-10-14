#!flask/bin/python
from app import app

from flask import Flask
import os
app2 = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT'))

    app2.run(host = "0.0.0.0",port = PORT)
