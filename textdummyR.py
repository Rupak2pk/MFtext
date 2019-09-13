#!/usr/bin/python3

#Rupak Kannan and Ella Adam

#Sep 6 2019

#This is a dummy for text based options and multiple variable responses.
#basic intro
def intro():
	print("Welcome to the test dummy!")
	print("------------------------")
	print("Determine the best choices for each question by typing either 1,2 or 3")
	print("---------------------------------------------------------------")
	print("TEXT BOX")
	print("-----------------------------------------")
	dummytext1 = ("Welcome to Hades")
	print(dummytext1)
	print("")
	print("")
	options()
#restarting the program
def oops():
	print("Thats something you shouldn't say, try again")
	end()
#end
def end():
	print("------------")
#your potienal responses
def options():
	dummyoption1 = ("Get me the hell out")
	print("1:", dummyoption1)
	dummyoption2 = ("Where is hades?")
	print("2:", dummyoption2)
	dummyoption3 = ("Alright")
	print("3:", dummyoption3)
	Answer1 = input("input option: ")
	

	if (Answer1 == '2') or (Answer1 == 'Where is hades?') :
		print("--------")
		print("Silly you, THIS is Hades!")
		end() 

	elif (Answer1 == '3') or (Answer1 == 'Alright') :
		print("--------")
		print("Thats the best thing you've ever said!")
		end()

	elif (Answer1 == '1') or (Answer1 == 'Get me the hell out') :
		print("--------")
		dummyres1question()
		end()

	elif (Answer1 == 'WRRRYYY') :
		print('YOU FELL FOR IT FOOL')
		print('THUNDER CROSS SPLIT ATTACK')
		end()
	else :
		oops()

#something something branching options
def dummyres1question():
	print("Woah there buddy, watch your vulgarity, are you okay?")
	print( "1:Yes  2:No")
	Answer2 = input("")
	
	if (Answer2 == 'Yes') or (Answer2 == '1') :
		print("--------")
		print("Oh okay")
		end()

	elif (Answer2 == 'No') or (Answer2 == '2') :
		print("--------")
		print("Not okay")
		end()
	else :
		oops()

intro()



