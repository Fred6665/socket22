from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    DB = os.environ.get('DATABASE_URL')
    return {"tery":"lol","fr":[22,10,22]}

@app.route('/events', methods=['POST'])
def events():
#    return request.form["home"]
#    return {66:333}
    ret = request.json
    return str(ret['66'])
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT'))

    app.run(host = "0.0.0.0",port = PORT)
