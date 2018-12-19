

#class Customer(object):
#     
##     A customer of ABC Bank with a checking account.
##     Customers have the following properties:
##     Attributes:
##     name: A string representing the customer's name.
##     balance: A float tracking the current balance of the
##     customer's account.
#    
#  
#    def __init__(self,name,balance,overdraft=0):
#        """Return a Customer object whose name is *name* and
#         starting balance is *balance*."""
#        self.name = name
#        self.balance = balance
#        self.overdraft = overdraft
#        
#    def overdraft_limit(self,overdraft):
#        if self.balance >= 1500:
#            self.balance += overdraft
#            return self.balance
#        else:
#            return('Your have less than 1500 in your acccount and not eligible for overdraft')
#            
#    
#    def withdraw(self,amount):
#        """Return the balance remaining 
#        after withdrawing *amount*dollars."""
#        
#        if amount > self.balance:
#            raise RuntimeError('Amount greater than available balance.')
#        self.balance -= amount
#        return self.balance
#    
#    def deposit(self,amount):
#        """Return the balance remaining after depositing *amount* dollars."""
#        self.balance += amount
#        return self.balance
#
#
#cust_name = input('what is your name?: ')
#customer_1 = Customer(cust_name ,0 )
#print('Welcome' ,customer_1.name , 'Thank you for registering your name')
#deposit_amount = int(input('How much do you want to deposit today?: '))
#add_to_balance = (customer_1.deposit(deposit_amount))
#print('Your current account balance is' ,customer_1.balance)
#customer_withdraw = int(input('How much do you wanna withdraw today? :'))
#
#print('You withdrew ', customer_withdraw,'and your remaining balance is ', customer_1.balance - customer_withdraw)
#
#print(f'Your balance is {customer_1.balance}.If your balance is >= 1500, you are eligible for a £500 overdraft', customer_1.overdraft_limit(500))


#INHERITANCE IN OOP - Task 2

class Animal():
    def __init__(self,age ):
        self.age = age
           
    def eat(self):
        print('yum')
        
    def new_age(self,age):
       self.age += age
       return self.age
        
class Dog(Animal):
    def bark(self):
        print('Woof!')
    
        
class Cat(Dog):
    def meow(self):
        print('Meow')
 
#Because the __init__ function takes in an age argument, you have to pass an age to the instance of the classs.
       
clinton = Dog(5)
clinton.eat()
print(clinton.new_age(5))

claireCat = Cat(7)
claireCat.bark()
print(claireCat.new_age(5))
claireCat.meow()      
        


#INHERITANCE IN OOP - Task 3

class Robot():
    def move(self):
        print('I am moving...')
        
    def HairCut(self):
        print('Its time for a hair cut')
        
class CleanRobot(Robot):
    def clean(self):
        print('I am cleaning your room')
        
class CookRobot(Robot):
    def cook(self):
        print('I am cooking joll of rice')
        
GrandMa = CleanRobot()
GrandMa.clean()
GrandMa.HairCut()
        

 #ASSOCIATION IN OOP - Task 3      
      
            
class SuperRobot():
    def __init__(self):
        self.zeddy = Robot()
        self.snoopy= Dog(10)
        self.moory = Cat(10)
        self.tidy = CleanRobot()
        
    def playGame(self):
        print('perfect game')
    def move(self):
        return self.zeddy.move()
    def bark(self):
        return self.snoopy.bark()
    def meow(self):
        return self.moory.meow()
    def clean(self):
        return self.tidy.clean()
        
machineDog = SuperRobot()

machineDog.move()
machineDog.bark()
machineDog.playGame()
machineDog.clean()


#USER INPUT AND CLASSES 
snoopy = Dog(10)
moory = Cat(5)
new_age = int(input('what is moory\'s age: ?'))
print(moory.new_age(new_age))
snoopy.bark()
snoopy.eat()
my_day_age = snoopy.new_age(11)
print(my_day_age)


















































