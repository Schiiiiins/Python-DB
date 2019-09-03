import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='db1' user='postgres' password='yse4.rfv' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert_data(item, quantity, price):
    conn = psycopg2.connect("dbname='db1' user='postgres' password='yse4.rfv' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='db1' user='postgres' password='yse4.rfv' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_data(item):
    conn = psycopg2.connect("dbname='db1' user='postgres' password='yse4.rfv' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update_data(quantity, price, item):
    conn = psycopg2.connect("dbname='db1' user='postgres' password='yse4.rfv' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


# insert_data("Orange", 2, 5)
print(view())
