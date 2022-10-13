from model import Pessoa
from tinydb import TinyDB, Query
import pandas as pd

bd = TinyDB("Pessoas.json")
usuario = Query()


def inserir(model: Pessoa):
    '''Insere um modelo no banco de dados'''
    bd.insert({"Nome": model.nome,
               "email": model.email,
               "senha": model.senha})


def mostrarTodos():
    '''Mostra todos os contatos cadastrados no banco de dados'''

    todos = bd.all()
    return todos


def deletarPessoa(nome: str):
    '''Busca um CPF e deleta o registro do modelo encontrado'''
    if bd.search(usuario.nome == str(nome)):
        bd.remove(usuario.nome == str(nome))
    else:
        print("Usuário não encontrado")


def atualizarPessoa(nome: str, model: Pessoa):
    """Atualiza um modelo no banco de dados"""
    if bd.search(usuario.nome == str(nome)):
        bd.remove(usuario.nome == str(nome))
        inserir(model)
    else:
        print("Esse usuário não existe")


def mostrarTabelaTodos():
    todos = pd.DataFrame(bd)
    return todos.to_html()


def buscar_nome(nome):
    return bd.search(usuario.nome == str(nome))


def count():
    total_cadastrado = len(bd.all())
    return total_cadastrado
