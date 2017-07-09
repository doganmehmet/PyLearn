# PROMPTING AND PASSING

from sys import argv

script, user_name = argv
promt = '>'

print(f"Hi {user_name} I am script {script}")
print("I'd like to ask you a few questions")
print(f"Do you like me {user_name}")
likes = input(promt)

print(f"Where do you live {user_name}")
lives = input(promt)

print("What kind of computer do you have?")
computer = input(promt)

print(f"""
Alright, so you said {likes} about me
You live in {lives}
and you have {computer} model computer
""")
