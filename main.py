from flask import Flask, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json
import sys
import logging



app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/cadastro'

db = SQLAlchemy(app)

class Usuario(db.model):
    id=db.Column(db.Integer, primary_key=True)
    nome=db.Columm(db.String(50))
    email=db.Columm(db.String(100))
    senha=db.Columm(db.String(20))

db.create_all()
#TERMINA [BANCO DE DADOS]
#---------------------------------------------------------------------------#

#Pra não bugar
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


#criar páginas:
    #route(o caminho)  > #treino.com/users
    #função (o que você quer exibir na página)
    #template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/notas")
def notas():
    return render_template("notas.html")

@app.route("/users/<nome_usuario>")
def users(nome_usuario):
    return render_template("users.html",nome_usuario=nome_usuario)

@app.route ("/login")
def login():
    return render_template("login.html")

@app.route ("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route ("/cadastro_professor")
def cadastro_professor():
    return render_template("cadastro_professor.html")



#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)


