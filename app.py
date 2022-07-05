from flask import Flask


def create_app():
    app = Flask(__name__, static_url_path='/static')

    from controllers import main_controller, board_controller, answer_controller
    app.register_blueprint(main_controller.main_bp)
    app.register_blueprint(board_controller.board_bp)
    app.register_blueprint(answer_controller.answer_bp)

    if __name__ == "__main__":
        app.run(debug=True)

    return app


create_app()