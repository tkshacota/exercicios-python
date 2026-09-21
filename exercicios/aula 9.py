import sqlite3

conn = sqlite3.connect("contatos.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS contatos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT)")
dados_exemplo = [
('João', 'joao@email.com', '123-456-7890'),
('Maria', 'maria@email.com', '987-654-3210'),
('Carlos', 'carlos@email.com', '555-555-5555')
]
cursor.executemany("INSERT INTO contatos (nome, email, telefone) VALUES (?, ?, ?)", dados_exemplo)
conn.commit()
cursor.execute("SELECT * FROM contatos")
contatos = cursor.fetchall()
print(contatos)
for contato in contatos:
    print(contato)
novo_telefone = '999-999-9999'
contato_id = 2
cursor.execute('UPDATE contatos SET telefone = ? WHERE id = ?', (novo_telefone, contato_id))
conn.commit()
contato_id_para_excluir = 1
cursor.execute('DELETE FROM contatos WHERE id = ?', (contato_id_para_excluir,))
conn.commit()
conn.close()
