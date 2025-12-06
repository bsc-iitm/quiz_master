from flask import Flask
from models import db
from controllers.auth_controller import auth_bp
# from controllers.admin_controller import admin_bp
from werkzeug.security import generate_password_hash
from flask_session import Session
from models.user import User
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'quiz.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "quiz_master_secret"
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

db.init_app(app)

app.register_blueprint(auth_bp)
# app.register_blueprint(admin_bp)

with app.app_context():
    db.create_all()
    admin_email = "admin@quizmaster.com"
    if not User.query.filter_by(username=admin_email).first():
        admin = User(
            username=admin_email,
            password=generate_password_hash("admin123"),
            full_name="Quiz Master",
            qualification="Admin",
            role="admin"
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin created: admin@quizmaster.com / admin123")

if __name__ == "__main__":
    app.run(debug=True)
