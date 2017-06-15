import sqlite3

def create_table():
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT,quantity INTEGER, price REAL)")
	conn.commit()
	conn.close()

def insert(item,quantity,price):
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
	conn.commit()
	conn.close()

def show():
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM store")
	rows = cur.fetchall()
	conn.close()
	return rows

def main():
	create_table()
	# insert('Hello',4,20.4)
	rows= show()
	for i in rows:
		i.encode("ascii")
	print rows


if __name__ == "__main__":
	main()