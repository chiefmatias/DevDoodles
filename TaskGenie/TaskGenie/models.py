from TaskGenie import db
from datetime import date


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)    
    title = db.Column(db.String(80), nullable=False)
    due = db.Column(db.Date, nullable=False, default=date.today)
    priority = db.Column(db.String(10), nullable=False)
    description = db.Column(db.Text, nullable=False)  # description is not required
    completed = db.Column(db.Boolean, nullable=False, default=False)
    
    @property
    def formatted_due(self):
        return self.due.strftime("%d-%m-%Y")

    def __repr__(self) -> str:
        return (
            f"Task({self.title}, is due {self.due}, "
            f"with {self.priority} priority. "
            f"Description: {self.description})"
        )


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    tasks = db.relationship('Task', backref='list', lazy=True)