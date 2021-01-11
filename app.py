from pymongo import MongoClient

from flask import Flask, render_template, jsonify

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
@app.route('/stretch/fullbody', methods=['GET'])
def show_fullbodyST():
    fullbodySTs = list(db.myproject.find({}, {"_id": 0, "videoId": 1, "subCAT": "fullbodyST"}).limit(4))
    # fullbodySTs = list(db.myproject.find({}, {"subCAT": "fullbodyST"}).sort([{"_id": 1}]))
    # fullbodySTs = list(db.myproject.find({"subCAT": "fullbodyST"},{'videoId':1}))
    return jsonify({'result': 'success', 'fullbodyST_list': fullbodySTs})


@app.route('/stretch/upperbody', methods=['GET'])
def show_upperbodyST():
    upperbodySTs = list(db.myproject.find({}, {"_id": 0, "videoId": 1, "subCAT": "upperbodyST"}).limit(4))
    return jsonify({'result': 'success', 'upperbodyST_list': upperbodySTs})


@app.route('/stretch/lowerbody', methods=['GET'])
def show_lowerbodyST():
    lowerbodySTs = list(db.myproject.find({}, {"_id": 0, "videoId": 1, "subCAT": "lowerbodyST"}).limit(4))
    return jsonify({'result': 'success', 'lowerbodyST_list': lowerbodySTs})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
