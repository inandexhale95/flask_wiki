from flask import Blueprint, request, render_template, flash, redirect, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import User
from forms.form import UserCreateForm, UserLoginForm
from flask_login import login_user, login_required, logout_user


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route("/signup", methods=['GET', 'POST'])
def signup():
    form = UserCreateForm()

    if request.method == 'POST' and form.validate_on_submit():
        user_check = User.duplicate_user_check(username=form.username.data)
        email_check = User.duplicate_email_check(email=form.email.data)
        if not user_check and not email_check:
            User.create_user(username=form.username.data,
                             password=generate_password_hash(form.password1.data),
                             email=form.email.data)
            return redirect('/')
        elif user_check:
            flash('이미 존재하는 사용자입니다.')
        elif email_check:
            flash('이미 존재하는 이메일입니다.')

    return render_template('/auth/signup.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.get_user(username=form.username.data)
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user[2], form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            user_object = User(user[0], user[1], user[2], user[3], user[4])
            login_user(user_object)
            return redirect('/')
        flash(error)
    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
