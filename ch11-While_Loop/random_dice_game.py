
from random import randint

def randomGame ():
    game = 0
    
    userInput = ''
    
    while userInput != 'quit':
        num1 = randint(1,6)
        num2 = randint(2,6)
        add_num = num1 + num2
#        print(add_num)
        game += 1
        
        userInput = input('Enter even or odd and to play or quit to exit the game ?\n' )
        if userInput == 'even' and add_num % 2 == 0:
            print(add_num)
            print('You Win Yay')
            
        elif userInput == 'odd' and add_num % 2 != 0:
            print('You Win Yay....play again')
            
        elif userInput == 'quit':
            break
        
        else:
            print('You lose....play again')
            
    print (f'You have played {game} times only play 3 more times to have a perfect score...So sad to see you go')       
       
    

    
randomGame()   