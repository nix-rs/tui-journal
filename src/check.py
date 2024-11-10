import sqlite3

DB = "ck.db"

sql = """
CREATE TABLE IF NOT EXISTS Journal (
id INTEGER PRIMARY KEY,
tag text NOT NULL,
create_date DATE NOT NULL,
update_date DATE NOT NULL,
content text NOT NULL
);
"""


