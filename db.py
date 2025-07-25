import sqlite3

try:
    connection = sqlite3.connect("data.db")
    
    cursor = connection.cursor()
    
    # query = """SELECT * from student;"""
    # cursor.execute("INSERT INTO student values('Rahul','Sharma','20','12')")
    # cursor.execute("INSERT INTO student values('Ram','Vyas','18','10')")
    # cursor.execute("INSERT INTO student('Name','Surname','Age','Class') values('Sam','Curran','25','16')")
    
    
    # cursor.execute('SELECT * from student')
    # for row in cursor.fetchall():
    #     print(row)
        
    # cursor.execute("UPDATE student set  Age=19, class=11 where Name='Ram'")
    # cursor.execute("")
    # cursor.execute('SELECT * from student')
    # for row in cursor.fetchall():
    #     print(row)
    
         
    # cursor.execute("DELETE from student where Name='Rohit'")

    # output = cursor.execute("SELECT * from student")
    # for row in output:
    #     print(row)
        
    # cursor.execute("CREATE table student1('id' INT PRIMARY KEY, 'name' VARCHAR(30), 'age' INT, 'rollno' INT, 'address' VARCHAR(50));")
    cursor.execute("INSERT INTO student1 values('1','Raghav','20','12','Indore')")
    cursor.execute("INSERT INTO student1 values('2','Aditya','25','21','Rau')")
    
    output = cursor.execute('SELECT * from student1')
    for row in output:
        print(row)
    
    
except ConnectionError as e:
    print("Failed to connect",e)
    
finally:
    if connection:
        connection.commit()
        connection.close()
        print("Connection Closed")