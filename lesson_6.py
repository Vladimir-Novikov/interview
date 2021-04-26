import sqlite3
import os

db_path = os.getcwd()
print(db_path)

conn = sqlite3.connect(f"{db_path}/test.db")
cur = conn.cursor()


# cur.execute(
#     """
#     DROP TABLE IF EXISTS categories;
#     """
# )

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS categories(
     category_name TEXT NOT NULL PRIMARY KEY,
     category_description TEXT NOT NULL);
 """
)

cur.execute(
    """CREATE TABLE IF NOT EXISTS units(
     unit TEXT NOT NULL PRIMARY KEY);
 """
)

cur.execute(
    """CREATE TABLE IF NOT EXISTS positions(
     position TEXT NOT NULL PRIMARY KEY);
 """
)

# cur.execute(
#     """
#     DROP TABLE IF EXISTS goods;
#     """
# )

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS goods(
    good_id INTEGER PRIMARY KEY AUTOINCREMENT,
    good_name TEXT NOT NULL,
    good_unit TEXT NOT NULL,
    good_cat TEXT NOT NULL,
    FOREIGN KEY (good_unit) REFERENCES units(unit),
    FOREIGN KEY (good_cat) REFERENCES categories(category_name));
    """
)

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS employees(
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_fio TEXT NOT NULL,
    employee_position TEXT NOT NULL,
    FOREIGN KEY (employee_position) REFERENCES positions(position));
    """
)

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS vendors(
    vendor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vendor_name TEXT NOT NULL,
    vendor_ownerchipform TEXT NOT NULL,
    vendor_address TEXT NOT NULL,
    vendor_phone TEXT NOT NULL,
    vendor_email TEXT NOT NULL);
"""
)

conn.commit()


categories = [("Процессоры", "Для настольных ПК"), ("Блок питания", "Выносные")]
cur.executemany("INSERT INTO categories VALUES(?, ?);", categories)

conn.commit()


cur.execute("insert into goods (good_name, good_unit, good_cat) values ('Процессор AMD-1', 'шт', 'процессоры');")
cur.execute("insert into goods (good_name, good_unit, good_cat) values ('Процессор AMD-2', 'шт', 'процессоры');")


conn.commit()

cur.execute("SELECT * FROM goods;")
results = cur.fetchall()
print(results)


cur.execute("SELECT * FROM categories;")
results = cur.fetchall()
print(results)

conn.close()
