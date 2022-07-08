from flask import Blueprint, render_template, redirect, request
from models.question_model import Question
from models.answer_model import Answer

answer_bp = Blueprint('answer', __name__, url_prefix='/answer')


@answer_bp.route("/create", methods=['POST'])
def create():
    q_id = request.form['q_id']
    content = request.form['content']
    result = Answer.create(q_id, content)
    # 예외 처리 해야함
    if result:
        return redirect('/board/detail/%s' % q_id)
    return render_template('board.html')
