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
#    def __init__(self,name,balance=0.0,overdraft = 0):
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
#            print('Your have less than 1500 in your acccount and not eligible for overdraft')
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
#customer_1 = Customer('seraphine young', 1000.0,500)
#print(customer_1.name)
#add_to_balance = (customer_1.deposit(1200))
#print(customer_1.balance)
#
#customer_withdraw = int(input('How much do you wanna withdraw today? :'))
#
#print(customer_1.withdraw(customer_withdraw))
#
#print(customer_1.balance)
#
#print(customer_1.overdraft_limit(500))
#
#
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
        
class Robot():
    def move(self):
        print('...move move move...')
        
class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')
        
class Cat(Dog):
    def meow(self):
        print('Meow')
        
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





        
        
        
        
#snoopy = Dog(10)
#moory = Cat(5)
#
#new_age = int(input('what is moory\'s age: ?'))
#print(moory.new_age(new_age))
#
#snoopy.bark()
#snoopy.eat()
#my_day_age = snoopy.new_age(10)
#print(my_day_age)


















































