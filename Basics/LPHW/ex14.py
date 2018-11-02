# Prompting and Passing

from sys import argv

this_script, username = argv
prompt = '>'

print("Hi {} I am {}".format(username, this_script))
print("I'd like to ask you a few questions.")
print(f"Do you like me {username}")
likes = input(prompt)

print(f"Where do you live {username}")
lives = input(prompt)


print("What kind of computer do you have {}".format(username))
computer = input(prompt)

print("""So, you said {} about me.
You live in {}. I know where it is.
And you have a {} computer.
""".format(likes, lives, computer))
