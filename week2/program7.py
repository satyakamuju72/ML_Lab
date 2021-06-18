import mysql.connector

#create database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mllab")

#Create table
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="mllab"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customer(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#Insert data
sql = "INSERT INTO customer(name, address) VALUES (%s, %s)"
val = ("David", "California")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) inserted.")

#insert multiple rows
sql = "INSERT INTO customer(name, address) VALUES (%s, %s)"
val = [
    ("Lily", "California"),
    ("David", "San Francisco"),
    ("Micheal", "Las Vegas"),
    ("Sarah", "New York")
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) inserted.")

#Extract data
mycursor.execute("SELECT * FROM customer")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
