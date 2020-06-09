input1 = int()
input2 = int()
while True:
    try:
        input1 = int(input('Please input FIRST integer value: '))
        break
    except ValueError:
        print("Please input integer type. Try again.")

while True:
    try:
        input2 = int(input('Please input SECOND integer value: '))
        break
    except ValueError:
        print("Please input integer type. Try again.")

plus=input1+input2
print("adding {}+{}={}".format(input1,input2,plus))
minus=input1-input2
print("subtracting {}-{}={}".format(input1,input2,minus))

