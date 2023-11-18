import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("TASKGENIE_SECRET")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("TASKGENIE_DATABASE_URL") #"sqlite:///sqlitedb.file"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    csrf = CSRFProtect(app)
    csrf.init_app(app)
    db.init_app(app)

    from TaskGenie.main.routes import main
    from TaskGenie.tasks.routes import tasks
    from TaskGenie.lists.routes import lists

    app.register_blueprint(main)
    app.register_blueprint(tasks)
    app.register_blueprint(lists)
    return app

