from flask import Flask, request
from flask_restful import Api, Resource

import logging
from logging.handlers import RotatingFileHandler

from utils import databaseOperations

from weixin import WXAPPAPI
from weixin.lib.wxcrypt import WXBizDataCrypt


import json

Users = {"SIST": "SIST"}

APP_ID = "wx2f288f8d6e59cb0c"
APP_SECRET = "e8f76ec53056679cbdcb733e1015bb56"


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
        postPassword = request.args.get("password")

        if postPassword != "SIST":
            return "Invalid username or password"

        print("Right password")
        postJSON = json.loads(request.get_data())
        print(postJSON)
        databaseOperations.replaceIntoDB("SIST", postJSON)
        return postJSON





class GECEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("GEC")
    
    def post(self):
        postJSON = json.loads(request.get_data())
        databaseOperations.replaceIntoDB("GEC", postJSON)
        return postJSON

class SLSTEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("SLST")
    def post(self):
        postJSON = json.loads(request.get_data())
        databaseOperations.replaceIntoDB("SLST", postJSON)
        return postJSON

class SPSTEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("SPST")
    def post(self):
        postJSON = json.loads(request.get_data())
        databaseOperations.replaceIntoDB("SPST", postJSON)
        return postJSON

class SEMEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("SEM")
    def post(self):
        postJSON = json.loads(request.get_data())
        databaseOperations.replaceIntoDB("SEM", postJSON)
        return postJSON

class SCAEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("SCA")
    def post(self):
        postJSON = json.loads(request.get_data())
        databaseOperations.replaceIntoDB("SCA", postJSON)
        return postJSON

class IMSEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("IMS")
    def post(self):
        postJSON = json.loads(request.get_data())
        databaseOperations.replaceIntoDB("IMS", postJSON)
        return postJSON





class Login(Resource):
    def get(self):
        wxAPI = WXAPPAPI(appid=APP_ID, app_secret=APP_SECRET)


        data = request.get_data()
        print(data)
        loginJSON = json.loads(data)
        code = loginJSON["code"]
        encrypted_data = loginJSON["encryptedData"]
        iv = loginJSON["iv"]







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
        user_info = crypt.decrypt(encrypted_data, iv)
        print("\nuserinfo: ", user_info)
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
    app.run(debug=debugBool, host="0.0.0.0", port=80)
