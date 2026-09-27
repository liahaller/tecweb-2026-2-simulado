import sqlite3
from dataclasses import dataclass

class Database():
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo + '.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL, favorite INTEGER NOT NULL DEFAULT 0);')

    def add(self, note):
        self.conn.execute('INSERT INTO note (title, content) VALUES (?, ?)', (note.title, note.content))
        self.conn.commit()

    def get_all(self):
        lista = []
        cursor = self.conn.execute("SELECT id, title, content, favorite FROM note ORDER BY favorite DESC, id")
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            favorite = linha[3]
            lista.append(Note(id, title, content, favorite))
        return lista

    def get_by_id(self, note_id):
        cursor = self.conn.execute("SELECT id, title, content, favorite FROM note WHERE id = ?", (note_id,))
        linha = cursor.fetchone()
        if linha is None:
            return None
        return Note(linha[0], linha[1], linha[2], linha[3])

    def update(self,entry):
        self.conn.execute('UPDATE note SET title=?, content=?, favorite=? WHERE id=?', (entry.title, entry.content, entry.favorite, entry.id))
        self.conn.commit()

    def delete(self, note_id):
        self.conn.execute('DELETE FROM note WHERE id= ?', (note_id,))
        self.conn.commit()

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''
    favorite: int = 0