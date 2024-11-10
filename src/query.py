# SQLITE queries

read = "SELECT * from Journal;"

delete = "DELETE FROM Journal WHERE id = ?;"

sql = """
CREATE TABLE IF NOT EXISTS Journal (
id INTEGER PRIMARY KEY,
tag text NOT NULL,
create_date DATE NOT NULL,
update_date DATE NOT NULL,
content text NOT NULL
);
"""

add = """
INSERT INTO Journal(tag,create_date,update_date,content)
VALUES(?,?,?,?);
"""

u_tag = """
UPDATE Journal SET
tag=?,
update_date=?
WHERE id=?;
"""

u_content = """
UPDATE Journal SET
update_date=?,
content=?
WHERE id=?;
"""

u_all = """
UPDATE Journal SET
tag=?,
update_date=?,
content=?
WHERE id=?;
"""
