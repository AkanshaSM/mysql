import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="root123",db="Employee")
cursor=conn.cursor()
cursor.execute("use Employee")
cursor.execute("insert into EmpInfo values(01,'Akansha',35000);")
cursor.execute("insert into EmpInfo values(02,'Devi',25500);")
cursor.execute("insert into EmpInfo values(03,'Apurva',28000);")
cursor.execute("insert into EmpInfo values(04,'Meher',30000);")

cursor.execute("Select * from EmpInfo")
Emp=cursor.fetchall()
for i in Emp:
    print(i)

conn.commit()

cursor.close()
conn.close()



import mysql.connector

# Establish a connection to MySQL
conn = mysql.connector.connect(host="localhost", user="root", password="root123")

# Create a cursor
cursor = conn.cursor()

# Create the 'Employee' database
cursor.execute("CREATE DATABASE Employee")

# Switch to the 'Employee' database
cursor.execute("USE Employee")

# Create the 'EmpInfo' table
cursor.execute("CREATE TABLE EmpInfo (Emp_NO int NOT NULL, Emp_Name varchar(50), Salary int)")

# Insert data into the table
cursor.execute("INSERT INTO EmpInfo VALUES (01, 'Akansha', 35000)")
cursor.execute("INSERT INTO EmpInfo VALUES (02, 'Devi', 25500)")
cursor.execute("INSERT INTO EmpInfo VALUES (03, 'Apurva', 28000)")
cursor.execute("INSERT INTO EmpInfo VALUES (04, 'Meher', 30000)")

# Commit the changes
conn.commit()

# Select and display data
cursor.execute("SELECT * FROM EmpInfo")
Emp = cursor.fetchall()
for i in Emp:
    print(i)

# Close the cursor and connection
cursor.close()
conn.close()
