import sqlite3
import csv

with open('queries/get_products_for_csv.sql', 'r') as sql_file:
    get_products = sql_file.read()

output_csv_file = 'report.csv'


# Connect to the db
conn = sqlite3.connect('../data.db')
cur = conn.cursor()

cur.execute(get_products)

rows = cur.fetchall()


# Write to the CSV output
with open(output_csv_file, 'w', newline='') as csvFile:
    column_names = ['id', 'title', 'price', 'image_count']
    writer = csv.DictWriter(csvFile, fieldnames=column_names)

    # built in function takes care of header
    writer.writeheader()

    # loop for the body rows
    for row in rows:
        writer.writerow({'id': row[0], 'title': row[1], 'price': row[2], 'image_count': row[3]})

conn.close()

print("report generated")