from flask import Blueprint, render_template
from models.question_model import Question

main_bp = Blueprint('main', __name__, url_prefix='/')


@main_bp.route("/")
def index():
    question_list = Question.get_question_list()
    print(question_list)
    return render_template('index.html', question_list=question_list)
