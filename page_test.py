from pymongo import MongoClient

from flask import Flask, render_template, jsonify

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

PER_PAGE_CNT = 6

# # 1. 전체 게시글의 갯수
# @app.route('/st/fullbody', methods=['GET'])
# def show_fullbodyST():

total_cnt = db.myproject.find({'subCAT': 'fullbodyST'}).count()
page_cnt = int(total_cnt / PER_PAGE_CNT)
if total_cnt % PER_PAGE_CNT != 0:
    page_cnt += 1
    for page_num in range(page_cnt - 1):
        start_idx = page_num * PER_PAGE_CNT + 1
        end_idx = (page_num + 1) * PER_PAGE_CNT
        int(start_idx)
        int(end_idx)
        # print(start_idx, end_idx)
        fullbody_sts = list(db.myproject.aggregate(
            [{'$match': {'subCAT': 'fullbodyST'}}, {'$limit': end_idx}, {'$skip': start_idx - 1}]))
        print(fullbody_sts)

        # for fullbody_st in fullbody_sts:
        #     print(fullbody_st)
        # return jsonify({'result': 'success', 'fullbodyST_list': fullbody_sts})

# print(start_idx, end_idx)
# last_id=int(end_idx)
#  {'$project': {'_id': 0}},
# fullbody_sts = list(db.myproject.find().skip(6).limit(6))
# for fullbody_st in fullbody_sts:
#     print(fullbody_st)

# fullbody_sts = list(db.myproject.aggregate([{'$match': {'subCAT': 'fullbodyST'}}, {'$project': {'_id': 0}}]))
# for fullbody_st in fullbody_sts:
#     print(fullbody_st)
# for fullbody_st in range('end_idx'):
#     start_idx = page_num * PER_PAGE_CNT + 1
#     end_idx = (page_num + 1) * PER_PAGE_CNT
#     print(start_idx, end_idx)

#
#     fullbody_sts = list(
#         db.myproject.aggregate([{'$match': {'subCAT': 'fullbodyST'}}, {'$project': {'_id': 0}}]))
#     # db.Employee.find().limit(2)
#     return jsonify({'result': 'success', 'fullbodyST_list': fullbody_sts})
#     # fullbodySTs = list(db.myproject.find({}, {"subCAT": "fullbodyST"}).sort([{"_id": 1}]))
#     # fullbodySTs = list(db.myproject.find({"subCAT": "fullbodyST"},{'videoId':1}))
#
# total_cnt = 106
# # pymongo list count
#
# PER_PAGE_CNT = 10
#
# page_cnt = int(total_cnt / PER_PAGE_CNT)
# if total_cnt % PER_PAGE_CNT != 0:
#     page_cnt += 1
#
# # (1,10) (11,20) (21,30) (31,40) (41,50) ....
# # page_num = 1
# #
# # start_idx = 1 = (page_num - 1) * per_page_cnt + 1
# # end_idx = 10 = page_num * per_page_cnt
#
# # .sort(start_idx~end_idx)
#
# # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# for page_num in range(page_cnt - 1):
#     start_idx = page_num * PER_PAGE_CNT + 1
#     end_idx = (page_num + 1) * PER_PAGE_CNT
#     print(start_idx, end_idx)
#
# # sort(end_idx + 1 ~ total_cnt)
#
#
# ####### api
# # click 1 -> /list?page=1
#
# # page = requests.args.get('page')
# # page -> 1
#
# # click 2 -> /list?page=2
# # page = requests.args.get('page')
# # page -> 2
# page = 2
#
# def calIdx(page_num):
#     start_idx = page_num * PER_PAGE_CNT + 1
#     end_idx = (page_num + 1) * PER_PAGE_CNT
#     print(start_idx, end_idx)
#
#     return start_idx,end_idx

# pymongo (start_idx~end_idx)
