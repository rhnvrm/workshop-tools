from flask import Flask, request
from flask_cors import CORS, cross_origin
import operator

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

leaderboard = {}


@app.route('/')
@cross_origin(origin='*')
def hello():
    return "hello world"


@app.route('/insert', methods=['POST'])
@cross_origin(origin='*')
def insert():
    who = request.form['name']
    lvl = request.form['level']
    leaderboard[who] = lvl
    return 'Success!'


@app.route('/display', methods=['GET'])
@cross_origin(origin='*')
def display():
    sorted_lboard = sorted(leaderboard.items(),
                           key=operator.itemgetter(1),
                           reverse=True)
    str_lboard = ""
    for i in sorted_lboard:
        str_lboard += "" + i[0] + ":" + i[1] + "\n"
    return str_lboard


app.run(host='0.0.0.0')
