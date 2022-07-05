from flask import Blueprint, render_template, request
from models.question_mgmt import Question
from models.answer_mgmt import Answer

board_bp = Blueprint('board', __name__, url_prefix='/board')


@board_bp.route("/list", methods=['GET'])
def index():
    question_list = Question.get_question_list()
    print(question_list)
    return render_template('board.html', question_list=question_list)


@board_bp.route("/detail/<int:q_id>", methods=['GET'])
def detail(q_id):
    question = Question.get_question(q_id)
    answer_list = Answer.get_answer_list(q_id)
    return render_template('detail.html', question=question, answer_list=answer_list)
