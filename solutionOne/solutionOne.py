import sqlite3
import requests

# Retrieve data from the API endpoint
url = "https://dummyjson.com/products"
response = requests.get(url)

# Read SQL queries from the files
with open('queries/populate_product.sql', 'r') as sql_file:
    populate_product = sql_file.read()

with open('queries/populate_images.sql', 'r') as sql_file:
    populate_images = sql_file.read()


# if the API call was successful the code block below executes
if response.status_code == 200:
    data = response.json()
    
    # The API returns a nested dictionary called products
    products = data.get("products", [])
    
    # Establish a connection to the SQLite database and create the cursor for executing SQL commands
    conn = sqlite3.connect('../data.db')
    cur = conn.cursor()
    
    # This code block executes for each product in the products dictionary
    for product_data in products:

        # Assign each column to a variable
        product_id = product_data['id']
        title = product_data['title']
        description = product_data['description']
        price = product_data['price']
        discount_percentage = product_data['discountPercentage']
        rating = product_data['rating']
        stock = product_data['stock']
        brand = product_data['brand']
        category = product_data['category']
        thumbnail = product_data['thumbnail']
        
        # Populates product table using INSERT or REPLACE to ensure no duplicates
        cur.execute(populate_product, (product_id, title, description, price, discount_percentage, rating, stock, brand, category, thumbnail))
        
        # Populates product_images table using INSERT or REPLACE looking at image_url to ensure no duplicates 
        images = product_data.get('images', [])
        for image_url in images:
            cur.execute(populate_images, (product_id, image_url, image_url))
    
    # Commit to the DB
    conn.commit()
    
    # Close the cursor and connection
    cur.close()
    conn.close()
    
    
    print("Data inserted or updated successfully.")
else:
    print("Failed to retrieve data from the API.")
