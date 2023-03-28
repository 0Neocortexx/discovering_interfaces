from model import app, User, db
from flask import request, jsonify
import bcrypt

def criptpass(senha:str):
    senha = senha["utf-8"]
    senha = bcrypt.hashpw(senha, bcrypt.gensalt(8))
    return senha

@app.route('/')
def home():
    return 'aline gostosa'

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return 'cadastro'
    else:    
        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
        dados = request.get_json(force=True)
        senha = criptpass(dados["senha"])
        try:
            user = User(email = dados["email"].lower(), nome = dados["nome"].lower(), senha = senha, data_nasc = "2004-13-04")        
            db.session.add(user)
            db.session.commit()
            resposta = jsonify({"resultado":"ok", "resposta": "Usuário cadastrado com sucesso!"})
        except Exception as e:
            resposta = jsonify({"resultado": "erro", "resposta": str(e)})
        
        resposta.headers.add('Access-Control-Allow-Origin', '*')
        return resposta


app.run(debug=True, host=('0.0.0.0'))