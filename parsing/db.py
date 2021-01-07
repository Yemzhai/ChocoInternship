import psycopg2
con = psycopg2.connect(
    host = 'localhost',
    database='sulpak',
    user='postgres',
    password='123456789i',
    port='5432',
)
cursor = con.cursor()
# sql = 'CREATE TABLE items (name VARCHAR, price VARCHAR, availability VARCHAR, link TEXT)'
# cursor.execute('CREATE TABLE items (id SERIAL PRIMARY KEY, name VARCHAR);')
# cursor.execute("INSERT INTO items (name) VALUES('Islam')")
cursor.execute("SELECT * from items")
print(cursor.fetchall())
con.commit()
cursor.close()
con.close() 