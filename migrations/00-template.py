import sqlite3

# setting up the database
conn = sqlite3.connect("./weather.db")
cursor = conn.cursor()

# https://sqlite.org/datatype3.html
cursor.execute("""
    
""")
# 4 data types: when you configure the databse you can be as specific as you want.

# tell the database to confirm the changes made by the EXECUTE command
conn.commit()

# ALWAYS close the connection
conn.close()