# coding=utf-8
from flask import Flask, request
from flask_restful import Api, Resource

import logging
from logging.handlers import RotatingFileHandler

from utils import databaseOperations, stringParsing


from weixin import WXAPPAPI
from weixin.lib.wxcrypt import WXBizDataCrypt


import json


APP_ID = "wx8d674a9d2410f0f4"
APP_SECRET = "0b28ad89ec979b784d74779c2db064da"


############################################################################
# This HAS to be False if we are actually running it instead of testing it #
############################################################################
debugBool = False

app = Flask(__name__)
api = Api(app)


handler = RotatingFileHandler('log.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)


class PopularEvents(Resource):
    def get(self):
        return databaseOperations.getPopularEvents()

class FavoriteEvents(Resource):
    def get(self):
        UserID = request.args.get("userid")
        return databaseOperations.getUserFavoriteEvents(UserID)
    def post(self):
        action = request.args.get("action")
        postJSON = json.loads(request.get_data())

        if action == "add":
            databaseOperations.replaceIntoDB("Favorite", postJSON)
        if action == "delete":
            databaseOperations.deleteFromDB("Favorite", postJSON)
        print(postJSON)
        return postJSON






class SISTEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("SIST")

    def post(self):
        action = request.args.get("action")
        postJSON = json.loads(request.get_data())


        if action == "add":
            databaseOperations.replaceIntoDB("Events", postJSON)
        if action == "delete":
            databaseOperations.deleteFromDB("Events", postJSON)
        print(postJSON)
        return postJSON



class GECEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("GEC")
    
    def post(self):
        action = request.args.get("action")
        postJSON = json.loads(request.get_data())


        if action == "add":
            databaseOperations.replaceIntoDB("Events", postJSON)
        if action == "delete":
            databaseOperations.deleteFromDB("Events", postJSON)
        print(postJSON)
        return postJSON


class SLSTEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("SLST")
    def post(self):
        action = request.args.get("action")
        postJSON = json.loads(request.get_data())


        if action == "add":
            databaseOperations.replaceIntoDB("Events", postJSON)
        if action == "delete":
            databaseOperations.deleteFromDB("Events", postJSON)
        print(postJSON)
        return postJSON


class SPSTEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("SPST")
    def post(self):
        action = request.args.get("action")
        postJSON = json.loads(request.get_data())


        if action == "add":
            databaseOperations.replaceIntoDB("Events", postJSON)
        if action == "delete":
            databaseOperations.deleteFromDB("Events", postJSON)
        print(postJSON)
        return postJSON


class SEMEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("SEM")
    def post(self):
        action = request.args.get("action")
        postJSON = json.loads(request.get_data())


        if action == "add":
            databaseOperations.replaceIntoDB("Events", postJSON)
        if action == "delete":
            databaseOperations.deleteFromDB("Events", postJSON)
        print(postJSON)
        return postJSON


class SCAEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("SCA")
    def post(self):
        action = request.args.get("action")
        postJSON = json.loads(request.get_data())


        if action == "add":
            databaseOperations.replaceIntoDB("Events", postJSON)
        if action == "delete":
            databaseOperations.deleteFromDB("Events", postJSON)
        print(postJSON)
        return postJSON


class IMSEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("IMS")
    def post(self):
        action = request.args.get("action")
        postJSON = json.loads(request.get_data())

        if action == "add":
            databaseOperations.replaceIntoDB("Events", postJSON)
        if action == "delete":
            databaseOperations.deleteFromDB("Events", postJSON)
        print(postJSON)
        return postJSON






class Login(Resource):
    def get(self):
        wxAPI = WXAPPAPI(appid=APP_ID, app_secret=APP_SECRET)

        print("string is: ", request.query_string)

        
    

        # BLACK MAGIC
        ##############################################
        # FIXME: Flask request parser takes + as space
        encrypted_data = request.args.get("encryptedData").replace(" ", "+")
        iv = request.args.get("iv").replace(" ", "+")
        ##############################################


        code = request.args.get("code")




        # print(data)
        # loginJSON = json.loads(data)
        # code = loginJSON["code"]
        # encrypted_data = loginJSON["encryptedData"]
        # iv = loginJSON["iv"]







        print("\ncode is : ", code)
        print("\ndata is : ", encrypted_data)
        print("\niv is : ", iv)



        session_info = wxAPI.exchange_code_for_session_key(code=code)



        # 获取session_info 后

        session_key = session_info.get('session_key')
        crypt = WXBizDataCrypt(APP_ID, session_key)

        # encrypted_data 包括敏感数据在内的完整用户信息的加密数据
        # iv 加密算法的初始向量
        # 这两个参数需要js获取
        try:
            user_info = crypt.decrypt(encrypted_data, iv)
            postJSON = stringParsing.userInfo2SQL(user_info)
            databaseOperations.replaceIntoDB("Users", postJSON)
        except:
            user_info = {"openId": session_info.get('openid')}
        return user_info







api.add_resource(Login, '/login')
api.add_resource(GECEvents, '/events/GEC')
api.add_resource(SISTEvents, '/events/SIST')
api.add_resource(SLSTEvents, '/events/SLST')
api.add_resource(SPSTEvents, '/events/SPST')
api.add_resource(SEMEvents, '/events/SEM')
api.add_resource(SCAEvents, '/events/SCA')
api.add_resource(IMSEvents, '/events/IMS')
api.add_resource(FavoriteEvents, "/events/favorite")
api.add_resource(PopularEvents, "/events/popular")


# class DayEvents(Resource):
#     def get(self, day):
#         return getFourteenDaysEvents("SIST")[int(day)]
#
#
# class AllEvents(Resource):
#     def get(self):
#         return getFourteenDaysEvents("SIST")
#
#
#
# ## Set up the API route
# api.add_resource(AllEvents, '/events')
# api.add_resource(DayEvents, '/events/<day>')


if __name__ == '__main__':
    app.run(debug=debugBool, host="0.0.0.0", port=5000)
