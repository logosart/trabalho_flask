
from flask import Flask, render_template
import sys
import logging
import pandas as pd
import numpy as np

app = Flask(__name__)

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


