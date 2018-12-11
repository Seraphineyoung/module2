
def userInput ():
    attempt = input('Please enter your password?:' )
    return attempt

def DataBundlePurchase(truePasscode, balance):
    
     counter = 0
 
     if userInput() == truePasscode and counter < 3:
        return transaction_type(balance)
    
     elif userInput() != truePasscode and counter < 3:
         counter +=1
         userInput()
         
         if counter <= 3:
             return 'you have tried 3 time, we would log you out now'
         
 

#def DataBundlePurchase(truePasscode, balance):
#
#    count = 0
#    while count < 3:
#        
#        UserInput = input('Please enter your password?:' )
#        if truePasscode == UserInput:
#            return transaction_type(balance) 
#      
#        else:
#            print('Wrong passcode')
#            count +=1
#            
#            if count == 3:
#                return'count is greater than 3'
#        
#
#result = DataBundlePurchase('1234', 34.55)
#print (result)
       
      
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False
    


def transaction_type(balance):  
    userOption = int(input('Enter 1 to check Credit Balance OR 2 to check Purchase Data bundle ? '))
    if userOption == 1:
        return f'Your Credit Balance is {balance}'
    elif userOption == 2:
        return 'Purchase Data Bundle is not available at this time'
    else:
        return 'Please choose a valid option'
    
def user_confirm_phone():
    first_num = int(input('Please enter your number'))
    second_num = int(input('Please enter your number'))
    
    if first_num == second_num :
        print ('num ok')
    
    else:
        print ('Your number do not match..Try again')
        
def credit_amount_input(balance):
    credit_amount = int(input('How much credit do you want ? Choose £5,£10, £15, £20'))
    if credit_amount > balance:
        print('Amount is higher than your available balance')

    
def mobile_data_bundle(balance):
    user_confirm_phone()
    

        
    
    


    
    
