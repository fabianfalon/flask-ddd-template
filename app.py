import sys

from flask import Flask

from src.app.injections.containers import Containers
from src.app.routes.course import blueprint as course_blueprint
from src.app.configurator.config import init_app


def create_app() -> Flask:
    app = Flask(__name__)

    container = Containers()
    container.init_resources()
    container.wire(modules=[sys.modules[__name__]])
    app.container = container

    app.secret_key = "very-secret-key"
    with app.app_context():
        init_app(app)
    app.register_blueprint(course_blueprint)
    app.add_url_rule("/", endpoint="index")
    return app
