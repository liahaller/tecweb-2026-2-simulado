# Guia de estudo: Tecnologias Web (Avaliação Intermediária)

> **Como usar este README**
> - As seções 1 a 6 são o **resumo** da matéria (comandos, conceitos e como os seus projetos funcionam).
> - A seção 7 tem o **enunciado resumido do simulado**.
> - A seção 8 tem a **resolução do simulado**, escondida em blocos recolhidos (clique em "▶" para abrir). **Só abra quando quiser conferir.**
> - Mais embaixo estão as instruções e regras originais da prova.

## Sumário

1. [Mapa da matéria](#1-mapa-da-matéria)
2. [Comandos de terminal](#2-comandos-de-terminal)
3. [Conceitos de HTTP que caem em tudo](#3-conceitos-de-http-que-caem-em-tudo)
4. [Projeto 1A: servidor "na mão" com socket](#4-projeto-1a-servidor-na-mão-com-socket)
5. [Projeto 1B: Django](#5-projeto-1b-django)
6. [Erros comuns e como resolver](#6-erros-comuns-e-como-resolver)
7. [Simulado: enunciado resumido](#7-simulado-enunciado-resumido)
8. [Resolução do simulado (spoiler)](#8-resolução-do-simulado-spoiler)
9. [Checklist para o dia da prova](#9-checklist-para-o-dia-da-prova)

---

## 1. Mapa da matéria

Site: https://barbaratieko.github.io/tecweb/

| Aula | Tema | O que importa para a prova |
|---|---|---|
| 01 | Get-it (servidor com `socket`) | Base do **Projeto 1A**: rotas, request/response, templates |
| 02 | Desafio CSS | Classes, seletores, `background-color` |
| 03 | Persistência de dados | SQLite com `sqlite3` (o `database.py` do 1A) |
| 04 | Django | Base do **Projeto 1B**: models, migrations, views, urls, templates, formulários |
| 05 | Containers e BD | Docker + PostgreSQL (na prova usamos **SQLite**) |
| 06 | Deploy | Render (na prova: `DEBUG = True` e SQLite) |
| 07 | JavaScript | `getit.js` (a prova do simulado **proíbe** JS para mudar cor) |

**Formato da prova (igual ao simulado):**
- **Questão 1**: adicionar funcionalidades no **Projeto 1A** (servidor Python puro, porta **8080**).
- **Questão 2**: adicionar funcionalidades no **Projeto 1B** (Django, porta **8000**).
- Cada etapa pede um **commit com uma mensagem específica**. Não esqueça!
- **Não pode quebrar** o que já funcionava, só **adicionar**.

---

## 2. Comandos de terminal

> Os exemplos usam **PowerShell** (terminal padrão do VS Code no Windows). Quando for diferente no Git Bash, está indicado.

### 2.1 Navegar até as pastas

```powershell
# Raiz do repositório (onde fica o .git e este README)
cd "C:\Users\liaha\OneDrive\Área de Trabalho\4° semestre\Tecnologias web\tecweb-2026-2-simulado"

# Projeto 1A
cd Projeto1A\tecweb-2026-2-projeto1A

# Projeto 1B
cd Projeto1B\tecweb-2026-2-projeto1B

# Voltar uma pasta
cd ..
```

Dica: no VS Code, clique com o botão direito numa pasta e escolha **"Open in Integrated Terminal"**.

### 2.2 Projeto 1A (não usa ambiente virtual, só Python puro)

```powershell
cd Projeto1A\tecweb-2026-2-projeto1A
python servidor.py            # sobe o servidor em http://localhost:8080
# Ctrl + C                    # para o servidor
python -m pytest test_utils.py   # roda os testes das funções de utils.py
```

⚠️ **Rode sempre de dentro da pasta `tecweb-2026-2-projeto1A`**, porque `load_template` abre `'templates/' + arquivo` e o banco é `notes.db`, ambos com caminho **relativo**.

⚠️ **Toda vez que alterar um `.py`, pare (Ctrl+C) e rode `python servidor.py` de novo.** O servidor do 1A não recarrega sozinho. Templates `.html` são lidos a cada request, então esses não exigem reiniciar.

⚠️ Se aparecer `OSError: [WinError 10048]` (porta em uso), já tem um servidor rodando em outro terminal. Feche-o.

### 2.3 Projeto 1B (Django, com ambiente virtual `env`)

```powershell
cd Projeto1B\tecweb-2026-2-projeto1B

# ATIVAR o ambiente virtual (aparece "(env)" no começo da linha)
.\env\Scripts\Activate.ps1          # PowerShell
# source env/Scripts/activate       # Git Bash
# env\Scripts\activate.bat          # cmd

# Se o PowerShell reclamar de "execução de scripts desabilitada":
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

deactivate                          # desativa o ambiente virtual
```

Criar/instalar do zero (caso precise):

```powershell
python -m venv env                  # cria o ambiente virtual na pasta env
.\env\Scripts\Activate.ps1
pip install -r requirements.txt     # instala as dependências
pip list                            # confere o que está instalado
pip freeze > requirements.txt       # salva as dependências
```

Comandos do Django (sempre com o `env` ativado e dentro da pasta que tem o `manage.py`):

| Comando | Para que serve |
|---|---|
| `python manage.py runserver` | Sobe o servidor em http://localhost:8000 (recarrega sozinho ao salvar) |
| `python manage.py makemigrations` | **Gera** o arquivo de migração a partir das mudanças em `models.py` |
| `python manage.py migrate` | **Aplica** as migrações no banco (`db.sqlite3`) |
| `python manage.py showmigrations` | Lista as migrações e quais já foram aplicadas (`[X]`) |
| `python manage.py createsuperuser` | Cria usuário para o `/admin` |
| `python manage.py shell` | Terminal Python com acesso aos models |
| `python manage.py check` | Procura erros de configuração sem subir o servidor |
| `django-admin startproject getit .` | Cria um projeto (já feito) |
| `python manage.py startapp notes` | Cria um app (já feito) |

> **Mudou `models.py`? Então SEMPRE: `makemigrations` → `migrate`.** Os dois, nessa ordem.

### 2.4 Git (commits pedidos na prova)

Os commits são feitos **na raiz do repositório** (a pasta que tem o `.git`), mas os comandos funcionam de qualquer subpasta.

```powershell
git status                              # o que mudou?
git add .                               # adiciona tudo que mudou
git commit -m "Adicionando data de hoje"   # commit com a mensagem EXATA do enunciado
git log --oneline                       # confere os commits feitos
git push                                # envia para o GitHub (se a prova pedir)
```

- Use **exatamente** a mensagem pedida no enunciado (acentos inclusive).
- O `.gitignore` da raiz já ignora `env/`, `__pycache__/` e `.pytest_cache/`.
- Rode `git status` antes do `add` para garantir que não está indo nada estranho.

---

## 3. Conceitos de HTTP que caem em tudo

**Request (requisição)** é o que o navegador manda. A primeira linha diz o método e a rota:

```
GET /edit/3 HTTP/1.1          ← método, rota, versão
Host: localhost:8080
...                           ← cabeçalhos
                              ← linha em branco
titulo=Oi&detalhes=Tudo+bem   ← corpo (só no POST)
```

**Response (resposta)** é o que o servidor devolve:

```
HTTP/1.1 200 OK               ← status
Content-Type: text/html       ← cabeçalhos (opcionais)
                              ← linha em branco
<html>...</html>              ← corpo
```

| Conceito | Resumo |
|---|---|
| **GET** | Pedir uma página. Acontece ao digitar a URL ou clicar num link. |
| **POST** | Enviar dados. Acontece ao submeter um `<form method="post">`. |
| **200 OK** | Deu certo. |
| **302 / 303** | **Redirect**: manda o navegador ir para a URL do cabeçalho `Location`. Usado depois de um POST para não reenviar o formulário ao dar F5. |
| **404 Not Found** | Rota não existe. |
| `name` do input | Vira a **chave** do dado enviado: `<input name="titulo">` envia `titulo=...` |
| Formulário | `<form method="post" action="/rota">` + inputs com `name` + botão `type="submit"` |

---

## 4. Projeto 1A: servidor "na mão" com socket

### 4.1 Arquivos

| Arquivo | Papel |
|---|---|
| `servidor.py` | Abre o socket na porta 8080, recebe a request, **decide qual view chamar** pela rota e devolve a resposta |
| `views.py` | Uma função por página. Recebe a `request` (string) e devolve a resposta (bytes) |
| `utils.py` | Funções auxiliares (`extract_route`, `read_file`, `load_template`, `extract_params`, `build_response`, ...) |
| `database.py` | Classe `Database` (SQLite) e dataclass `Note` |
| `templates/*.html` | HTML com "buracos" `{nome}` preenchidos com `.format()` |
| `getit.css`, `getit.js`, `img/` | Arquivos estáticos, servidos direto pelo `read_file` |

### 4.2 O caminho de uma requisição

```
Navegador ──"GET /edit/3 HTTP/1.1..."──▶ servidor.py
   1. route = extract_route(request)            → "edit/3"
   2. é um arquivo que existe? (getit.css, img/...) → devolve o arquivo
   3. senão, testa a rota em if/elif:
        ''            → index(request)
        'delete...'   → delete(request, id)
        'edit...'     → edit(request, id)
        'favorite...' → favorite(request, id)
        senão         → not_found()  (404)
   4. a view monta o HTML e chama build_response(...) → bytes
   5. client_connection.sendall(response)
```

### 4.3 Funções de `utils.py` (as que você mais vai usar)

```python
extract_route('GET /edit/3 HTTP/1.1 ...')   # → 'edit/3'  (sem a barra inicial)
load_template('index.html')                 # → string com o conteúdo de templates/index.html
extract_params(request)                     # → {'titulo': 'Oi', 'detalhes': 'Tudo bem'}  (corpo do POST)
build_response(body='<h1>oi</h1>')          # → b'HTTP/1.1 200 OK\n\n<h1>oi</h1>'
build_response(code=303, headers='Location: /')   # → redirect para "/"
build_response(body=..., code=404, reason='Not Found')
```

### 4.4 Templates com `.format()`

```html
<!-- templates/exemplo.html -->
<h1>{titulo}</h1>
```
```python
load_template('exemplo.html').format(titulo='Olá')   # → '<h1>Olá</h1>'
```

⚠️ **Pegadinha:** o `.format()` trata **toda** `{` e `}` como marcador. Se você colocar CSS ou JS **dentro** de um template que passa por `.format()`, precisa **duplicar** as chaves:

```html
<style>
  body {{ background-color: {cor}; }}   <!-- {{ e }} viram { e } ; {cor} é substituído -->
</style>
```

E **toda** chave `{algo}` que está no template precisa ser passada no `.format(...)`, senão dá `KeyError: 'algo'`.

### 4.5 Receita: adicionar uma rota nova no 1A

1. **Template**: crie `templates/nova.html` com `html`, `head` e `body`, e os marcadores `{...}` que precisar.
2. **View** em `views.py`:
   ```python
   def nova(request):
       body = load_template('nova.html').format(algo='valor')
       return build_response(body=body)
   ```
3. **Import** em `servidor.py`: `from views import index, ..., nova`
4. **Rota** em `servidor.py`, num `elif` **antes** do `else`:
   ```python
   elif route == 'minha/rota':
       response = nova(request)
   ```
5. **Reinicie** o servidor e teste em **aba anônima** (evita cache do navegador).

Por que `route == ...` e não `startswith`? Para rotas fixas o `==` é mais seguro. O `startswith` serve para rotas com id no final (`edit/3`, `delete/7`), onde o id é pego com `route.split('/')[-1]`.

### 4.6 Banco de dados no 1A (`database.py`)

```python
db = Database('notes')                  # abre/cria notes.db e a tabela note
db.add(Note(title='t', content='c'))    # INSERT
db.get_all()                            # SELECT → lista de Note
db.get_by_id(3)                         # SELECT ... WHERE id=? → Note ou None
db.update(nota)                         # UPDATE
db.delete(3)                            # DELETE
```

Use sempre `?` nos comandos SQL (`WHERE id = ?`, `(note_id,)`). Isso evita SQL injection.

---

## 5. Projeto 1B: Django

### 5.1 Estrutura

```
tecweb-2026-2-projeto1B/
├── manage.py                 ← "controle remoto" do Django (runserver, migrate...)
├── db.sqlite3                ← banco de dados
├── env/                      ← ambiente virtual (não vai pro git)
├── getit/                    ← PROJETO (configuração)
│   ├── settings.py           ← INSTALLED_APPS, DATABASES, DEBUG, ALLOWED_HOSTS
│   └── urls.py               ← rotas "raiz": admin/ e include('notes.urls')
└── notes/                    ← APP (a lógica)
    ├── models.py             ← tabelas do banco (classes)
    ├── views.py              ← funções que tratam cada página
    ├── urls.py               ← rotas do app → views
    ├── admin.py              ← registra models no /admin
    ├── migrations/           ← histórico de mudanças do banco (gerado automaticamente)
    ├── templates/notes/*.html
    └── static/notes/         ← css, js, img
```

### 5.2 O caminho de uma requisição

```
GET /tags/2/
  → getit/urls.py:  path('', include('notes.urls'))
  → notes/urls.py:  path('tags/<int:tag_id>/', views.tag_detail, name='tag_detail')
  → notes/views.py: tag_detail(request, tag_id=2)
        busca no banco com o ORM (Tag.objects.get(id=2))
        return render(request, 'notes/tag_detail.html', {'tag': tag, 'notes': notes})
  → template usa {{ tag.name }}, {% for note in notes %} ...
```

**Para toda página nova você mexe em 3 lugares: `urls.py` + `views.py` + template.** Se mexer no banco, também em `models.py` (+ migrations).

### 5.3 Models e migrations

```python
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):          # como o objeto aparece no admin/shell
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='notes')
```

- O Django cria o campo `id` sozinho.
- Por padrão todo campo é **obrigatório** (`null=False`). `null=True` deixa o **banco** aceitar vazio. `blank=True` deixa **formulários** aceitarem vazio.

| Campo | Uso |
|---|---|
| `CharField(max_length=200)` | Texto curto. No Django 6 com SQLite/PostgreSQL o `max_length` é opcional, mas use sempre (padrão dos handouts, funciona em qualquer versão) |
| `TextField()` | Texto sem limite |
| `BooleanField()` | Verdadeiro/Falso |
| `IntegerField()`, `FloatField()` | Números |
| `DateTimeField(auto_now_add=True)` | Data/hora |
| `ForeignKey(Outro, on_delete=models.CASCADE)` | Relação **um para muitos** |
| `ManyToManyField(Outro)` | Relação **muitos para muitos** |

**Relações:**

| | Um para muitos (`ForeignKey`) | Muitos para muitos (`ManyToManyField`) |
|---|---|---|
| Exemplo | Uma categoria tem **várias** perguntas; cada pergunta tem **uma** categoria | Uma nota tem várias tags; uma tag tem várias notas |
| Onde declarar | No lado "muitos" (em quem tem **uma** só) | Em qualquer um dos dois |
| Salvar | `Pergunta(..., categoria=cat)` ou `p.categoria = cat` | `note.save()` e **depois** `note.tags.set([...])` / `.add(tag)` |
| Acessar ida | `pergunta.categoria.nome` | `note.tags.all()` |
| Acessar volta | `categoria.perguntas.all()` (com `related_name='perguntas'`) | `tag.notes.all()` |

`on_delete=models.CASCADE`: se apagar a categoria, apaga as perguntas dela junto.

#### Passo a passo: um para muitos no código (exemplo Autor → Livro)

> Um **autor** tem **vários** livros; cada **livro** tem **um** autor.

**Regra de ouro:** a `ForeignKey` fica na classe do lado **"muitos"**. Pense assim: "cada livro tem UM autor", então o campo `autor` fica no `Livro`.

**1) `models.py`**

```python
class Autor(models.Model):                  # o lado "um" vem PRIMEIRO no arquivo
    nome = models.CharField(max_length=200)

class Livro(models.Model):                  # o lado "muitos"
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
```

- `Autor` precisa estar **acima** de `Livro`, senão dá `NameError: name 'Autor' is not defined`. Alternativa: escrever `'Autor'` entre aspas.
- No banco, o Django cria na tabela de livros uma coluna **`autor_id`** que guarda o **id** do autor.

**2) Terminal**: `makemigrations` e depois `migrate`. Se já existem livros salvos, ele pergunta o valor para as linhas antigas: escolha `1` e digite o **id de um autor que existe** (veja a seção de migrations logo abaixo).

**3) Template: o `<select>` manda o id**

```django
<select name="autor">
  {% for autor in autores %}
    <option value="{{ autor.id }}">{{ autor.nome }}</option>
  {% endfor %}
</select>
```

- O usuário **vê** o nome (`{{ autor.nome }}`), mas o navegador **envia** o `value`, que é o id: `autor=3`.
- Para o `for` funcionar, a view precisa mandar `autores` no contexto do `render` (senão o select fica vazio).

**4) View: transformar o id em objeto e salvar**

```python
from .models import Autor, Livro

def livros(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor_id = request.POST.get('autor')             # "3" (texto)
        autor = Autor.objects.get(id=autor_id)           # busca o OBJETO autor
        Livro.objects.create(titulo=titulo, autor=autor) # liga o livro ao autor
        return redirect('livros')
    else:
        return render(request, 'app/livros.html', {
            'livros': Livro.objects.all(),
            'autores': Autor.objects.all(),              # para montar o <select>
        })
```

(Atalho equivalente: `Livro.objects.create(titulo=titulo, autor_id=autor_id)`, passando direto o id.)

**5) Mostrar a relação no template**

```django
{% for livro in livros %}
  <li>{{ livro.titulo }} ({{ livro.autor.nome }})</li>    {# ida: livro → autor #}
{% endfor %}

{% for livro in autor.livros.all %} ... {% endfor %}       {# volta: autor → livros (related_name) #}
```

| Quero... | Código |
|---|---|
| O autor de um livro | `livro.autor` (é um objeto `Autor`) |
| O nome do autor de um livro | `livro.autor.nome` |
| Todos os livros de um autor | `autor.livros.all()` (graças ao `related_name='livros'`) |
| Livros de um autor pelo filtro | `Livro.objects.filter(autor=autor)` |

**Migrations:** o fluxo é `models.py` → `makemigrations` (gera `notes/migrations/000X_....py`) → `migrate` (altera o `db.sqlite3`).

Se você adiciona um campo **obrigatório** num model que **já tem linhas** no banco, o `makemigrations` pergunta qual valor colocar nas linhas antigas:

```
It is impossible to add a non-nullable field 'categoria' to pergunta without specifying a default...
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 1
>>> 1            ← valor padrão (para ForeignKey é o ID de um objeto que EXISTE)
```

### 5.4 ORM (consultas no banco sem SQL)

```python
Note.objects.all()                        # todos
Note.objects.get(id=3)                    # um só (erro se não existir)
Note.objects.filter(title='oi')           # vários que batem com o filtro
Tag.objects.order_by('name')              # ordenado
Note.objects.create(title='a', content='b')   # cria e já salva
n = Note(title='a'); n.save()             # cria em 2 passos
n.title = 'novo'; n.save()                # atualiza
n.delete()                                # apaga
tag, criada = Tag.objects.get_or_create(name='x')   # busca ou cria
```

Testar no shell: `python manage.py shell` → `from notes.models import *` → `Note.objects.all()`.

### 5.5 URLs

```python
# notes/urls.py
urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:note_id>/', views.update, name='update'),   # <int:...> vira parâmetro da view
]
```

- O `name=` permite usar `{% url 'index' %}` no template e `redirect('index')` na view.
- **Barra final importa:** `path('perguntas', ...)` responde em `/perguntas`, e `path('perguntas/', ...)` responde em `/perguntas/`. Use **exatamente** a URL que o enunciado mostra.

### 5.6 Views

```python
from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == 'POST':                    # formulário enviado
        title = request.POST.get('titulo')          # 'titulo' = name do input
        Note.objects.create(title=title)
        return redirect('index')                    # volta para a página (evita reenvio)
    else:                                           # GET: só mostrar
        return render(request, 'notes/index.html', {'notes': Note.objects.all()})
```

- `request.POST.get('x')` sempre devolve **string** (ou `None`). Converter é com você: `int(...)`, `== 'Verdadeiro'` etc.
- O 3º argumento do `render` (dicionário) é o **contexto**: as chaves viram variáveis no template.

#### `render` × `redirect`

| | `render` | `redirect` |
|---|---|---|
| Frase | "Toma aqui a página" | "Vai lá buscar em outro lugar" |
| O que devolve | HTML pronto (template + dados), status **200** | Só um status **302** com `Location: /rota` (sem HTML) |
| URL no navegador | Não muda | Muda para a nova rota |
| Quando usar | **Mostrar** uma página (GET) | **Depois de salvar/editar/apagar** (POST) |
| Precisa de template? | Sim | Não, só o nome da rota (`name=`) |

Fluxo de um formulário:

```
1. Usuário envia o form        → POST /perguntas
2. View salva e redireciona    ← 302, Location: /perguntas   (redirect)
3. Navegador faz sozinho       → GET /perguntas
4. View mostra a página        ← 200, HTML com a lista atualizada   (render)
```

- **Por que não dar `render` direto depois do POST?** Se a última requisição foi um POST, o F5 **reenvia o formulário** e o dado é salvo **duas vezes**. Com o `redirect`, a última requisição passa a ser um GET e o F5 só recarrega a página.
- **No Projeto 1A** a mesma ideia foi feita na mão: `build_response(code=303, headers='Location: /')` é um redirect.

### 5.7 Templates (linguagem de template do Django)

```django
{% extends "notes/base.html" %}      {# herda o esqueleto html/head/body #}
{% load static %}

{% block content %}
  <form method="post" action="{% url 'index' %}">
    {% csrf_token %}                 {# OBRIGATÓRIO em todo form POST #}
    <input type="text" name="titulo" />
    <input type="submit" />
  </form>

  <ul>
    {% for note in notes %}
      <li>{{ note.title }}</li>
    {% empty %}
      <li>Nenhuma nota</li>
    {% endfor %}
  </ul>

  {% if note.favorita %}★{% else %}☆{% endif %}
  <img src="{% static 'notes/img/logo-getit.png' %}">
  <a href="{% url 'update' note.id %}">Editar</a>
{% endblock %}
```

- `{{ variavel }}` **mostra** um valor. `{% tag %}` é **lógica** (for, if, url, csrf_token...).
- O `base.html` tem `{% block content %}{% endblock %}`, e os outros templates preenchem esse bloco.
- Templates ficam em `notes/templates/notes/` e são chamados como `'notes/arquivo.html'`.

**Select (dropdown):**

```django
<select name="categoria">
  {% for c in categorias %}
    <option value="{{ c.id }}">{{ c.nome }}</option>   {# value = o que é enviado; texto = o que aparece #}
  {% endfor %}
</select>
```

### 5.8 Admin

```python
# notes/admin.py
from .models import Note, Tag
admin.site.register(Note)
```

`python manage.py createsuperuser` e depois http://localhost:8000/admin. É ótimo para **conferir** se os dados foram salvos.

### 5.9 Receita: funcionalidade nova no Django (checklist)

1. `models.py`: criar/alterar a classe.
2. Terminal: `python manage.py makemigrations` e depois `python manage.py migrate`.
3. (Opcional) `admin.py`: `admin.site.register(NovoModel)`.
4. `views.py`: importar o model (`from .models import ..., NovoModel`) e criar a função com `if request.method == 'POST': ... redirect(...)` / `else: render(...)`.
5. `urls.py`: `path('rota', views.funcao, name='rota')`.
6. Template em `notes/templates/notes/arquivo.html`: form com `{% csrf_token %}`, inputs com `name` e lista com `{% for %}`.
7. Testar no navegador e no `/admin`.
8. `git add .` e `git commit -m "mensagem do enunciado"`.

---

## 6. Erros comuns e como resolver

| Erro | Causa provável | Solução |
|---|---|---|
| **1A:** `KeyError: 'cor'` | Template tem `{cor}` mas não foi passado no `.format()` | Passe `cor=...` no `.format` |
| **1A:** `KeyError` / `ValueError` com CSS | `{ }` do CSS dentro do template | Duplique: `{{` e `}}` |
| **1A:** mudança não aparece | Servidor não foi reiniciado / cache | Ctrl+C, `python servidor.py`, aba anônima |
| **1A:** `FileNotFoundError: templates/...` | Rodou de outra pasta | `cd` para a pasta do projeto |
| **1A:** `NameError`/`ImportError` | View não importada no `servidor.py` | Adicione no `from views import ...` |
| **1A:** acentos da data errados (`sÃ¡bado`) | Bug do Python no **Windows** com `'pt_BR.UTF-8'` | Use `locale.setlocale(locale.LC_TIME, 'pt_BR')` |
| **1A:** `locale.Error: unsupported locale setting` | Locale não existe no sistema | Tente `'pt_BR'`, `'pt_BR.UTF-8'` ou `'Portuguese_Brazil.1252'` |
| **Django:** `no such table: notes_pergunta` | Esqueceu de migrar | `makemigrations` + `migrate` |
| **Django:** `No changes detected` | Model não salvo / app não está em `INSTALLED_APPS` | Salve o arquivo (Ctrl+S) |
| **Django:** `CSRF verification failed` (403) | Faltou `{% csrf_token %}` no form | Adicione dentro do `<form>` |
| **Django:** `TemplateDoesNotExist` | Caminho errado | O arquivo deve ficar em `notes/templates/notes/x.html` e ser chamado como `'notes/x.html'` |
| **Django:** `NoReverseMatch` | `{% url 'nome' %}` / `redirect('nome')` com nome inexistente | Confira o `name=` no `urls.py` |
| **Django:** `NameError: Pergunta` | Não importou o model na view | `from .models import ..., Pergunta` |
| **Django:** `NameError: Categoria` em `models.py` | `ForeignKey(Categoria)` antes de `Categoria` existir | Declare `Categoria` **acima**, ou use `'Categoria'` entre aspas |
| **Django:** `RuntimeError ... APPEND_SLASH` | POST para `/rota` mas a rota é `rota/` | Deixe a URL do `path` igual à do `action` |
| **Django:** tirei a barra do `path` (`'rota/'` → `'rota'`) e deu 404 em `/rota/` | Antes, `/rota` respondia **301** para `/rota/`, e o navegador **guarda o 301 no cache** e continua redirecionando | Teste numa **aba anônima nova** (ou limpe o cache) |
| **Django:** `Reverse for 'x' with arguments '('',)' not found` | `{% url 'x' objeto.id %}` com um objeto que não existe no contexto (ou rota errada) | Confira o nome da rota e se a variável foi passada no `render` |
| **Django:** `IntegrityError NOT NULL` | Campo obrigatório vazio | Envie o valor ou ajuste o model |
| **Django:** `ModuleNotFoundError: django` | `env` não ativado | `.\env\Scripts\Activate.ps1` |
| **Django:** `ModuleNotFoundError: dj_database_url` (em qualquer comando do `manage.py`) | Pacote do deploy não instalado no `env` (o `settings.py` importa ele) | `pip install -r requirements.txt` (ou `pip install dj-database-url`) e confira com `pip list` |
| **Django:** `That port is already in use` | Outro runserver aberto | Feche o outro terminal ou use `runserver 8001` |

---

## 7. Simulado: enunciado resumido

PDF: https://barbaratieko.github.io/tecweb/simulado/251_tecweb_ai_disponibilizar.pdf

### Questão 1: Projeto 1A (3,5 pts)
- **1.1 Página nova (1,5):** rota `http://localhost:8080/hoje/agora`, com um **arquivo HTML novo** (válido: `html`, `head`, `body`), `h1` "Avaliação Intermediária" e `h2` com **data e hora atual** (`datetime.datetime.now()`, data por extenso em português com `locale`). Precisa de uma **função nova em `views.py`**. Commit: **"Adicionando data de hoje"**.
- **1.2 Cor de fundo (2):** o fundo da página muda de cor **a cada carregamento**, **sem JavaScript**. Alterações esperadas em `index.html` e `views.py`. Mínimo de **6 cores**: `#DAF7A6 #FFC300 #FF5733 #C70039 #900C3F #581845`. Commit: **"Adicionando cor ao fundo da página"**.

### Questão 2: Projeto 1B (6 pts), perguntas de verdadeiro ou falso
- **3.1 Model `Pergunta` (0,5):** `enunciado` (`TextField`, sem limite, não nulo) e `resposta_correta` (`BooleanField`, não nulo). **Nenhum campo a mais.** Fazer as migrações. Commit: **"Criando modelo Pergunta"**.
- **3.2 Formulário (1,5):** rota `http://localhost:8000/perguntas` com form (enunciado + resposta). O usuário digita "Verdadeiro" ou "Falso". Salva no banco e **redireciona** para `/perguntas`. Commit: **"Formulário criado"**.
- **3.3 Listagem (1):** abaixo do form, uma `<ul>` com o enunciado e a resposta correta de todas as perguntas. Commit: **"Listagem implementada"**.
- **3.4 Categoria (1):** model `Categoria` com só `nome` (`CharField`, obrigatório). Rota `categorias` com form de cadastro e lista abaixo. Commit: **"Cadastro de categorias"**.
- **3.5 Relação (2):** **um para muitos** (uma categoria tem várias perguntas, cada pergunta tem uma categoria). No form de perguntas, um `<select name="categoria">` com todas as categorias. Salvar o vínculo. Commit: **"Categoria Finalizada"**.

---

## 8. Resolução do simulado (spoiler)

> ⚠️ **SPOILER.** Tudo abaixo está recolhido. Tente sozinha primeiro, e abra só a parte em que travar.
>
> Esta resolução foi **testada** numa cópia dos seus projetos (o seu código **não** foi alterado).

<details>
<summary><b>▶ Q1.1: página /hoje/agora</b></summary>

**Ideia:** template novo + view nova + `elif` novo no `servidor.py`.

**`templates/hoje.html`** (HTML válido, com `html`/`head`/`body`):

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Hoje</title>
    </head>
    <body>
        <h1>Avaliação Intermediária</h1>
        <h2>{data}</h2>
    </body>
</html>
```

(Pode manter os `<link>` de CSS se quiser. Eles não usam `{ }`, então não atrapalham o `.format`.)

**`views.py`**: no topo `import locale` e `import datetime`, e a função:

```python
def hoje_agora(request):
    locale.setlocale(locale.LC_TIME, 'pt_BR')   # no Mac/Linux: 'pt_BR.UTF-8'
    hoje = datetime.datetime.now()
    data_em_extenso = hoje.strftime('%A, %d de %B de %Y - %H:%M:%S')
    body = load_template('hoje.html').format(data=data_em_extenso)
    return build_response(body=body)
```

- O enunciado pede **data e hora**, por isso o `%H:%M:%S` no final.
- **Windows:** o enunciado usa `'pt_BR.UTF-8'`, mas no Windows isso gera acentos quebrados (`sÃ¡bado`, `marÃ§o`). Testei no seu computador: com `'pt_BR'` sai `sábado` certinho.
- Códigos do `strftime`: `%A` dia da semana, `%d` dia, `%B` mês por extenso, `%Y` ano, `%H:%M:%S` hora.

**`servidor.py`**: importar e rotear:

```python
from views import index, edit, delete, favorite, not_found, hoje_agora
...
    elif route.startswith('favorite'):
        response = favorite(request, route.split('/')[-1])
    elif route == 'hoje/agora':
        response = hoje_agora(request)
    else:
        response = not_found()
```

Reinicie o servidor, abra http://localhost:8080/hoje/agora em aba anônima e faça o commit:

```powershell
git add .
git commit -m "Adicionando data de hoje"
```
</details>

<details>
<summary><b>▶ Q1.2: cor de fundo aleatória (sem JS)</b></summary>

**Ideia:** o **Python** sorteia a cor a cada request e injeta no HTML pelo `.format()`. Como a view `index` roda a cada carregamento, a cor muda sempre.

**`views.py`**:

```python
import random

CORES = ['#DAF7A6', '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845']

def index(request):
    ...   # (tudo igual ao que já existe)
    notes = '\n'.join(notes_li)
    cor = random.choice(CORES)
    body = load_template('index.html').format(notes=notes, erro=erro, cor=cor)
    return build_response(body=body)
```

**`templates/index.html`**: trocar só a tag `<body>`:

```html
<body style="background-color: {cor};">
```

Alternativa com CSS (se quiser mexer no `getit.css`): crie classes `.fundo-1 { background-color: #DAF7A6; }` ... `.fundo-6 {...}` no `getit.css`, use `<body class="fundo-{numero}">` e na view `numero = random.randint(1, 6)`.

⚠️ **Não** coloque um bloco `<style> body { ... } </style>` dentro do `index.html` sem duplicar as chaves (`{{ }}`), senão o `.format()` quebra.

Teste recarregando http://localhost:8080 várias vezes (F5). Depois:

```powershell
git add .
git commit -m "Adicionando cor ao fundo da página"
```
</details>

<details>
<summary><b>▶ Q2 3.1: model Pergunta</b></summary>

**`notes/models.py`** (embaixo dos outros models):

```python
class Pergunta(models.Model):
    enunciado = models.TextField()
    resposta_correta = models.BooleanField()

    def __str__(self):
        return self.enunciado
```

- `TextField()` não tem limite de caracteres.
- Sem `null=True`, o campo **não pode ser nulo** (o padrão do Django já é `null=False`). Não precisa escrever nada a mais.
- **Não adicione outros campos** (o `id` é automático e não conta).

**Terminal** (com o `env` ativado, na pasta do `manage.py`):

```powershell
python manage.py makemigrations    # → notes\migrations\0007_pergunta.py  + Create model Pergunta
python manage.py migrate           # → Applying notes.0007_pergunta... OK
git add .
git commit -m "Criando modelo Pergunta"
```

(Opcional, para conferir no admin: `admin.site.register(Pergunta)` no `admin.py`.)
</details>

<details>
<summary><b>▶ Q2 3.2 + 3.3: formulário e listagem de perguntas</b></summary>

**`notes/views.py`**: atualizar o import e criar a view:

```python
from .models import Note, Tag, Pergunta

def perguntas(request):
    if request.method == 'POST':
        enunciado = request.POST.get('enunciado')
        resposta = request.POST.get('resposta')
        resposta_correta = resposta.strip().lower() == 'verdadeiro'   # "Verdadeiro" → True ; "Falso" → False
        Pergunta.objects.create(enunciado=enunciado, resposta_correta=resposta_correta)
        return redirect('perguntas')
    else:
        todas_perguntas = Pergunta.objects.all()
        return render(request, 'notes/perguntas.html', {'perguntas': todas_perguntas})
```

Por que converter? O form envia **texto** ("Verdadeiro"), mas o campo é **booleano**. A comparação `== 'verdadeiro'` já devolve `True`/`False`. O `.strip().lower()` aceita também "verdadeiro " ou "VERDADEIRO".

**`notes/urls.py`**:

```python
path('perguntas', views.perguntas, name='perguntas'),
```

(Sem barra no final, porque o enunciado usa `http://localhost:8000/perguntas`.)

**`notes/templates/notes/perguntas.html`** (novo):

```django
{% extends "notes/base.html" %}

{% block content %}
<h1>Cadastro de Perguntas</h1>

<form method="post" action="{% url 'perguntas' %}">
  {% csrf_token %}
  <label for="enunciado">Enunciado</label>
  <input id="enunciado" type="text" name="enunciado" />
  <label for="resposta">Resposta (Verdadeiro ou Falso)</label>
  <input id="resposta" type="text" name="resposta" />
  <input type="submit" value="Cadastrar" />
</form>

<ul>
  {% for pergunta in perguntas %}
    <li>
      {{ pergunta.enunciado }} -
      {% if pergunta.resposta_correta %}Verdadeiro{% else %}Falso{% endif %}
    </li>
  {% endfor %}
</ul>
{% endblock %}
```

Commits em **dois momentos**: primeiro só com o form (sem a `<ul>`) → `git commit -m "Formulário criado"`; depois adicione a `<ul>` e passe `perguntas` no `render` → `git commit -m "Listagem implementada"`.

(Se o enunciado mostrar `True`/`False` na lista, basta usar `{{ pergunta.resposta_correta }}`. Existe também o filtro `{{ pergunta.resposta_correta|yesno:"Verdadeiro,Falso" }}`.)
</details>

<details>
<summary><b>▶ Q2 3.4: model e página de Categoria</b></summary>

**`notes/models.py`**: declare **acima** de `Pergunta` (vai ser usada na ForeignKey do 3.5):

```python
class Categoria(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
```

`CharField` sem `null`/`blank` já é **obrigatório**. O `max_length` é opcional no Django 6 (SQLite/PostgreSQL), mas é boa prática colocar.

```powershell
python manage.py makemigrations    # + Create model Categoria
python manage.py migrate
```

**`notes/views.py`**:

```python
from .models import Note, Tag, Pergunta, Categoria

def categorias(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        Categoria.objects.create(nome=nome)
        return redirect('categorias')
    else:
        todas_categorias = Categoria.objects.all()
        return render(request, 'notes/categorias.html', {'categorias': todas_categorias})
```

**`notes/urls.py`**:

```python
path('categorias', views.categorias, name='categorias'),
```

**`notes/templates/notes/categorias.html`**:

```django
{% extends "notes/base.html" %}

{% block content %}
<h1>Cadastro de Categorias</h1>

<form method="post" action="{% url 'categorias' %}">
  {% csrf_token %}
  <label for="nome">Nome</label>
  <input id="nome" type="text" name="nome" required />
  <input type="submit" value="Cadastrar" />
</form>

<ul>
  {% for categoria in categorias %}
    <li>{{ categoria.nome }}</li>
  {% endfor %}
</ul>
{% endblock %}
```

Cadastre **pelo menos uma categoria** em http://localhost:8000/categorias antes do 3.5 (vai precisar do id dela na migração).

```powershell
git add .
git commit -m "Cadastro de categorias"
```
</details>

<details>
<summary><b>▶ Q2 3.5: relação um para muitos + select</b></summary>

**`notes/models.py`**: a `ForeignKey` fica no lado "muitos", ou seja, na **Pergunta**:

```python
class Pergunta(models.Model):
    enunciado = models.TextField()
    resposta_correta = models.BooleanField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='perguntas')
```

- Com `related_name='perguntas'` dá para fazer `categoria.perguntas.all()` (acesso reverso).
- `Categoria` precisa estar declarada **acima** de `Pergunta`.

**Migração:** como já existem perguntas salvas sem categoria, o Django pergunta:

```
 1) Provide a one-off default now ...
 2) Quit and manually define a default value in models.py.
Select an option: 1
>>> 1
```

Digite `1` (opção) e depois o **id de uma categoria que existe** (a primeira categoria criada tem id `1`; confira no `/admin` ou no shell). Assim as perguntas antigas ficam ligadas a essa categoria.

```powershell
python manage.py makemigrations    # + Add field categoria to pergunta
python manage.py migrate
```

(Outra saída, se não existir nenhuma categoria: apagar as perguntas antigas antes, ou usar `null=True` na ForeignKey.)

**`notes/views.py`**: na view `perguntas`, buscar a categoria escolhida e mandar as categorias para o template:

```python
def perguntas(request):
    if request.method == 'POST':
        enunciado = request.POST.get('enunciado')
        resposta = request.POST.get('resposta')
        resposta_correta = resposta.strip().lower() == 'verdadeiro'
        categoria = Categoria.objects.get(id=request.POST.get('categoria'))
        Pergunta.objects.create(enunciado=enunciado, resposta_correta=resposta_correta, categoria=categoria)
        return redirect('perguntas')
    else:
        todas_perguntas = Pergunta.objects.all()
        todas_categorias = Categoria.objects.all()
        return render(request, 'notes/perguntas.html', {'perguntas': todas_perguntas, 'categorias': todas_categorias})
```

**`perguntas.html`**: adicionar o `select` dentro do form (antes do botão) e, se quiser, mostrar a categoria na lista:

```django
  <label for="categoria">Categoria</label>
  <select id="categoria" name="categoria">
    {% for categoria in categorias %}
      <option value="{{ categoria.id }}">{{ categoria.nome }}</option>
    {% endfor %}
  </select>
```

```django
    <li>
      {{ pergunta.enunciado }} -
      {% if pergunta.resposta_correta %}Verdadeiro{% else %}Falso{% endif %}
      ({{ pergunta.categoria.nome }})
    </li>
```

Como funciona: o `<option value="{{ categoria.id }}">` faz o navegador enviar o **id** da categoria escolhida (`categoria=2`). A view busca esse objeto com `Categoria.objects.get(id=...)` e passa para o `create`. Isso é o vínculo um para muitos.

```powershell
git add .
git commit -m "Categoria Finalizada"
```
</details>

---

## 9. Checklist para o dia da prova

- [ ] Abrir o VS Code na pasta da prova e conferir `git status`.
- [ ] **1A:** `cd` na pasta do projeto, `python servidor.py`, testar em **aba anônima**, reiniciar a cada mudança em `.py`.
- [ ] **1B:** ativar `env`, `python manage.py runserver`, abrir http://localhost:8000.
- [ ] Mudou model? Então `makemigrations` + `migrate`.
- [ ] Todo `<form method="post">` do Django tem `{% csrf_token %}`.
- [ ] Nomes de **model, campos e rotas exatamente** como no enunciado.
- [ ] Commit com a **mensagem exata** depois de **cada** etapa.
- [ ] Não apagar nem quebrar funcionalidades antigas (testar a página inicial no fim).
- [ ] Smowl ligado do começo ao fim.

---
---

# Instruções originais da preparação e regras da avaliação

> [PREPARAÇÃO PARA AVALIAÇÃO]

- Crie uma pasta chamada `Projeto1A` e dentro desta pasta adicione o código entregue no Projeto 1A.
  - IMPORTANTE: Tome cuidado para não copiar o arquivo .git que existe dentro da pasta do repositório.

- Crie uma pasta chamada `Projeto1B` e dentro desta pasta adicione o código entregue no Projeto 1B.
  - Caso tenha realizado a tarefa do deploy, altere as configurações do projeto para utilizar o banco de dados SQLite e altere a variável DEBUG para True.
  - Crie o ambiente virtual dentro da pasta `Projeto1B` e instale as dependências do projeto.
  - IMPORTANTE: Tome cuidado para não copiar o arquivo .git que existe dentro da pasta do repositório.

- Faça o teste do Smowl. Após realizar os itens acima, valide com os professores ou ninja para receber o 0.5 pontos da prova.

- Esta tarefa deve ser validada até o dia 22/09, durante o horário de aula ou atendimento.

___

> [Regras para avaliação]

NÃO é permitido (será considerada infração do código de ética da instituição):

- usar smartphone ou tablet
- consultar google drive, one drive, dropbox ou qualquer ferramenta de compartilhamento de arquivos.
- consultar repositórios nos sites github, gitlab, bitbucket ou similares.
- consultar email, whatsapp, discord ou qualquer outra forma de comunicação direta com outras pessoas
- criar perguntas em forums na hora da aula
- utilizar outras pessoas para resolver a prova por você
- utilizar ferramentas como Chat-GPT, Claude e afins (ferramentas que utilizem inteligência artificial)
- utilizar ferramentas de auto-geração de código (exemplo: copilot)
- acessar a avaliação enquanto estiver fora da sala ou já tiver informado a entrega ao professor

O desrespeito a estas regras constituirá violação ao Código de Ética e de Conduta e acarretará sanções nele previstas. Faça o seu trabalho de maneira ética!

É permitido:

- Consultas no google para consultar a documentação de bibliotecas, stackoverflow e afins. 
    - Ou seja, ignore a resposta gerada por IA.
- Consultas aos códigos desenvolvidos em aula, handout, projetos e simulado.
    - O código deve estar no seu computador.

___

> [Ferramentas Smowl]

A ferramenta Smowl deverá ser utilizada para monitoramento da prova e deverá registrar toda a implemetação da solução da prova. Caso o Smowl não registre a implementação integral da solução, a questão será desconsiderada.

___

> [ARGUIÇÃO ORAL]

A avaliação poderá ser objeto de arguição oral sobre seu conteúdo, seus procedimentos de elaboração, funcionamento e as decisões adotadas pelo estudante. 
A realização da arguição poderá ser exigida como condição para a validação da nota atribuída a prova.

