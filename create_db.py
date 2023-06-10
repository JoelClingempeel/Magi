import sqlite3

conn = sqlite3.connect('data.db')

query = """
create table foo
(id int primary key not null,
spell int not null);
"""
conn.execute(query);

query = "insert into foo (id, spell) values (1, 0);"
conn.execute(query)

conn.commit()
