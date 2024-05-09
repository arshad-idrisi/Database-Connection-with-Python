import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "arshad123",
    database = "arshad_db"
)
# print("connected", mysql)  // check your python has connected to MYSQL database
cur = mydb.cursor()

# create table in a database.

'''s = "create table book(" \
    "id int not null, " \
    "name varchar(50)," \
    "course varchar(40)," \
    "location varchar(30))"
cur.executemany(s)'''


# insert one value in a table.

'''s = "insert into book" \
    "(id, name, course, location)" \
    "values(%s, %s, %s, %s) "
b = (1, "arshad", "python", "malad")
cur.executemany(s, b)
mydb.commit()'''


# insert multiple value in a table.

'''s = "insert into book" \
    "(id, name, course, location)" \
    "values(%s, %s, %s, %s) "
b = [(2, "dipesh", "python", "nalasopara"), (3, "kuldeep", "java", "dadar"), (4, "prakash", "R", "borivali")]
cur.executemany(s, b)
mydb.commit()'''


# fetch all data in for loop.

'''s = "select * from book"
cur.execute(s)
result = cur.fetchall()
for s in result:
    print(s)'''

# how to update data in a table.
'''s = "update book set course = 'data science' where id = 4"
cur.execute(s)
mydb.commit()'''


# how to delete data in a table.
'''s = "delete from book where course='data science'"
cur.execute(s)
mydb.commit()'''

# if you want to show all data in the table. then use this command...

s = "select * from book"
cur.execute(s)
result = cur.fetchall()
for i in result:
    print(i)