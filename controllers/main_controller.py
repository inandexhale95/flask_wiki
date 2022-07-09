from flask import Blueprint, render_template, abort
from flask.views import View

main_bp = Blueprint('main', __name__, url_prefix='/')


@main_bp.route("/index")
@main_bp.route("/")
def index():
    return render_template('index.html')


@main_bp.route("/users")
def users():
    # abort 함수로 에러를 발생 시킨다
    abort(403)


# 에러 처리를 위해 핸들러를 작성
@main_bp.errorhandler(403)
def permission_denied(error):
    return '403', 403
