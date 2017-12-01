# This version of our game introduces the concept of looping thereby giving the player infinite guesses
# Notice we have also 'introduced' code repetition...something we will deal with in the next version

import os	#import os class to allow for clearing of terminal screen
import random

os.system('clear')

print("Welcome to the number guessing game!\n")
max = int(input("Please input the max number for this game: "))

num = random.randint(0, max)
print(num)

guess = int(input("Let's go! Your guess? \n"))

while(guess != num):
	if(guess < num):
		print("Too low")
	elif(guess > num):
		print("Too high")
	
	guess = int(input("Let's go! Your guess? \n"))

print("Correct!")