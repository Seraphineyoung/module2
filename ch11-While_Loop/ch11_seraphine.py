##################### Task1 #######################
#repeated division 

#function to print series of values produced when doing repeated division (by 2) of some intial value
x = 33

while x >= 1:
    
    print(x,': ',end='')
    
    x = x/2   
print(x)



###################Task2#######################
#triangular numbers

#Writing a while number that takes a number n and computes traingular numbers.

def tri(n):
    
    number = 0
    
    while n > 0:
        
       number = number + n
       
       n = n - 1
        
    return number
print(tri(4))


################### Task3 #######################
#student's Mark

def student_result ():
    
    mark = 1 
    
    while mark > 0:
        
        mark = int(input('Please enter your score : ' ))
        
        if mark >= 70:
            print(f'Mark is {mark} - first class')
            
        elif mark >= 40:
            print(f'Mark is {mark} - pass')
            
        else:
            print(f'Mark is {mark} - fail')
            break
                      
student_result()

    
################### Task4 #######################
#Break in While Loops

i = 55

while i > 10:
    
    print(i)
    
    i = i * 0.8
    
    if i == 35.2:
        break

#################### Class Exercise ########################      

while True:
    name = input('Enter Your name ?')
    
    if name == 'done':
        break
    
    print(f'Hello {name}')
    
    
    
################### Task 5 & 6 #######################
from random import randint

def guess (attempts,rangeint):
    
    number = randint(1,rangeint)
    
    print('Welcome! Can you guess my secret number? ')
    
    print(f'you have {attempts} guesses remaining')
    
    
    
    while attempts > 0 :
        user_guess = int(input(' Make a guess between number 1 - 20 : '))
        attempts = attempts - 1
        
        if user_guess < number:
            print(f'you have {attempts} guesses remaining')
            print('Your guess is too low')
            
        elif user_guess > number:
            print(f'you have {attempts} guesses remaining')
            print('Nope your guess is too high')
            
        else:
            print('Well done ! You got it right')
            break
            
    print('GAME OVER: Thanks for playing. Bye.')
            
    
    
guess(6,20)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    