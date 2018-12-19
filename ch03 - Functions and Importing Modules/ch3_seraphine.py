"""
#first way

print('what is your name? ')
user_name = input().upper()
print('Hello {}!'.format(user_name))


#second way

user_name = input('What is your name? ')
user_country = input('Where are you from? ')

user_name = user_name.upper()

print('Hello {}! you are from {}'.format(user_name,user_country.title()))

#third way 
name = input("What’s your name? ")
city = input("What’s your city? ")
age = input("What’s your age? ")
age = str(age)
print ("Hello {}! from {} I am {} years old!".format(name.upper(),city.title(),age ))


def hello_world():
    my_details()

def my_details():
    user_name = input('What is our name? ')
    print ("My       name{}".format(user_name.title()))
    add_numbers()
    
def add_numbers():
    user_age = input('what is your age ? ')
    print(int(user_age) + 2)
    favourite_player()
    
def favourite_player():
    input('who is your favourite player? ')
    print("You lie !! Your favourite player is Murray ;yeah yeah")
    
  
   
def my_calculator ():
    first_number = input('Enter your first number? ')
    second_number = input('Enter another number? ')

 
    print (int(first_number) + int(second_number))
  
    
def hello_name(name):
   print('hello ' + name + '!')

car = 100
space_in_a_car = 4.0
drivers = 30
passengers = 30
cars_not_driven = car - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print('There are' , car, "cars available" )
print('There are only', drivers, 'drivers available')
print('There will be', cars_not_driven, 'empty cars today')
print('We can transport', passengers, 'to carpool today')
print('We need to put about', average_passengers_per_car, 'in each car')
"""

def hello_world_2args(d,e,f,g):
    print("my name is {} {} and I am {} years old".format(e,f,g))

a1 = 'hello'
b1 = 'world'
a2 = 'love'
b2 = 'coding'
s1 = 'seraphine'
s2 = 'young'
s3 = 28

hello_world_2args(a1,b1,a2,b2)

hello_world_2args(s1,s2,s3,b2)


def add_two_numbers(numb1,numb2):
    print(int(numb1) + int(numb2))
    
#add_two_numbers(2,2)


def add_new_twonumbs(num1 , num2):
    print(num1 + num2)
     
#add_new_twonumbs(1,3)

#mid-class challenge
    




def temp_conversion(centigrade):
    centigrade = int(centigrade)
    fahrenheit = centigrade * 9.0/5.0 + 32
    kelvin = centigrade + 273.15

    print("That's" ,  fahrenheit ,  "degrees in fahrenheit and" , kelvin , "degrees in kelvin.")
    return (kelvin , fahrenheit)




new_kelvin , new_fahrenheit = temp_conversion(centigrade)













































