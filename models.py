from config import db

class Conversa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50))
    mensagens = db.relationship('MensagensConversa')

class MensagensConversa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input = db.Column(db.String(300))
    output = db.Column(db.String(500))
    conversa_id = db.Column(db.Integer, db.ForeignKey('conversa.id'))
