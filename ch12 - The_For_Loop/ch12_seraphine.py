#
#####################Task 1 ########################################
##Loop through a list
#my_shopping_cart = ['cake','plates','plastic forks','juice','cups']
#
#for item in my_shopping_cart:
#    print(item)
#    
######################Task 2 #####################################
##Update List Values
#values = [875,23,451]
#
#for val in values:
#    print('--->' + str(val))
#    
#print()   
# 
#for val in values:    
#    print('--->' + str(val + 50))
#    
#
##############################Task 3 ##################################
#    
#    
#    
#    
#    
#    
#    
#    
############################Task 4######################################
##Loop through  a string data type
#    
#for char in "Yes":
#    print(char)
#    
## looping through a string, you have to split the string first and then loop
#for char in 'My name is seraphine'.split():
#    print(char)
#    
## This loops and where it see the letter e, it splits and forms a string without the letter e    
#for char in 'My name is seraphine'.split('e'):
#    print(char)   
#    
#    
###########################Task 5 ######################################
##Loop through a tuple
#
#for char in (1,3,5,2,3,5,3):
#    print(char)
#    
    
##########################Task 6 ######################################
    
metal = {}

metal['iron'] = (7.8,6,12)
metal['gold'] = (1.3,20,2)
metal['zinc'] = (4.9,3,9)
metal['lead'] = (9.9,2,20)
metal['silver'] = (2,10,4)

metal_list = list(metal.keys())

print(metal_list)

metal_list_value = sorted(metal.items(),reverse= True,key=lambda kv: kv[1])

print(metal_list_value)

for items in metal_list_value:
    print(items[0],items[1][1])
    

   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    