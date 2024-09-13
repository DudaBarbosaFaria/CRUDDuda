from database import db

class Eventos(db.Model):
    __tablename__= "eventos"
    id_eventos = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    data = db.Column(db.Date)
    local = db.Column(db.String(10))

    def __init__(self, nome, data, local):
        self.nome = nome
        self.data = data
        self.local = local

    def __repr__(self):
        return "<Nome do Evento: {}>".format(self.nome)
