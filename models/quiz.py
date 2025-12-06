from . import db

class Quiz(db.Model):
    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'))
    title = db.Column(db.String(100), nullable=False)
    date_of_quiz = db.Column(db.Date)
    time_duration = db.Column(db.String(10))  # HH:MM
    remarks = db.Column(db.Text)
