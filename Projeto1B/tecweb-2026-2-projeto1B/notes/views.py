from django.shortcuts import render, redirect
from .models import Note, Tag

def parse_tags(texto):
    tags = []
    for nome in texto.split(','):
        nome = nome.strip()
        if nome:
            tag, created = Tag.objects.get_or_create(name=nome)
            tags.append(tag)
    return tags

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note = Note(title=title, content=content)
        note.save()
        note.tags.set(parse_tags(request.POST.get('tag', '')))
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request, note_id):
    note = Note.objects.get(id=note_id) #busca a nota pelo id
    note.delete() #apaga a note
    return redirect('index') #volta pra pg inicial

def update(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        note.title = request.POST.get('titulo')
        note.content = request.POST.get('detalhes')
        note.save()
        note.tags.set(parse_tags(request.POST.get('tag', '')))
        return redirect('index')
    else:
        tags_texto = ', '.join(tag.name for tag in note.tags.all())
        return render(request, 'notes/edit.html', {'note': note, 'tags_texto': tags_texto})

def tag_list(request):
    all_tags = Tag.objects.order_by('name')
    return render(request, 'notes/tags.html', {'tags': all_tags})

def tag_detail(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    notes = tag.notes.all()
    return render(request, 'notes/tag_detail.html', {'tag': tag, 'notes': notes})






