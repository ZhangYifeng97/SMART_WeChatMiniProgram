from flask import Flask
from flask_restful import Api, Resource
from utils import databaseOperations


############################################################################
# This HAS to be False if we are actually running it instead of testing it #
############################################################################
debugBool = False

app = Flask(__name__)
api = Api(app)


class SISTEvents(Resource):
    def get(self):
        databaseOperations.updateDB("SIST")
        return databaseOperations.getDataFromDB("SIST")

    def put(self):
        # Need a textbox here
        pass

    def delete(self):
        # Need a textbox here
        pass

class GECEvents(Resource):
    def get(self):
        databaseOperations.updateDB("GEC")
        return databaseOperations.getDataFromDB("GEC")
class SLSTEvents(Resource):
    def get(self):
        databaseOperations.updateDB("SLST")
        return databaseOperations.getDataFromDB("SLST")
class SPSTEvents(Resource):
    def get(self):
        databaseOperations.updateDB("SPST")
        return databaseOperations.getDataFromDB("SPST")
class SEMEvents(Resource):
    def get(self):
        databaseOperations.updateDB("SEM")
        return databaseOperations.getDataFromDB("SEM")
class SCAEvents(Resource):
    def get(self):
        databaseOperations.updateDB("SCA")
        return databaseOperations.getDataFromDB("SCA")
class IMSEvents(Resource):
    def get(self):
        databaseOperations.updateDB("IMS")
        return databaseOperations.getDataFromDB("IMS")






api.add_resource(GECEvents, '/events/GEC')
api.add_resource(SISTEvents, '/events/SIST')
api.add_resource(SLSTEvents, '/events/SLST')
api.add_resource(SPSTEvents, '/events/SPST')
api.add_resource(SEMEvents, '/events/SEM')
api.add_resource(SCAEvents, '/events/SCA')
api.add_resource(IMSEvents, '/events/IMS')


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
    app.run(debug=debugBool, host="0.0.0.0", port=80)
