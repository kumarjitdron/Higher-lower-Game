import mysql.connector as a
mydb=a.connect(
	host="localhost",
	user="root",
	password="Password"#Enter your sql Password Here!!!
	)
cur=mydb.cursor()
s="create database game1"
cur.execute(s)
s1="use game1"
cur.execute(s1)
s2="create table acheiver(name varchar(50),score int)"
cur.execute(s2)
mydb.commit()
