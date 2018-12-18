
#Intializing a dictionary



def UserDetails(phone_book):
    
    counter = 0
    
    while counter < 2:
        name = input('what is your name ?')
        phoneNo = input('what is your phone number ?')
        luckyNo = input('what is your lucky number ?')
        postcode = input('what is your  postcde ?')
        city = input('what is your city ?')
        
        counter += 1
        
        
        if counter == 2:
            print('Maxed out')
            
    
        phone_book[name.title()] = [int(phoneNo), int(luckyNo), postcode, city ]
        
        
    
    
    
            
#    print('\nPhone book has ben updated with new classmate, ' + name.title(), ':\n', phone_book, '\n')

phone_book = {}

UserDetails(phone_book)

print(phone_book)





