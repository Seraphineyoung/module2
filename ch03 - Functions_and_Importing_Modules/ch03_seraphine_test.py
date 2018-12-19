
#Test file

#Import * imports everything fromt the test function file

#############################TASK 1 #####################################
#Input from User

from ch03_seraphine_function import *

centigrade = input('what is your centigrade: ?')

new_kelvin , new_fahrenheit = temp_conversion(centigrade)
print (new_kelvin,new_fahrenheit)



#The second way imports the file and to access a function, you would have to call the test file name dot the function you want.

#import ch03_function
#centigrade = input('what is your centigrade: ?')
#
#ch03_function.temp_conversion(centigrade)
#new_kelvin , new_fahrenheit = ch03_function.temp_conversion(centigrade)



