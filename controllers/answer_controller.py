from flask import Blueprint, render_template, redirect, request
from models.question_mgmt import Question
from models.answer_mgmt import Answer

answer_bp = Blueprint('answer', __name__, url_prefix='/answer')


@answer_bp.route("/create", methods=['POST'])
def create():
    q_id = request.form['q_id']
    content = request.form['content']
    result = Answer.create(q_id, content)

    return redirect('/board/detail/%s' % q_id)
