# This version of our game represents the most basic implementation of number guessing.
# The player only gets 1 guess

import os	# import os class to allow for clearing of terminal screen
import random

os.system('clear')

print("Welcome to the number guessing game!\n")
max = int(input("Please input the max number for this game: "))

num = random.randint(0, max)
print(num)

guess = int(input("Let's go! Your guess? \n"))

if(guess < num):
	print("Too low!")
elif(guess > num):
	print("Too high")
else:
	print("Correct!")