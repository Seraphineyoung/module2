

def add_two_numbers():
    num1 = input('what is your first number? :')
    num2 = input('what is your second number? :')
    answer = print(int(num1) + int(num2))
    return answer
    


def add_new_twonumbs(num1 , num2):
    answer = print(num1 + num2)
    return answer
     




def temp_conversion(centigrade):
    centigrade = int(centigrade)
    fahrenheit = centigrade * 9.0/5.0 + 32
    kelvin = centigrade + 273.15
    print("That's" ,  fahrenheit ,  "degrees in fahrenheit and" , kelvin , "degrees in kelvin.")
    return (kelvin , fahrenheit)


