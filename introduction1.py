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
    if gen.isalpha():
        if gen=="m" or gen=="male":
            print("Hello Sir,I'm Khushiram from Acadview ")
            your_name=input("Can you tell me your name\n")

            if your_name.isalpha():
                print("Hello Sir,Your Good Name is", your_name)
                print("I would like to collect some more information about you\n")
                your_age = input("Please tell me your age")

                if your_age.isdigit():
                    if int(your_age) > 20:
                        print("Welcome ",your_name,"Sir,as your age is",your_age,"years,so you are eligible for Pyhton fundamental course...\m")
                    else:
                        print("Oops Sorry", your_name, "Sir,as your age is", your_age,"years,so you are not eligible for Pyhton fundamental course...\m")
                else:
                    print("Sorry you have entered wrong input,So please enter your age correctly containing only numerical value")

            else:
                print("Sorry you have entered wrong name,So please enter a valid name containing only characters")

        elif gen=="f" or gen=="female":
            print("Hello Mam,I'm Khushiram from Acadview ")
            your_name=input("Can you tell me your name\n")

            if your_name.isalpha():
                print("Hello Mam,Your Good Name is", your_name)
                print("I would like to collect some more information about you\n")
                your_age = input("Please tell me your age")

                if your_age.isdigit():
                    if int(your_age)>19:
                        print("Welcome ", your_name,"Mam,as your age is", your_age,"years,so you are eligible for Pyhton fundamental course...\m")
                    else:
                        print("Oops Sorry", your_name, "Mam,as your age is", your_age,"years,so you are not eligible for Pyhton fundamental course...\m")
                else:
                    print("Sorry you have entered wrong input,So please enter your age correctly")

            else:
                 print("Sorry you have entered wrong name,So please enter a valid name containing only characters")

        else:
                    print("Sorry,this is not a valid input,so please enter your gender correctly\n")
                    gender()
    else:
        print("Sorry check your input and enter only characters in your gender")
        gender()

gender()
