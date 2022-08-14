from flask import Blueprint, request, jsonify

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata',methods=['GET'])
def getdata():
    return "<h1>api sub page</h1>"