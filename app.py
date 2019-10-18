from flask import Flask, request
import os
app = Flask(__name__)

@app.errorhandler(400)
def error_req(error):
    return str("you giv error 400")

@app.route('/sing_up',methods=['GET','POST'])
def hello_world():
    #DB = os.environ.get('DATABASE_URL')
    return "It`s GOOD!!!"

@app.route('/events', methods=['POST'])
def events():
#    return request.form["home"]
#    return {66:333}
    ret = request.json
    return str(ret['66'])
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT'))

    app.run(host = "0.0.0.0",port = PORT)
