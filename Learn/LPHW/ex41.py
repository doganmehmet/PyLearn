# Learning to Speak Object-Oriented

# class : tell Python to make a new type thing
# object : two meanings; the most basic type of thing, and any instance of some thing
# instance : what you get when you tell Python to create a class
# def : how you define a function inside a class
# self : insine the functions in a class, self is a variable for the instance/object being accessed
# inheritence : the concept that one class can inherit traits from another class, much like you and your parents
# composition : the concept that a class can be composed of other classes as parts, much like how a car has weels
# attribute : a property classes have that are from composition and are usually variables
# is-a : a phrase to say that somehting inherits from another, as in a "salmon" is-a "fish"
# has-a : a phrase to say that somehting is composed of other things or has a trait, as in "a salmon has-a mouth.


import random
from urllib.request import urlopen
import sys

WORLD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
     "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
     "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
     "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
     "Set *** to an instance of class %%%.",
    "***.***(@@@)":
     "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
     "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
# takes the words from the url(in WORLD_URL) and reads its lines and stores the values in WORD list
for word in urlopen(WORLD_URL).readlines():
    WORDS.append(str(word.strip(), encoding = "utf-8"))

# defining function called convert with two arguments; snippet and phrase
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append('. '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameters list
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL + D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            print(question)

            input('> ')
            print(f"ANSWER: {answer}\n\n")

except EOFError:
        print("\nBye")


# str.strip("chars") : This method returns a copy of the string in which all chars have been stripped from the beginning and the
# end of the string.

# example:
# str = "*****this is string example....wow!!!*****"
# print (str.strip( '*' ))

# returning output will be:
# this is string example....wow!!!


# random.sample(population, k) : returns a k length list of unique elements chosen from the population sequence. Used for
# random sampling without replacement.

# example:
# c = list(range(15))
# random.sample(c, 5)

# the reterning output may be(randomly chosen):
# [9, 2, 3, 14, 11] --> randomly chosen five values
