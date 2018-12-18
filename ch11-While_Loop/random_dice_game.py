
from random import randint

def randomGame ():
    
    
    userInput = ''
    
    while userInput != 'quit':
        num1 = randint(1,6)
        num2 = randint(2,6)
        add_num = num1 + num2
        print(add_num)
        
        userInput = input('Enter even or odd to play or quit to exit the game')
        if userInput == 'even' and add_num % 2 == 0:
            print(add_num)
            print('You Win Yay')
            
        elif userInput == 'odd' and add_num % 2 != 0:
            print('You Win Yay')
            
        elif userInput == 'quit':
            break
        
        else:
            print('You lose')
            
    print ('So sad to see you go')       
       
    

    
randomGame()   