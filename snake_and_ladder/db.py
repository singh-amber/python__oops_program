import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="mysql", database="test")
except Exception as e:
    print("!!!!An exception has occurred ", e)

mycursor = mydb.cursor()

# try:
#     mycursor.execute("create table demo1(name varchar(255), salary int)")
# except Exception as e:
#     print("!!!Exception is ", e)
try:
    mycursor.execute("insert into demo1 values('aman', 40000)")
    mycursor.execute("insert into demo1 values('vaibhav', 20000)")
    mycursor.execute("insert into demo1 values('raman', 46000)")
    mycursor.execute("insert into demo1 values('shyam', 50000)")
except Exception as e:
    print("!!!!Exception is, ", e)

mycursor.execute("select * from demo1")

for name, salary in mycursor:
    print("Name ", name, "Salary ", salary)

