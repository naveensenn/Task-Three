import sqlite3

try:
    sqlConnect = sqlite3.connect("data.db")
    cursor = sqlConnect.cursor()

    print("Database initialised")


    query = "SELECT sqlite_version();"
    cursor.execute(query)

    result = cursor.fetchall()
    print("SQLite version is {}".format(result[0][0]))

    cursor.close()
    
except sqlite3.Error as error:
    print("Failed to connect",error)

finally:
    if sqlConnect:
        sqlConnect.close()
        print("SQL connection closed")
