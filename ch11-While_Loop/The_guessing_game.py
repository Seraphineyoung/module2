
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
            
        
        
        
        
        
        
    
    