from select_friend import select_friend
from spy_details import friends

#importing termcolor for colorful output.
from termcolor import colored

def read_chat_history():
    read_chat = select_friend()

    print '\n'

    for chat in friends[read_chat].chats:
        if (chat.sent_by_me != False) :
            print (colored(str(chat.time.strftime("%d %B %Y %A %H:%M"))+ ", ", 'yellow')),
            print (colored("You said: ", 'red')),
            print str(chat.message)
        else:
            print (colored(str(chat.time.strftime("%d %B %Y %A %H:%M"))+ ", ", 'yellow')),
            print (colored(str(friends[read_chat].name)+"You said: ", 'red')),
            print str(chat.message)