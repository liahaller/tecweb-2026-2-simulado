from database import Database, Note
from urllib.parse import unquote_plus

def extract_route(string):
    resposta = string.split(" ")
    resposta = resposta[1]
    resposta = resposta[1:]
    return resposta

def read_file(path):
    arquivo = open(path,'rb')
    conteudo = arquivo.read()
    arquivo.close()
    return conteudo

def load_data():
    database = Database('notes')
    return database.get_all()

def load_template(arquivo):
    arquivo_aberto = open('templates/' + arquivo, 'r', encoding='utf-8')
    conteudo = arquivo_aberto.read()
    arquivo_aberto.close()
    return conteudo

def add_note(anotacao):
    database = Database('notes')
    note = Note(title=anotacao['titulo'], content=anotacao['detalhes'])
    database.add(note)

def extract_params(request):
    request = request.replace('\r', '')
    corpo = request.split('\n\n')[1]
    params = {}
    for chave_valor in corpo.split('&'):
        chave, valor = chave_valor.split('=')
        params[chave] = unquote_plus(valor)
    return params

def build_response(body='', code=200, reason='OK', headers=''):
    if headers:
        resposta = f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'
    else:
        resposta = f'HTTP/1.1 {code} {reason}\n\n{body}'
    return resposta.encode()
