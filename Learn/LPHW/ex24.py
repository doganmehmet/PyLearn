# More Practice

print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tGerilir zorlu bir yay\nOku firlatmak icin;
\tGece gokte dogar ay\nYukselip batmak icin.
\tMecnun inler, kanini\nLeyla'ya katmak icin.
\tCilve yapar sevgili\nGonul kanatmak icin.
\tSair neden gam ceker?\nSiir yaratmak icin.
\tDagda nicin bagrilir?\nFelege catmak icin.
\tAcilir tatli guller\nArilar tatmak icin.
\tTanri kizlar yaratmis\nErlere satmak icin.
\tInsan buyur besikte\nMezarda yatmak icin.
.......................
\tKahramanlar can verir\nYurdu yasatmak icin...
"""
print("............................")
print(poem)
print("............................")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))

# it is just like a f"" string
print(f"We'd have {beans} beans, {jars} jars and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)

# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates".format(*formula))
