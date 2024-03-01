import sqlite3


with open('queries/create_cities.sql', 'r') as sql_file:
    create_cities = sql_file.read()


#create the table in data.db
def create_table():
    conn = sqlite3.connect('../data.db')
    cur = conn.cursor()
    cur.execute(create_cities)
    conn.commit()
    conn.close()

create_table()

print("Cities successfully created")