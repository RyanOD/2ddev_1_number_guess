# This version of the game introduces setting up an infinite loop and breaking upon condition to eliminate code repetition and achieve a more professional final result

import os	#import os class to allow for clearing of terminal screen
import random

os.system('clear')

print("Welcome to the number guessing game!\n")
max = int(input("Please input the max number for this game: "))

num = random.randint(0, max)
print(num)

while True:
	guess = int(input("Let's go! Your guess? \n"))

	if(guess > num):
		print("Too high")
	elif(guess < num):
		print("Too low")
	else:
		break

print("Correct!")