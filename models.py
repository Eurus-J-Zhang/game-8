from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    id= db.Column(db.String(20))
    gender=db.Column(db.String(1))
    age = db.Column(db.Integer)

    final_choice = db.Column(db.String(1))

    emo_choice = db.Column(db.String(10))
    feedback = db.Column(db.String(10000))