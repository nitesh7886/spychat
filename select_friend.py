# older friend
from spy_details import friends

#from globals import friends

# importing termcolor for colorful output
from termcolor import colored

def select_friend():

    counter = 1

    for friend in friends:
        print str(counter) + ". " + friend.name + "Age : " + str(friend.age)

        counter = counter + 1

    result = int(raw_input(colored("\nSelect from the list : ", 'magenta')))
    return result - 1