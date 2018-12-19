
#Testing booleans TRUE or FALSE
age =15
myage = age >=13 and age <=19

print(myage)

age = 22
isaTeen = age >=13 and age <=19

print(isaTeen)



number = input("Enter a number between 1 and 10 ")
number = int(number)

########################Task3##########################

if number >10 :
    print("Too High")
if number< 0 :
    print("Too Low")
    
########################Task4##########################
if  type(number) == int :
    print("you have enter a number")
else:
    print("you have not enter a number")

########################Task5##########################
age = input("Enter your age ")
age = int(age)

if  age < 13:
    print('child')
elif age < 18 :
    print('teen')
    
elif age < 65 :
    print('adult')
else:
    print ('pensioner')




                 
