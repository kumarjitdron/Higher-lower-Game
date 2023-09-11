import os
import sqlHandler
from gameData import data
from art import logo,vs
import random
flag=True
score=0
n=sqlHandler.nameRe()
m=sqlHandler.scoreRe()
name=input("Enter Your Name: ")
user=random.randint(0,49)
while flag==True:
	print(logo)
	print(f"Highest Score: {m} by {n}")
	print(f"Your Current Score: {score}")
	comput=user
	user=random.randint(0,49)
	while user==comput:
		user=random.randint(0,49)
	print("Compare A:",data[comput]["name"],",",data[comput]["description"],"from",data[comput]["country"])
	print(vs)
	print("Against B:",data[user]["name"],",",data[user]["description"],"from",data[user]["country"])
	res=input("Who has more followers? Tyoe 'A' or 'B':").lower()
	if res=='a':
		if data[comput]['follower_count']>data[user]['follower_count']:
			score+=1
			os.system("cls")
		else:
			print(f"Your Final score: {score}")
			flag=False
	elif res=='b':
		if data[comput]['follower_count']<data[user]['follower_count']:
			score+=1
			os.system("cls")
		else:
			print(f"Your Final score: {score}")
			flag=False	
if score==m:
	sqlHandler.updateRe(name,score)	
else:
	sqlHandler.insertA(name,score)


	


