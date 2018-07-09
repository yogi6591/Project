#Quiz question
print("<----- Hello!,Let's get started ----->\n")
print("\n*************************************\n")
print("We welcomes you to Our Introduction Application")
print("\n*************************************\n")
print("Featuring the Basic Project for Introduction")
print("\n*************************************\n")
print("Designed By Khushiram")
print("\n*************************************\n")
def gender():
    gen=input("Please enter your gender \n")
    if gen=='m' or gen=='male':
        print("Hello Sir,I'm Khushiram from Acadview ")
        your_name=input("Please enter your name\n")
        name(your_name)

    elif gen=='f' or gen=='female':
        print("Hello Mam,I'm Khushiram from Acadview ")
        your_nfreame=input("Please enter your name\n")
        name1(your_name)

    else:
        print("Sorry,this is not a valid input,so please enter your gender correctly\n")
        gender()

def name(your_name):
    a=your_name
    if your_name.isalpha():
        print("Hello Sir,Your Good Name is", a)
        print("I would like to collect some more information about you\n")
        your_age = input("Please tell me your age")
        age(your_age,a)
    else:
        print("you have entered wrong age,check wether you have entered any digit in name")
        your_name=input("Enter your name ")
        name(your_name)


def name1(your_name):
    b=your_name
    if your_name.isalpha():
        print("Hello Mam,Your Good Name is", b)
        print("I would like to collect some more information about you\n")
        your_age = input("Please tell me your age")
        age1(your_age,b)
    else:
        print("you have entered wrong name,check wether you have entered any digit in name")
        your_name = input("Enter your name ")
        name1(your_name)

def age(your_age,a):
    c=a
    if your_age.isdigit():
        if int(your_age) > 20:
            print("Welcome ", a, "Sir,as your age is", your_age,"years,so you are eligible for Pyhton fundamental course...\m")
        else:
            print("Oops Sorry",a, "Sir,as your age is", your_age,"years,so you are not eligible for Pyhton fundamental course...\m")
    else:
        print("you have entered wrong name,check wether you have entered any digit in name")
        your_age=input("Please tell me your age")
        age(your_age,c)

def age1(your_age,b):
    c=b
    if your_age.isdigit():
        if int(your_age) > 19:
            print("Welcome ",b, "Mam,as your age is", your_age,"years,so you are eligible for Pyhton fundamental course...\m")
        else:
            print("Oops Sorry",b, "Mam,as your age is", your_age,"years,so you are not eligible for Pyhton fundamental course...\m")
    else:
        print("you have entered wrong name,check wether you have entered any digit in name")
        your_age = input("Please tell me your age")
        age1(your_age,c)
gender()
