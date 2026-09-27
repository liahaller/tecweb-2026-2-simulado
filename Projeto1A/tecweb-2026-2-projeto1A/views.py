from database import Database
from random import randint
import locale
import datetime
from utils import add_note, load_data, load_template, build_response, extract_params


def index(request):
    erro = ''
    cores = ['#DAF7A6','#FFC300','#FF5733','#C70039','#900C3F','#581845']
    i = randint(0,5)
    cor = cores[i]
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        params = extract_params(request)

        # Monta a nova anotação e a adiciona ao banco de dados
        nova_anotacao = {
            'titulo': params['titulo'].strip(),
            'detalhes': params['detalhes'].strip(),
        }
        if not nova_anotacao['titulo'] or not nova_anotacao['detalhes']:
            erro = '<p class="erro">Preencha o título e o conteúdo da anotação.</p>'
        else:
            add_note(nova_anotacao)
            return build_response(code=303, headers='Location: /')

    # Cria uma lista de <li>'s para cada anotação
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id=dados.id, title=dados.title, details=dados.content,
                             estrela='★' if dados.favorite else '☆')
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)
    body = load_template('index.html').format(notes=notes, erro=erro, cor=cor)

    return build_response(body=body)


def confirm_delete(indice):
    database = Database('notes')
    nota = database.get_by_id(indice)
    if nota is None:
        return build_response(code=303, headers='Location: /')
    return build_response(body=load_template('delete.html').format(
        id=nota.id, title=nota.title, details=nota.content))


def delete_note(indice):
    database = Database('notes')
    database.delete(indice)
    return build_response(code=303, headers='Location: /')


def edit_note(indice):
    database = Database('notes')
    nota = database.get_by_id(indice)
    if nota is None:
        return build_response(code=303, headers='Location: /')
    return build_response(body=load_template('edit.html').format(
        id=nota.id, title=nota.title, details=nota.content))


def update_note(indice, request):
    params = extract_params(request)
    database = Database('notes')
    nota = database.get_by_id(indice)
    nota.title = params['titulo']
    nota.content = params['detalhes']
    database.update(nota)
    return build_response(code=303, headers='Location: /')


def edit(request, indice):
    if request.startswith('POST'):
        return update_note(indice, request)
    return edit_note(indice)


def delete(request, indice):
    if request.startswith('POST'):
        return delete_note(indice)
    return confirm_delete(indice)


def favorite(request, indice):
    database = Database('notes')
    nota = database.get_by_id(indice)
    if nota is None:
        return build_response(code=303, headers='Location: /')
    nota.favorite = 0 if nota.favorite else 1
    database.update(nota)
    return build_response(code=303, headers='Location: /')

def hoje(request):
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    hoje = datetime.datetime.now()
    #Formatar a data por extenso
    data_em_extenso = hoje.strftime('%A, %d de %B de %Y')
    return build_response(body=load_template('hoje.html').format(data=data_em_extenso))

def not_found():
    return build_response(body=load_template('404.html'), code=404, reason='Not Found')
