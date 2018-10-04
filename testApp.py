from flask import Flask, request
from flask_restful import Api, Resource

import logging
from logging.handlers import TimedRotatingFileHandler

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


formatter = logging.Formatter('%(name)-12s %(asctime)s level-%(levelname)-8s thread-%(thread)-8d %(message)s')   # 每行日志的前缀设置
log = logging.getLogger('api')
fileTimeHandler = TimedRotatingFileHandler("logs/api_", "S", 1, 10)
fileTimeHandler.suffix = "%Y%m%d.log"  #设置 切分后日志文件名的时间格式 默认 filename+"." + suffix 如果需要更改需要改logging 源码
fileTimeHandler.setFormatter(formatter)
logging.basicConfig(level = logging.INFO)
fileTimeHandler.setFormatter(formatter)
log.addHandler(fileTimeHandler)



class PopularEvents(Resource):
    def get(self):
        return databaseOperations.getPopularEvents()

class FavoriteEvents(Resource):
    def get(self):
        UserID = request.args.get("userid")
        return databaseOperations.getUserFavoriteEvents(UserID)
    def post(self):
        action = request.args.get("action")
        postJSON = request.get_data().decode("utf-8")

        if action == "add":
            databaseOperations.replaceIntoDB("Favorite", postJSON)
        if action == "delete":
            databaseOperations.deleteFromDB("Favorite", postJSON)
        return postJSON






class SISTEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("SIST")

    def post(self):
        postPassword = request.args.get("password")

        if postPassword != "SIST":
            return "Invalid username or password"

        print("Right password")
        postJSON = request.get_data().decode("utf-8")
        print(postJSON)
        databaseOperations.replaceIntoDB("SIST", postJSON)
        return postJSON





class GECEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("GEC")
class SLSTEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("SLST")
class SPSTEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("SPST")
class SEMEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("SEM")
class SCAEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("SCA")
class IMSEvents(Resource):
    def get(self):
        return databaseOperations.getFourteenDaysEvents("IMS")





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
        return user_info


api.add_resource(Login, '/login', endpoint="login")
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
