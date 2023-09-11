import mysql.connector as a
mydb=a.connect(
	host="localhost",
	user="root",
	password="Password",#Enter Your Sql Password Here!!!!
	database="game1")
cur=mydb.cursor()
def nameRe():
	#s="select name from acheiver where score in (select max(score) from acheiver group by score) ;"
	s="select name from acheiver order by score desc;"
	cur.execute(s)
	d=cur.fetchall()
	for i in d:
		return i;

def scoreRe():
	#s="select score from acheiver where score in (select max(score) from acheiver group by score) ;"
	s="select score from acheiver order by score desc;"
	cur.execute(s)
	d=cur.fetchall()
	for i in d:
		return i;
	
	
def insertA(name,score):
	s="insert into acheiver values(%s,%s)"
	data=(name,score)
	cur.execute(s,data)
	mydb.commit()
def updateRe(name,score):
	s="update acheiver set name=%s where score=%s"
	data=(name,score)
	cur.execute(s,data)
	mydb.commit()
