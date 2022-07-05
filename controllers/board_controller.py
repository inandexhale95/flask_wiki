from flask import Blueprint, render_template
from models.question_mgmt import Question
from models.answer_mgmt import Answer

main_bp = Blueprint('board', __name__, url_prefix='/board')


@main_bp.route("/list")
def index():
    question_list = Question.get_question_list()
    print(question_list)
    return render_template('board.html', question_list=question_list)


@main_bp.route("/detail/<int:q_id>")
def detail(q_id):
    question = Question.get_question(q_id)
    answer_list = Answer.get_answer_list(q_id)
    # print(question.q_id, type(question.subject), question.content, question.create_date)
    return render_template('detail.html', question=question, answer_list=answer_list)
