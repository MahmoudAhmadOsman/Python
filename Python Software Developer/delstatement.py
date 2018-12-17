#del statement in python
#The del statement can be used to remove an item from a list by referring to its index, rather than its value.
value = [1,3,5,74,8,55]

#first list
print(value)

print('________________________________________ ')
print('With del() function used ')
print('\n')
#second value - with one value mission
del value[0]

for values in value:
    print(value)