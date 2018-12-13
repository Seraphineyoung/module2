

my_favourite_fruits = ['apple','orange','banana']

x = ['this',55,'that',my_favourite_fruits]

print(x[0])

print(x[:])

x.remove(my_favourite_fruits)

x[1] = 'and'
x.append('again')

print(x)
print(x[::-1])
print(x[::1])
print(x[-3::])




x = ['the','cat','sat']

y = ['on','the','mat']
#this prints none because the append and extend functions does not have the return key word
a = x.extend(y)
b = y.append(x)

##this merges the 2 arrays in a new array keeping its original array brackets
print(y)

##this merges the 2 arrays in a new array and removed the brackets seperating the two arrays, so one big array
print(x)




##this creates a new list with x and y in one array
#
z = x + y
print(z)

z = x * 3
print(z)

##set function removes duplicate values and changes the data type to dictionaries. In dictionaries the keys has to uniques
##print(set(z))
#
##slicing a list
#
b = ['the','cat','sat','hair','food','skin','care']
#
##starts from 1 to n-1, so to 4-1 which is index 3
print(b[1:4])
print(b[3:5])
print(b[-1::-1])
print(b[-3:-1])

#SORT AND SORTED
x = [5,3,8,1,6,0,1,2,5]

#SORTED DOES NOT MUTATE X
y = sorted(x)

print(y)

print(x)

##this prints none as the sort() returns nothing, but x is mutated.
print(x.sort())

#prints out the mutated version
print(x)

#REVERSE SORT

x = [5,3,8,1,6,0,1,2,5]
y= ['the','cat','sat','hair','food','skin','care']

print(sorted(x))

print(sorted(x,reverse=True))

print(sorted(y,reverse=True))

print(sorted(y,reverse=False))


##
print(x[::-1])
#
##
print(x[:-2])
#
##
print(x[-3::])

#TUPLES

a = (5,3,8,1,6,0,1,2,'edem')

print(a[-1][-1])

#To change a data types you can cast Tuples to List and back to Tuple
b =list(a)

#tuples cant be added to or changed.

#del a[-1]
#
#print(a)
#
#a.append('z')

print(a)

b.append('seraphine')

print(b)










