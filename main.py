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


#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)


    #servidor do heroku

#Conectar com o MySql


#Criando tabela de médias

colunas= "N1 N2 N3 N4".split()
linhas= "{nome_usuario}".split()
dados= np.random.randint (0,10,len(colunas)*len(linhas)).reshape(len(linhas),len(colunas))
tabela= pd.Dataframe(data=dados,index=linhas,columns=colunas)
print (tabela)