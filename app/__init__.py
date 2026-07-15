from flask import Flask

from app.database import init_database


def create_app():
    app = Flask(__name__)

    init_database()

    from app.routes import main
    app.register_blueprint(main)

    return app
