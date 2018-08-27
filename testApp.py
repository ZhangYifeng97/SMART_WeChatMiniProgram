from flask import Flask, request
from flask_restful import Api, Resource

import logging
from logging.handlers import RotatingFileHandler

from utils import databaseOperations

from weixin import WXAPPAPI
from weixin.lib.wxcrypt import WXBizDataCrypt


Users = {"SIST": "SIST"}

APP_ID = "wx2f288f8d6e59cb0c"
APP_SECRET = "e8f76ec53056679cbdcb733e1015bb56"


############################################################################
# This HAS to be False if we are actually running it instead of testing it #
############################################################################
debugBool = False

app = Flask(__name__)
api = Api(app)



class PopularEvents(Resource):
    def get(self):
        return databaseOperations.getPopularEvents()

class FavoriteEvents(Resource):
    def get(self):
        UserID = request.args.get("UserID")
        return databaseOperations.getUserFavoriteEvents(UserID)
    def post(self):
        postJSON = {}
        postJSON["UserID"] = request.args.get("UserID")
        postJSON["BeginTime"] = request.args.get("BeginTime")
        postJSON["Date"] = request.args.get("Date")
        postJSON["Location"] = request.args.get("Location")
        databaseOperations.updateDB("Favorite", postJSON)
        return postJSON






class SISTEvents(Resource):
    def get(self):
        return databaseOperations.getDataFromDB("SIST")

    def post(self):
        postPassword = request.args.get("password")

        if postPassword != "SIST":
            return "Invalid username or password"

        print("Right password")
        postJSON = request.get_data().decode("utf-8")
        print(postJSON)
        databaseOperations.updateDB("SIST", postJSON)
        return postJSON





class GECEvents(Resource):
    def get(self):
        return databaseOperations.getDataFromDB("GEC")
class SLSTEvents(Resource):
    def get(self):
        return databaseOperations.getDataFromDB("SLST")
class SPSTEvents(Resource):
    def get(self):
        return databaseOperations.getDataFromDB("SPST")
class SEMEvents(Resource):
    def get(self):
        return databaseOperations.getDataFromDB("SEM")
class SCAEvents(Resource):
    def get(self):
        return databaseOperations.getDataFromDB("SCA")
class IMSEvents(Resource):
    def get(self):
        return databaseOperations.getDataFromDB("IMS")





class Login(Resource):
    def get(self):

        wxAPI = WXAPPAPI(appid=APP_ID, app_secret=APP_SECRET)




        code = request.args.get("code")

        ##############################################
        # FIXME: Flask request parser takes + as space
        encrypted_data = request.args.get("encryptedData").replace(" ", "+")
        iv = request.args.get("iv").replace(" ", "+")
        ##############################################






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


api.add_resource(Login, '/login', endpoint="login")
api.add_resource(GECEvents, '/events/GEC')
api.add_resource(SISTEvents, '/events/SIST')
api.add_resource(SLSTEvents, '/events/SLST')
api.add_resource(SPSTEvents, '/events/SPST')
api.add_resource(SEMEvents, '/events/SEM')
api.add_resource(SCAEvents, '/events/SCA')
api.add_resource(IMSEvents, '/events/IMS')
api.add_resource(FavoriteEvents, "/events/Favorite")
api.add_resource(PopularEvents, "/events/Popular")


# class DayEvents(Resource):
#     def get(self, day):
#         return getDataFromDB("SIST")[int(day)]
#
#
# class AllEvents(Resource):
#     def get(self):
#         return getDataFromDB("SIST")
#
#
#
# ## Set up the API route
# api.add_resource(AllEvents, '/events')
# api.add_resource(DayEvents, '/events/<day>')


if __name__ == '__main__':
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=debugBool, host="0.0.0.0", port=5000)
