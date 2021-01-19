import math

from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
# 스트레칭 API
@app.route('/st/fullbody', methods=['GET'])
def show_fullbodyST():
    page = int(request.args.get('page', 1))
    LIMIT = 8
    offset = (page - 1) * LIMIT
    fullbody_sts = list(db.myproject.find({'subCAT': 'fullbodyST'}, {'_id': 0}).limit(LIMIT).skip(offset))
    return jsonify({'result': 'success', 'fullbodyST_list': fullbody_sts})


@app.route('/st/upperbody', methods=['GET'])
def show_upperbodyST():
    page = int(request.args.get('page', 1))
    LIMIT = 8
    offset = (page - 1) * LIMIT
    upperbody_sts = list(db.myproject.find({'subCAT': 'upperbodyST'}, {'_id': 0}).limit(LIMIT).skip(offset))
    return jsonify({'result': 'success', 'upperbodyST_list': upperbody_sts})


@app.route('/st/lowerbody', methods=['GET'])
def show_lowerbodyST():
    page = int(request.args.get('page', 1))
    LIMIT = 8
    offset = (page - 1) * LIMIT
    lowerbody_sts = list(db.myproject.find({'subCAT': 'lowerbodyST'}, {'_id': 0}).limit(LIMIT).skip(offset))
    return jsonify({'result': 'success', 'lowerbodyST_list': lowerbody_sts})


# 유산소 운동 API
@app.route('/cardio', methods=['GET'])
def show_cardio():
    page = int(request.args.get('page', 1))
    LIMIT = 8
    offset = (page - 1) * LIMIT
    cardios = list(db.myproject.find({'subCAT': 'Cardio'}, {'_id': 0}).limit(LIMIT).skip(offset))
    return jsonify({'result': 'success', 'cardio_list': cardios})


# 근력 운동 API
@app.route('/w/upperbody', methods=['GET'])
def show_upperbodyW():
    page = int(request.args.get('page', 1))
    LIMIT = 8
    offset = (page - 1) * LIMIT
    upperbody_ws = list(db.myproject.find({'subCAT': 'upperbodyW'}, {'_id': 0}).limit(LIMIT).skip(offset))
    return jsonify({'result': 'success', 'upperbodyW_list': upperbody_ws})


@app.route('/w/lowerbody', methods=['GET'])
def show_lowerbodyW():
    page = int(request.args.get('page', 1))
    LIMIT = 8
    offset = (page - 1) * LIMIT
    lowerbody_ws = list(db.myproject.find({'subCAT': 'lowerbodyW'}, {'_id': 0}).limit(LIMIT).skip(offset))
    return jsonify({'result': 'success', 'lowerbodyW_list': lowerbody_ws})


@app.route('/w/core', methods=['GET'])
def show_coreW():
    page = int(request.args.get('page', 1))
    LIMIT = 8
    offset = (page - 1) * LIMIT
    core_ws = list(db.myproject.find({'subCAT': 'coreW'}, {'_id': 0}).limit(LIMIT).skip(offset))
    return jsonify({'result': 'success', 'coreW_list': core_ws})


@app.route('/w/abs', methods=['GET'])
def show_absW():
    page = int(request.args.get('page', 1))
    LIMIT = 8
    offset = (page - 1) * LIMIT
    abs_ws = list(db.myproject.find({'subCAT': 'absW'}, {'_id': 0}).limit(LIMIT).skip(offset))
    return jsonify({'result': 'success', 'absW_list': abs_ws})


@app.route('/w/hip', methods=['GET'])
def show_hipW():
    page = int(request.args.get('page', 1))
    LIMIT = 8
    offset = (page - 1) * LIMIT
    hip_ws = list(db.myproject.find({'subCAT': 'hipW'}, {'_id': 0}).limit(LIMIT).skip(offset))
    return jsonify({'result': 'success', 'hipW_list': hip_ws})


# @app.route('/st/fullbody', methods=['GET'])
# def show_fullbodyST():
#     fullbody_sts = list(
#         db.myproject.aggregate([{'$match': {'subCAT': 'fullbodyST'}}, {'$project': {'_id': 0}}]))
#     return jsonify({'result': 'success', 'fullbodyST_list': fullbody_sts})


# @app.route('/st/upperbody', methods=['GET'])
# def show_upperbodyST():
#     upperbody_sts = list(
#         db.myproject.aggregate([{'$match': {'subCAT': 'upperbodyST'}}, {'$project': {'_id': 0}}]))
#     return jsonify({'result': 'success', 'upperbodyST_list': upperbody_sts})


# @app.route('/st/lowerbody', methods=['GET'])
# def show_lowerbodyST():
#     lowerbody_sts = list(
#         db.myproject.aggregate([{'$match': {'subCAT': 'lowerbodyST'}}, {'$project': {'_id': 0}}]))
#     return jsonify({'result': 'success', 'lowerbodyST_list': lowerbody_sts})


# 유산소 운동 API
# @app.route('/cardio', methods=['GET'])
# def show_cardio():
#     cardios = list(
#         db.myproject.aggregate([{'$match': {'subCAT': 'Cardio'}}, {'$project': {'_id': 0}}]))
#     return jsonify({'result': 'success', 'cardio_list': cardios})


# 근력 운동 API
# @app.route('/w/upperbody', methods=['GET'])
# def show_upperbodyW():
#     upperbody_ws = list(
#         db.myproject.aggregate([{'$match': {'subCAT': 'upperbodyW'}}, {'$project': {'_id': 0}}]))
#     return jsonify({'result': 'success', 'upperbodyW_list': upperbody_ws})


# @app.route('/w/lowerbody', methods=['GET'])
# def show_lowerbodyW():
#     lowerbody_ws = list(
#         db.myproject.aggregate([{'$match': {'subCAT': 'lowerbodyW'}}, {'$project': {'_id': 0}}]))
#     return jsonify({'result': 'success', 'lowerbodyW_list': lowerbody_ws})


# @app.route('/w/core', methods=['GET'])
# def show_coreW():
#     core_ws = list(
#         db.myproject.aggregate([{'$match': {'subCAT': 'coreW'}}, {'$project': {'_id': 0}}]))
#     return jsonify({'result': 'success', 'coreW_list': core_ws})
#
#
# @app.route('/w/abs', methods=['GET'])
# def show_absW():
#     abs_ws = list(
#         db.myproject.aggregate([{'$match': {'subCAT': 'absW'}}, {'$project': {'_id': 0}}]))
#     return jsonify({'result': 'success', 'absW_list': abs_ws})
#
#
# @app.route('/w/hip', methods=['GET'])
# def show_hipW():
#     hip_ws = list(
#         db.myproject.aggregate([{'$match': {'subCAT': 'hipW'}}, {'$project': {'_id': 0}}]))
#     return jsonify({'result': 'success', 'hipW_list': hip_ws})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
