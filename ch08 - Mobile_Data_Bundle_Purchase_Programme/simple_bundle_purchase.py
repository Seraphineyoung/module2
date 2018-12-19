
def counter(truePasscode, balance):
    counter=0
    return DataBundlePurchase(truePasscode, balance, counter)



def DataBundlePurchase(truePasscode, balance, counter):
    
     userpasword = input('Please enter your password?: ' )

     if userpasword == truePasscode :
        return transaction_type(balance)
    
     elif userpasword != truePasscode and counter < 3:
          counter +=1
          return DataBundlePurchase(truePasscode, balance, counter)
         
            
     else:
         return f'you have tried {counter} time, we would log you out now'
         

      
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
         return user_confirm_phone(balance)
         
         
         
        #return 'Purchase Data Bundle is not available at this time'
    else:
        return 'Please choose a valid option'
    
def user_confirm_phone(balance):
    first_num = int(input('Please enter your phone number ? '))
    second_num = int(input('Please enter your phone number again ?'))
    
    if first_num == second_num :
        return max_top_up_amount(balance)
    
    else:
        print ('Your number do not match..Try again')
        

     
def max_top_up_amount(balance):
    
    credit_amount = int(input('How many GB do you want, Please enter multiples of 5? '))
    if credit_amount <= 35 and credit_amount < balance:
        if credit_amount % 5 == 0:
           new_balance = round(balance - credit_amount)
           return f'You have bought {credit_amount} and your remaining balance is {new_balance}'
        else:
            print( 'Please enter multiples of 5')
            return max_top_up_amount(balance)
    else:
        print('maximum amount has to be less than 35 and Your balance should be less than the top amount')
        return max_top_up_amount(balance)
    
    
    


        
    
    


    
    
