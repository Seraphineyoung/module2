



def DataBundlePurchase(truePasscode, balance):
    
    if passwordCheck(truePasscode):
        if checkBalance(balance):
             return transaction_type(balance)     
        else:
            return f'Not enough balance'     
    else: 
        return f'Wrong passcode'
    
def passwordCheck(truePasscode):
    
    UserInput = input('Please enter your password?:' )
    if truePasscode == UserInput:
        return True
    else:
        return False
    
    
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False
    
def transaction_type(balance):
    
    userOption = int(input('Enter 1 to check Credit Balance OR 2 to check Purchase Data bundle'))
    
    if userOption == 1:
        return f'Your Credit Balance is {balance}'
    
    elif userOption == 2:
        return f'Purchase Data Bundle is not available at this time'
    
    else:
        return f'Please choose a valid option'
        
    
    


    
    
