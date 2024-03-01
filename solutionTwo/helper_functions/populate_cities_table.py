import sqlite3

with open('queries/populate_cities.sql', 'r') as sql_file:
    populate_cities = sql_file.read()

#populate the cities table
def populate_cities_table(input):
    conn = sqlite3.connect('../data.db')
    cur = conn.cursor()
    with open(input, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
        print(lines)
        #go through each line starting with line after the header
        for line in lines[1:]:
            data = [item.strip() for item in line.strip().split(',')]

            #In order to prevent duplicate submissions for cities the SQL query expects the entire row twice
            dataWithValidationSet = data + data
            cur.execute(populate_cities, dataWithValidationSet)
        conn.commit()
        conn.close()
