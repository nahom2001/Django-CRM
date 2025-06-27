import mysql.connector

# Establish a connection to the database
data_base = mysql.connector.connect(
    host='localhost',
    user='root',
    password='nahom#db'  # Use 'password' instead of 'passwd'
)

# Prepare a cursor object
cursor_object = data_base.cursor()

# Execute a query to create a database
cursor_object.execute("CREATE DATABASE elderco")

# Close the cursor and connection
cursor_object.close()
data_base.close()
