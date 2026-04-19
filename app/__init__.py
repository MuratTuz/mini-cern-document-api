from flask import Flask
from .database import db

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:password@localhost:5433/docdb"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .models import Document
    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app