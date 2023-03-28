from config import app, User, db
from flask import request, jsonify
import bcrypt
from datetime import date

# Teste da rota cadastro: curl -X POST -d "{\"email\":\"testeemail\", \"nome\":\"testenome\", \"senha\":\"testesenha\"}" http://192.168.100.73:5000/cadastro

def criptpass(senha:str):
    senha = senha["utf-8"]
    senha = bcrypt.hashpw(senha, bcrypt.gensalt(8))
    return senha

def transformar_data(data:list):
    data = data.split()
    print(data)
    data = date(data)
    return data

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
        try:
            user = User(email = dados["email"], nome = dados["nome"], senha = dados["senha"], data_nasc = date(dados["data_nasc"]))        
            db.session.add(user)
            db.session.commit()
            resposta = jsonify({"resultado":"ok", "resposta": "Usuário cadastrado com sucesso!"})
        except Exception as e:
            resposta = jsonify({"resultado": "erro", "resposta": str(e)})
        resposta.headers.add('Access-Control-Allow-Origin', '*')
        return resposta


app.run(debug=True, host=('0.0.0.0'))