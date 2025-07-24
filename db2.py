import sqlite3

try:
    connection = sqlite3.connect("storage.db")

    cursor = connection.cursor()

    query = "SELECT sqlite3_version();"
    cursor.execute(query)
    print("Database init")

    result = cursor.fetchall()

    print("SQLite version is {}",result[0])
    cursor.close()
except sqlite3.Error as e:
    print("Something went wrong",e)
finally:
    if connection:
        connection.close()
        print("SQL server stopped!")
    
