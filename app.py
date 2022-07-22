from flask import Flask, redirect
from flask_cors import CORS
from flask_login.login_manager import LoginManager
from models.user_model import User


def create_app():
    app = Flask(__name__,
                static_url_path='/static',
                template_folder='templates')

    from controllers import main_controller, board_controller, auth_controller
    app.register_blueprint(main_controller.main_bp)
    app.register_blueprint(board_controller.board_bp)
    app.register_blueprint(auth_controller.auth_bp)

    from common.filter import format_datetime, answer_count, get_question_writer
    app.jinja_env.filters['datetime'] = format_datetime
    app.jinja_env.filters['answer_count'] = answer_count
    app.jinja_env.filters['get_question_writer'] = get_question_writer

    CORS(app)

    app.secret_key = 'inandexhale_server'

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.session_protection = 'strong'

    # 객체를 반환해야 한다.
    @login_manager.user_loader
    def load_user(user_id):
        try:
            user = User.get_user_for_id(user_id)
            return user
        except:
            return None

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect('/')

    if __name__ == "__main__":
        app.run(debug=True)

    return app


create_app()
