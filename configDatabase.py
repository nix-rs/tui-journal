def db(conn):
    sql = """CREATE TABLE IF NOT EXISTS Journal (
            id INTEGER PRIMARY KEY,
            tag text NOT NULL,
            create_date DATE NOT NULL,
            update_date DATE NOT NULL,
            content text NOT NULL
    );"""

    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


def add_entry(conn, data):
    sql = ''' INSERT INTO Journal(tag,create_date,update_date,content)
              VALUES(?,?,?,?) '''

    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()
    #return cursor.lastrowid

# FIX: - split this funtion into update individula items
# This function will update full content i.e., date, content tags
def update_entry(conn, data):
    sql = '''UPDATE Journal SET
                tag=?,
                update_date=?,
                content=?
                WHERE id=?
    '''

    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()


def read_entry(conn):

    sql = 'SELECT * from Journal'

    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def delete_entry(conn, id):
    sql = "DELETE FROM Journal WHERE id = ?"

    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()
