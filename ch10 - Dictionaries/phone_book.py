
#Intializing a dictionary


def UserDetails():
    phone_book = {}
    
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
    
    return phone_book
    
    print('\nPhone book has ben updated with new classmate, ' + name.title(), ':\n', phone_book, '\n')


phone_book = UserDetails()


#phone_book = {'Seraphine': ('075', 7, 'BR5 7PL', 'Beckenham', 30),
#                  'Etubom': ('831', 2, 'BR8 3QV', 'Birmingham', 23),
#                  'Makims': ('380', 5, 'LT5 2HP', 'Archway', 25),
#                  'Patrick': ('700', 3, 'SL5 7TY', 'London', 25),
                  }



def sortByNameKey (phone_book):
    #sorting by key name key
    sortedByName = sorted(phone_book.items(),key=lambda kv:kv[0])
    print(sortedByName)
    
    
sortByNameKey (phone_book)


def sortByCity(phone_book):
#    phone_book_list = list(phone_book.keys())
    sortedBycity = sorted(phone_book.items(),key=lambda kv:kv[1][3])
    print(sortedBycity)
    
sortByCity(phone_book)   
    
    
def sortByLuckyNo(phone_book):
    sortedByluckyNo = sorted(phone_book.items(),key=lambda kv:kv[1][1])
    print(sortedByluckyNo)
    
sortByLuckyNo(phone_book)
    
    
    


























