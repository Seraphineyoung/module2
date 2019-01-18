import string

letters = (string.ascii_uppercase)

for letter in letters:
    
    b = letters.index(letter)
    new_b = b + 1
    
    if new_b % 3 == 0 and new_b % 4 == 0: 
        print( str(new_b) + letter.lower())
        
       else:
        
        
print(8%10)