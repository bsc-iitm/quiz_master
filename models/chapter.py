from . import db

class Chapter(db.Model):
    __tablename__ = 'chapter'

    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
