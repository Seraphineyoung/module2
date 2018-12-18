
x = 33

while x >= 1:
    
    print(x,': ',end='')
    
    x = x/2
    
print(x)


def tri(n):
    
    number = 0
    
    while n > 0:
        
       number = number + n
       
       n = n - 1
        
    return number
    

print(tri(4))


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
            
             
student_result()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    