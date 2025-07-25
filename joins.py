import sqlite3

conn = sqlite3.connect("data1.db")
cursor = conn.cursor()

# query = "CREATE table s1('id' INT PRIMARY KEY,'name' varchar(50),'rollno' INT)"
# result = cursor.execute(query)

# cursor.execute("PRAGMA table_info(s1)")
# print(cursor.fetchall())
# print(result)

# cursor.execute("INSERT INTO s1 values('1','Raj','1')")
# cursor.execute("INSERT INTO s1 values('2','Rahul','2')")
# cursor.execute("INSERT INTO s1 values('3','Ram','3')")

# output = cursor.execute('SELECT * from s1')
# for row in output.fetchall():
#     print(row)
    
    
# query = "CREATE table s2('rollno' INT PRIMARY KEY,'marks'INT,'course_name' varchar(50))"
# cursor.execute(query)

# cursor.execute("INSERT INTO s2 values('1','50','Maths')")
# cursor.execute("INSERT INTO s2 values('2','80','Science')")
# cursor.execute("INSERT INTO s2 values('3','95','English')")

# output = cursor.execute("""\n\nSELECT * from s1
#                         CROSS JOIN s2
#                         ON s2.rollno=s1.rollno
#                         """)
# for row in output.fetchall():
#     print(row)   
    
    
cursor.execute("""
                DELETE s2 FROM s2  
                INNER JOIN s1 ON s2.rollno = s1.rollno
                WHERE s2.rollno = 2;

               """)
# conn.commit() 
conn.close()
print("DB closed")

# DELETE s2
#                FROM s2
#                INNER JOIN s1
#                ON s2.rollno=s1.rollno
#                WHERE s2.rollno=2