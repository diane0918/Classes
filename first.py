# Basics
# __var = 1
# var2 = 2
# var3 = 3
# var4 = 'hello world!'
# var5 = 'i am python!'
# var6 = '7'
# var7 = var3 + int(var6)
# print(__var + var2 + var3)
# print(var4+' '+var5+' '+str(var2))
# var4 = 4
# print(var4)

# parsing methods str() , int(), double(), float()
# conditional statement
# john_age = 24	#int
# alex_age = 1
# if john_age > 1 and john_age <= 5:
# 	print( "John age is "+str(john_age) )
# 	if alex_age > 1 and alex_age <= 5:
# 		print( "Alex age is " +str(alex_age) )
# elif john_age > 5 and john_age <= 10:
# 	print("John Age is range 5 - 10 " + str(john_age) )
# 	if alex_age > 5 and alex_age <= 10:
# 		print("Alex age is " +str(alex_age) )
# elif john_age > 10 and john_age <=15:
# 	print("John age range 10 - 15 " + str(john_age))
# 	if alex_age > 10 and alex_age <= 15:
# 		print("Alex age is " +str(alex_age) )
# else:
# 	print("John and alex aged 15 and above")

# Loops
# function range(0, 10) list[0 - 10]
# for(x=0;x<10;x++)
# array - list
# arr = [] ---> int arr = [] --> $arr = array()
# items = range(0, 10)
# year3_students = [
# 	'alex', 
# 	'john', 
# 	'airel', 
# 	'joy', 
# 	'lopez',
# 	'karl'
# ]
# year4_students= [
# 	'kevin',
# 	'mayang',
# 	'jason',
# 	'biol',
# 	'christian'
# ]
# emp = []
# it_year_lvl = [
# 	emp,
# 	year3_students,
# 	year4_students
# ]
# for it in it_year_lvl:
# 	print(it)
# 	for st in it:
# 		print(st)
# # for(x=0;x<10;x++)
# for x in range(0, 10):
# 	print(x)


# Use loop and conditional statement
# create a range 0 to 100 and loop it
# display "even "+number if value is even
# and display "odd "+number if odd
# sample:
# 2
# even 2
# 3
# odd 3
# item 3
# Hint: use item%2 = 1

# lists = range(0, 100)
# for l in lists:
# 	if l%2 == 1:
# 		print('Odd '+str(l))
# 	else:
# 		print('Even '+str(l))
# import string
# import random
# #raw_input()
# name = input("enter Name :")
# print(name)
# # random.choice(string.ascii_letters)
# strr = ''
# rand = random.randint(1, 10)
# while rand > 0:
# 	strr += random.choice(string.ascii_lowercase)
# 	rand-=1
# print(strr)
# rand = random.randint(1, 10)
# while rand > 0:
# 	print(rand)
# 	int(), str(), 
# 	var = '1'
# 	var = int(var)!=
# 	rand-=1 #rand = rand-1, rand--
# Guess what i am thinking!
# 1. Ask the user to input his/her name
# 2. generate a random number and let the user guess it. 1-20 random number
# 3. Promtp the user to guess the number.
# 4. "What number i am thinking?" -> ask for user input
# 5. check if user is correct or wrong
# 6. if correct, promtp the user that he/she is correct.
# 7. else, tell him/her that his/her guess is incorrect.
# 8. let him/her guess again
# var+""+var+""+var
# What is your name: Ferdz
# Guess what im thinking? 4
# Ferdz, you are incorrect! Guess again.
# Guess what im thinking? 3
# Ferdz, you are incorrect! Guess again.
# Guess what im thinking? 5
# Congrats!! you are correct.

import random
name = input("Enter Name:")
rand = random.randint(1,15)
flag = True
while flag:
	num = int(input('Guess: '))
	if num == rand:
		print("Congrats!!")
		flag = False
	else:
		print("Incorrect")

























