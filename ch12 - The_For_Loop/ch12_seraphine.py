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
#############################Task 3 ###############################
##Create your own list
#    
#values = ['this', 55, 'that']
#
#for item in values:
#    print('***', item)
#    
#    
###########################Task 4###################################
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
    
########################Task 6 and 7 ####################################
#Loop through dictionary data type
    
metal = {}

metal['iron'] = (7.8,6,12)
metal['gold'] = (1.3,20,2)
metal['zinc'] = (4.9,3,9)
metal['lead'] = (9.9,2,20)
metal['silver'] = (2,10,4)

metal_list = list(metal.keys())

#print(metal_list)
#
#metal_list_value = sorted(metal.items(),reverse= True,key=lambda kv: kv[1][1])
#
#print(metal_list_value)
#
#for items,itemsvalues in metal_list_value:
#    print(items,itemsvalues[1])
#    
    
        
    
# sorting through the metal_list wish holds the keys and print out the each key and use each key to print out the values in metal[items][1].. the [1] at the end is getting the second value at the end.   
    


########################Task 8 ####################################
#Combine counting loop and conditionals to filter out values

for items in metal_list:
    if metal[items][0] > 7:
        print(items,metal[items][1])
        
        
########################Task 9 ####################################
#Design a sum function
        
values = [3,12,9]
total = 0
for val in values:
    total += val
print('TOTAL: ' + str(total))
         
        
        
        

def SumValues(values):
    sum_Values = 0
    for val in values:
        sum_Values += val
    return sum_Values
    
    print('TOTAL: ' + str(sum_Values))
    
        



























   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    