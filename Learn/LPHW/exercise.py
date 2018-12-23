
# Exercise independent of any subject
from random import randint
# students list
paswd = randint(1,2)
selection = input('Password : ')
trial = 1
while int(selection) != paswd and trial < 3:
    print("Try again!")
    trial += 1
    selection = input('Password : ')

print(trial)
