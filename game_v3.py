# The final version of the game compresses the num determination code into a single, easy to read line

import os	#import os class to allow for clearing of terminal screen
import random

os.system('clear')

print("Welcome to the number guessing game!\n")
num = random.randint(0, int(input("Please input the max number for this game: ")))

while True:
	guess = int(input("Let's go! Your guess? \n"))

	if(guess > num):
		print("Too high")
	elif(guess < num):
		print("Too low")
	else:
		break

print("Correct!")