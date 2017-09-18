# importing spy details and start chat
from spy_details import spy
from start_chat import  start_chat

#Importing termcolor to get output colorful
from termcolor import colored

#Start greeting
print (colored("\n Hello!, brother.","blue"))
print "Let's get started!\n"

#Ask the spy to continue as default spy  or create new spy
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N): "
existing = raw_input(colored(question,"red"))

# validating input
if (existing.upper() == "Y") :
    spy_name = spy.salutation + " " + spy.name

    start_chat(spy.name, spy.age, spy.rating, spy.is_online)
elif (existing.upper() == "N"):
    spy.name = raw_input("What  your name :")
    if len(spy.name) > 0:
        spy.salutation = raw_input("What should we call you ? : ")


        while True:
            try:
                spy.age = int(raw_input("Enter your age: "))
                break
            except ValueError:
                print "Invalid age. Try again"
        spy.name = spy.salutation + " " + spy.name

        spy.rating = float(raw_input("What is your spy rating?"))
        spy.is_online = True

        start_chat(spy.name, spy.age, spy.rating, spy.is_online)
    else:
        print "Invalid name. Try again."
else:
    print "Wrong choice. Try again."