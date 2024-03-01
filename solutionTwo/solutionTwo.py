import sqlite3
from helper_functions.create_cities_table import create_table
from helper_functions.populate_cities_table import populate_cities_table

# Create a new table within the SQLite database.
create_table()
# Import data from cities.csv into the newly created table.
populate_cities_table('cities.csv')

print("Cities successfully created and populated")