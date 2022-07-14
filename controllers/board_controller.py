import math

from flask import Blueprint, render_template, request, redirect, url_for
from models.question_model import Question
from models.answer_model import Answer
from forms.form import QuestionForm, AnswerForm

board_bp = Blueprint('board', __name__, url_prefix='/board')


@board_bp.route("/list", methods=['GET'])
def _list(page=1):
    if request.args.get('page'):
        page = int(request.args.get('page', type=int))
    per_page = 20

    # 총 질문 갯수
    total_question = Question.get_question_count()
    # math.ceil로 소수점을 올림 해준다.
    total_page = math.ceil(total_question / per_page)

    # 페이지 수를 초과하거나 1 미만일 때
    if page > total_page:
        page = total_page
    elif page <= 0:
        page = 1

    page_index = total_question - (page - 1) * per_page
    question_list = Question.get_question_list(per_page, page)
    return render_template('board.html', question_list=question_list, total_page=total_page, page_index=page_index, page=page)


@board_bp.route("/answer/create", methods=['POST'])
@board_bp.route("/detail/<int:q_id>", methods=['GET'])
def detail(q_id: int = 0):
    form = AnswerForm()
    if request.method == 'POST':
        q_id = int(request.form.get('q_id'))
    question = Question.get_question(q_id)
    answer_list = Answer.get_answer_list(q_id)

    if request.method == 'POST' and form.validate_on_submit():
        content = form.content.data
        if Answer.create(q_id, content):
            return redirect('/board/detail/%s' % q_id)
    return render_template('detail.html', question=question, answer_list=answer_list, form=form)


@board_bp.route("/create/", methods=['GET', 'POST'])
def create():
    form = QuestionForm()

    # form.validate_on_submit 함수는 전송된 폼 데이터의 정합성을 점검한다.
    # 즉, QuestionForm 클래스의 각 속성에 지정한 DataRequired() 같은 점검 항목에 이상이 없는지 확인한다.
    if request.method == 'POST' and form.validate_on_submit():
        result = Question.insert(form.subject.data, form.content.data)
        # 예외 처리 해야함
        if result:
            return redirect('/board/list')
    return render_template('board_form.html', form=form)
