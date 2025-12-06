from . import db
from datetime import datetime

class Score(db.Model):
    __tablename__ = 'score'

    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    score = db.Column(db.Integer)
    attempt_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_questions = db.Column(db.Integer)
    correct_answers = db.Column(db.Integer)
