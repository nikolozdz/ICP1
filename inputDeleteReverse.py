import random

userInput = input('Please input some string: ')
if len(userInput) >= 2:
    for i in range(2):
        randomChar = userInput[random.randint(0,len(userInput)-1)]
        userInput=userInput.replace(randomChar,'')

outputString=userInput[::-1]

print(outputString)
