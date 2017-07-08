# ESCAPE SEQUENCES

# ESCAPE            WHAT IT DOES
# \\                Backslash(\)
# \'                Single-quote(')
# \"                double-quote(")
# \a                ASCII bell (BEL)
# \b                ASCII backspace (BS)
# \f                ASCII formfeed (FF)
# \n                ASCII linefeed (LF)
# \N{name}          Character named name in the Unicode database (Unicode only)
# \r                Carriage return (CR)
# \t                Horizontal tab (HT)
# \uxxxx            Character with 16-bit hex value xxxx
# \Uxxxxxxxx        Character with 32-bit hex value xxxxxxxx
# \v                ASCII vertical tab (VT)
# \ooo              Character with octal value ooo
# \xhh              Character with hex value hh

# let's define variables and use some escape sequences
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat ulan." # \\ puts a backslash
fat_cat = """I'll do a list:
\t* cat food
\t* fishes
\t* catnip\n\t grass
"""

# also possible to use three sing quotes instead of double. that is just a matter of style and preference.


print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
