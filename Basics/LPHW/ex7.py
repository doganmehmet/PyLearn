# MORE PRINTING AND FORMATTING

# print the text Mehmet had a middle lamp. WoW! should be tasty
print("Mehmet had a middle lamp. WoW! should be tasty")

# It's fleece is as white as {}. / put snow after as with {}. by using .format()
print("It's fleece is as white as {}.".format("snow"))

# print text And everywhere that Mehmet went.
print("And everywhere that Mehmet went.")

# print 10 dots by multiplying one dot by 10
print('.' * 10)

# define 12 variables to store each letter in Cheese Burger
end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

# watch that comma at the end. (after end6)
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

""" comma in the line 30 allows us to write the second print (print(end7 + end8 + end9 + end10 + end11 + end12)) right after that. (yani bir alt line a degilde yanina yazdirdi - Chesse Burger. Burger i asagi satira attirtmadi
digerinin yanina ekledi) note that end = ' ' is special here. i.e. if we use for example mehmet = '' it will give error."""

# print(end1 + end2, mehmet = ' ') # it will give error cause' mehmet = ' ' is wrong. end = '' is special
