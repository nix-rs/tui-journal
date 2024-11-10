from query import *
import sqlite3
from constants import DB
from datetime import date


#tg = """
#CREATE TABLE IF NOT EXISTS Tags (
#id INTEGER PRIMARY KEY,
#tag text NOT NULL
#);
#"""

#tg_add = """
#INSERT INTO Tags(tag)
#VALUES(?);
#"""

def db():
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
 #       cursor.execute(tg)
        conn.commit()

# To check if a query is present in the table
#def query_tag(tag):
#    with sqlite3.connect("check.db") as conn:
#        cursor = conn.cursor()
#        cursor.execute("SELECT id FROM Tags WHERE tag=?", (tag,))
#        data = cursor.fetchone()
#        if data != None:
#            print(data)
#            return data[0]
#        else:
#            return False


def add_entry(conn, data):
    cursor = conn.cursor()
    cursor.execute(add, data)
    conn.commit()

def update_tag(conn, data):
    cursor = conn.cursor()
    cursor.execute(u_tag, data)
    conn.commit()

def update_content(conn, data):
    cursor = conn.cursor()
    cursor.execute(u_content, data)
    conn.commit()

def update_all(conn, data):
    cursor = conn.cursor()
    cursor.execute(u_all, data)
    conn.commit()

def read_entry(conn):
    cursor = conn.cursor()
    cursor.execute(read)
    rows = cursor.fetchall()
    return rows

def delete_entry(conn, id):
    cursor = conn.cursor()
    cursor.execute(delete, (id,))
    conn.commit()
