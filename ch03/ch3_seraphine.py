#first way

#print('what is your name? ')
#user_name = input().upper()
#print('Hello {}!'.format(user_name))


#second way

#user_name = input('What is your name? ')
#user_country = input('Where are you from? ')
#
#user_name = user_name.upper()
#
#print('Hello {}! you are from {}'.format(user_name,user_country.title()))

#third way 
#name = input("What’s your name? ")
#city = input("What’s your city? ")
#age = input("What’s your age? ")
#age = str(age)
#print ("Hello {}! from {} I am {} years old!".format(name.upper(),city.title(),age ))


def hello_world():
    my_details()

def my_details():
    user_name = input('What is our name? ')
    print ("My name is {}".format(user_name.title()))
    add_numbers()
    
def add_numbers():
    user_age = input('what is your age ? ')
    print(int(user_age) + 2)
    favourite_player()
    
def favourite_player():
    input('who is your favourite player? ')
    print("You lie !! Your favourite player is Murray ;yeah yeah")
    
#    
#def my_calculator ():
#    first_number = input('Enter your first number? ')
#    second_number = input('Enter another number? ')
#    user_operation = input('Enter an operation? ')
#   
#    print (int(first_number) + int(second_number))
#   
    
def hello_name(name):
   print('hello ' + name + '!')
    
    
    
    
    
    
    
    

