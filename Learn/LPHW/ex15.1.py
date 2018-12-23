# Asking user to provide a filename to print out its content

# prompt sign
prompt = '> '

# asking user to provide input and assingning result to file variable
print("Write the filename you wanna see plase?")
file = input(prompt)

# opening file
txt = open(file)

# printing out its content
print(txt.read())

# closing the file
print("Closing the file")

txt.close()
