
#exercise 6

metal = {}

metal['iron'] = (7.8,6,12)
metal['gold'] = (1.3,20,2)
metal['zinc'] = (4.9,3,9)
metal['lead'] = (9.9,2,20)
metal['silver'] = (2,10,4)


#returning only keys

metal_keys_only = metal.keys()

#converting keys into a list
metal_keys_list = list(metal_keys_only)


#sorting the second value in decending order and returning the keys only
metal_keys_list.sort(reverse = True,key=lambda k:metal[k][1])


print(metal_keys_list)


#returning key-value pairs for the second position in descending order
sorted_value = sorted(metal.items(),reverse= True,key=lambda kv: kv[1][1])
print(sorted_value)



salary = {}
salary['sera'] = 20000
print(salary)
salary['brothers'] = ['Ekema','daddy','Etete']

#Updating a value or key on the dictionary
salary['sera'] += 1000
print(salary)

classMates = {}

classMates['mel'] = 862
classMates['mari'] = 885
classMates['seraphine'] = 385



classMates['seraphine'] = 7532633368
classMates['mel'] = 86256
classMates['mari'] = 88595



tilly = 'tilly'

classMates['jennifer'] = 3456
classMates['sarika'] = 862
classMates[tilly] = 687

print(classMates)

#Delete an item in Dictionaries

del classMates[tilly]

##getting the keys from the classmate dictionaries
#print(classMates.keys())

#getting the values of the key in classmate dictionaries
print(classMates.values())

#getting the keys and casting it into a list.. Remember to always use list()
phone_keys = list(classMates.keys())

#getting the key at position 1 of the phone_keys array
phone_values = list(classMates.values())

mari_val = (phone_keys[1])



if 'sarika' in classMates:
    print('sarika', ':', classMates['sarika'])
else:
    print('sarika', 'not found !')



labels = list(classMates.keys())

print(labels)

labels.sort(key=lambda a:classMates[a])

print(labels)

family = {}

family ['makims'] = ('may' , 5,'tase')
family ['patrick'] = ('july' , 4,'base')
family ['etubom'] = ('Dec' , 10,'vese')
family ['eno'] = ('mar' , 21,'pase')


family_keys = list(family.keys())

print(family_keys)

family_keys.sort(key = lambda f:family[f][2][-1])

print(family_keys)

family_keys.sort(reverse = False, key=lambda f:family[f])

print(family_keys)

family_keys.sort(reverse = True, key=lambda f:family[f])

print(family_keys)










