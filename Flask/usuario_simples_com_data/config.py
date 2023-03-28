from flask import *
from flask_sqlalchemy import *
import os

app = Flask(__name__)
app.app_context().push()

arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "teste.db")

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+ arquivo
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    email = db.Column(db.String(254), primary_key = True, nullable = False)
    nome = db.Column(db.String(254), nullable = False)
    senha = db.Column(db.String(254), nullable = False)
    data_nasc = db.Column(db.Date)

    def __str__(self):
        return f'Email: {self.email}, Nome: {self.nome}, Senha: {self.senha}, Data de Nascimento: {self.data_nasc}'
    
    def json(self):
        return {
            "email": self.email,
            "nome": self.nome,
            "senha": self.senha,
            "data_nasc": self.data_nasc
        }

if __name__=="__main__":
    db.create_all()