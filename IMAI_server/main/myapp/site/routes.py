from flask import Blueprint

site = Blueprint('site', __name__)

##기본페이지
@site.route('/')
def index():
    return "<h1>기본페이지</h2>"
##메인 출력문