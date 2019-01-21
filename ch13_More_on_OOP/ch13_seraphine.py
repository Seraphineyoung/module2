#####################Task 1  #################
#Initialise the person

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        if gender == 'm':
            self.isMale = True
        elif gender == 'f':
            self.isMale = False
        else:
            print('Gender not recognised')
            
            
p1 = Person('John',44,'m')
print(p1.name)
print(p1.isMale)



class Person:
    def __init__(self,name,age,gender):
    
        def greetingInformal(self):
            print('Hi',self.name)
            
        def greetingFormal(self):
            if self.isMale:
                print('Welcome, Mr', self.name)
            else:
                print('Welcome, Ms', self.name)

###################Task 2 #####################
#More functunalities for the Person class
                
                
p1 = Person('Harry',12,'m')
p2 = Person('Jean',12,'f')
p1.greetingInformal()
p2.greetingFormal()

###################Task 3 ######################
#A greeting filter

class Person
    def greetingAgeBase(self):
        if self.age < 18:
            print('Welcome,young',self.name)
        elif self.age > 60:
            print('welcome, venerable', self.name)
        else:
            self.greetingFormal()
            
p1 = Person('Harry',12,'m')
p2 = Person('Amali',88,'f')
p3 = Person('Richard',50,'m')

p1.greetingAgeBased()
p2.greetingAgeBased()
p3.greetingAgeBased()
    
##################Task 4 #####################
#Create a subclass for the Person Class

class Wizard(Person):
    def greetingForml(self):
        print('welcome,Mr ', self.name, end=' ')
        print('- you\'re a fine wizard')

p1 = Person('Harry', 12, 'm')
p1.greetingFormal()

p1 = Wizard('Harry',12,'m')
p1.greetingFormal()

class Wizard(Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.isMale = True
        
        
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        if gender == 'm':
            self.isMale = True
        elif gender == 'f':
            self.isMale = False
        else:
            print('Gender not regconized')

##################Task 5 #####################
#Redefine init


class Wizard(Person):
    def __init__(self,name,age,gender):
        Person.__init__(self,name,age,'m')
        
        
        
##################Task 6 #####################
#Add new method to the wizard class
        
class Wizard(Person):
    def spell(self):
        print('Expelliarmus!')
        








