from sys import argv

#exercise 14
script, user_name, age = argv
prompt = 'waiting .......'

print(f'Hi {user_name}, I\'m the {script} script. ')
print('I\'d like to ask you a few questions.')
print(f'You are {age} years old')
print(f'Do you like me {user_name}?')



likes = input(prompt)

print(f'Where do you live {user_name}?')
lives =input(prompt)

print('What kind of computer do you have?')
computer = input(prompt)



print (f''' 
Alright,so you said {likes} about liking me. 
You live in {lives} and you are {age} years old. Not sure where that is.
And you have a {computer} computer. Nice.''')

print('would you like to change your age ?')
changenewage = input(prompt)

if changenewage == 'no':
    print (f''' 
           Alright,you answered {changenewage} to changing your age, so your age is {age}''')
elif changenewage == 'yes':
    print(f'What is your new age?')
    newage = input(prompt)
    print(f'Your new age is now {newage}')
else:
    print('Please type in yes or no')






































