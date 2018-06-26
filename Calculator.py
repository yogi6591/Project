#Write a python program to perform the mathematical calculations.
print("Hey,Welcome Mukesh Dubey")
import math
def Addition():
    print("\n")
    x=int(input("Enter any number"))
    y=int(input("Enter any number"))
    print("Sum of both these numbers=\n",x+y)
    print("\n")
    menu()


def Subtraction():
    x = int(input("Enter any number"))
    y = int(input("Enter any number"))
    print("Subtraction of both these numbers=\n", x - y)
    print("\n")
    menu()


def Multiplication():
    x = int(input("Enter any number"))
    y = int(input("Enter any number"))
    print("Multiplication of both these numbers=\n", x * y)
    print("\n")
    menu()

def Raise_to_power():
    x = int(input("Enter any number whose power you want to calcuate"))
    y = int(input("Enter any number that you want to use as power"))
    print("Result of the power=\n", x ** y)
    print("\n")
    menu()


def Divison():
    x = int(input("Enter any number"))
    y = int(input("Enter any divisor"))
    print("Result of Divison =\n", x * y)
    print("\n")
    menu()


def Floor_Divison():
    x = int(input("Enter any number"))
    y = int(input("Enter any divisor"))
    print("Result of Floor Divison =\n", x * y)
    print("\n")
    menu()


def Factorial():
    x = int(input("Enter any number"))
    print("Result of Factorial =\n",math.factorial(x))
    print("\n")
    menu()


def Exponential():
    x = int(input("Enter any number"))
    print("Result of Exponential =\n", math.exp(x))
    print("\n")
    menu()


def menu():
    print("***\nPress 0 to exit***")
    print("***Press 1 to perform Addition***")
    print("***Press 2 to perform Subtraction***")
    print("***Press 3 to perform Multiplication***")
    print("***Press 4 to perform Raise to power***")
    print("***Press 5 to perform Divison***")
    print("***Press 6 to perform Floor Divison***")
    print("***Press 7 to perfrom Factorial***")
    print("***Press 8 to perform Exponential***")
    x=int(input("Enter the number to perform the calculation that you want"))
    if x==1:
        Addition()
    elif x==2:
        Subtraction()
    elif x==3:
        Multiplication()
    elif x==4:
        Raise_to_power()
    elif x==5:
        Divison()
    elif x==6:
        Floor_Divison()
    elif x==7:
        Factorial()
    elif x==8:
        Exponential()
    elif x==0:
        exit()
    else:
        print("Oops,it's a wrong input")
        menu()

menu()
