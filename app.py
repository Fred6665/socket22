from flask import Flask
import os
app = Flask(__name__)

@app.route('/<rrr>')
def hello_world(rrr):
    return str(rrr)

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT'))

    app.run(host = "0.0.0.0",port = PORT)
