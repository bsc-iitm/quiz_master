from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .subject import Subject
from .chapter import Chapter
from .quiz import Quiz
from .question import Question
from .score import Score
