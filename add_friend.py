# importing spy and existing friends
from spy_details import Spy, friends
# importing regular expressions for proper validation
import re

# importing termcolor for colorful output
from termcolor import colored

# function to add new friends.
def add_friend():
    new_friend = Spy(" ", " ", 0, 0.0)

    # ask user for name and salutation of friend
    new_friend.name = raw_input("Please add your friend's name: ")
    pattern_n = '^[a-zA-Z\s]+s'

    new_friend.salutation= raw_input("What to call Mr. or Ms.?: ")
    pattern_s = '^[a-zA-Z\s]+s'

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = int(raw_input("Age? "))
    pattern_a = '^[0-9]+$'

    new_friend.rating = float(raw_input("Spy rating? "))
    pattern_r = '^[0-9]+\.[0-9]+$'

    if len(new_friend.name) > 0 and new_friend.name.isdigit() == False and re.match(pattern_n,new_friend.name)!=None and re.match(pattern_s,new_friend.salutation)!=None and new_friend.age > 12 and new_friend.rating < 50 and re.match(pattern_a,new_friend.age)!=None and new_friend.salutation.isalpha() ==  True and new_friend.rating >= 0 and re.match(pattern_r,new_friend.rating)!=None:

        friends.append(new_friend)
        print (colored('Friend Added!', 'magenta'))
    else:
        print (colored('Sorry! Invalid entry. We can\'t add spy with the details you provided\n ', 'blue'))
    print (colored('The convention to follow is: \n ', 'blue'))
    print (colored('1. Name can be alphabets only.\n ', 'blue'))
    print (colored('2. Age can be digits only.\n ', 'blue'))
    print (colored('3. Do not use (.) after salutation, it can be alphabets only too.\n ', 'blue'))
    print (colored('Keep in mind and Try Again\n\n ', 'blue'))

    return len(friends)