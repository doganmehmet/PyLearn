# Some data work

# Tuples
#   - fixed sized
#   - immutable
#   - elements can contain mutable objects like list

# creating a tuple
tpl = 1,2,5,6
print(tpl)

# printing out how many 2s exist in our tuple
print(tpl.count(2))


# unpacking tupple
x, y, z, t = tpl
print("Out tupple is unpacked:")
print(x); print(y); print(z); print(t)

# creating nested tuples
print("Nested tupple:")
tpl_of_tpls = (1, 2, 3), (10, 15)

print(tpl_of_tpls)

tpl2 = 10, 12, 30

print("tuple of tuples, lists, strings, booleans")
tpl_all = (1, 2, 5), (10, 15), [1,5,7], True, 10, "Haha"
print(tpl_all)

# combining tupples
tpl_combined = tpl + tpl2
print("Combined tuples: {}".format(tpl_combined))

print("The first elemnet of tuple : {}".format(tpl_all[0]))

print(f"The first element of list within the tuple is {tpl_all[2][0]}")

tpl_all[2][0] = 1000
print(f"This first element of list is now changed to {tpl_all[2][0]}")
print(tpl_all)

print("But we cannot change high level elements of tuple.", end = ' ')
print("Above we have just modified the element of a list within tupple.", end = ' ')
print("If we'd wanted to replace list itself wiht something else it would not be possible", end = ' ')
print("because tuples are immutable")
