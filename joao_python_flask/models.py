from database import db

class Projeto(db.Model):
    __tablename__="projeto"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    data_inicio = db.Column(db.Date)
    data_termino = db.Column(db.Date)
    #construtor
    def __init__(self, nome, data_inicio, data_termino):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_termino = data_termino
    # representação do objeto
    def __rep__(self):
        return "<projeto {}>".format(self.nome)