import sqlite3

def connect():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS book (Id INTEGER PRIMARY KEY,Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
	conn.commit()
	conn.close()

def view():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM book")
	rows=cur.fetchall()
	conn.close()
	return rows

def insert(title,author,year,isbn):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title, author, year, isbn))
	conn.commit()
	conn.close()

def search(title="",author="",year="",isbn=""):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title, author, year, isbn))
	rows=cur.fetchall()
	conn.close()
	return rows

def delete(id):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM book WHERE id=?",(id,))
	conn.commit()
	conn.close()
	
def update(id,title,author,year,isbn):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn,id))
	conn.commit()
	conn.close()


connect()
"""
insert("Voldemort","JK Rowling",1992,9197818)
r= view()
for i in r:
	print i
print search(year=1992)
delete(3)
r= view()
for i in r:
	print i
update(4,"Moon","JK Rowling",1992,9197818)
"""
# print view()
search(author=u"JK Rowling")
