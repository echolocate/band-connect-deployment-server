from application import db

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    bands = db.relationship('Band', backref='agent')
    
class Band(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable = False)
    genre = db.Column(db.String(20), nullable = False)
    members = db.Column(db.Integer, nullable = False, default = 1)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=True)


