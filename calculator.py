def add():
    a = int(input ("enter your first number:  "))
    b = int(input ("enter your second number: "))
    x= a+b
    print(x)

def sub():
    a = int(input ("enter your first number:  "))
    b = int(input ("enter your second number: "))
    x= a-b
    print(x)

def mul():
    a = int(input ("enter your first number:  "))
    b = int(input ("enter your second number: "))
    x= a*b
    print(x)

def div():
    a = int(input ("enter your first number:  "))
    b = int(input ("enter your second number: "))
    x= a/b
    print(x)
x=0
while True:
    calc = input ("Hey do you wanna calculate? \n 1 to add \n 2 to substract \n 3 to multiply \n 4 to divide \n >>>")
    if calc == "1":
        add()

    elif calc == "2":
        sub()

    elif calc == "3":
        mul()

    elif calc == "4":
        div()

    else:
        input("press any key to exit")
        break
