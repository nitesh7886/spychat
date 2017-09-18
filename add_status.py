# importing spy details and default or/and older status
from spy_details import spy
from globals import STATUS_MESSAGES, current_status_message

# importing termcolor colorful output
from termcolor import colored

def add_status(current_status_message):
    updated_status_message = None

    if current_status_message != None:
        print 'Your current status message is %s \n' % (current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input(colored("Do you want to select from the older status (y/n)? ",'blue'))

    if default.upper() == "N":
        new_status_message = raw_input(colored("What status message do you want to set?: ",'blue'))

        # validating users input.
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
            print 'Your updated status message is: %s' % (updated_status_message)
        else:
            print "You did not provided any status message. Try again."

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input(colored("\nChoose from the Index of status: ",'cyan')))

        if len(STATUS_MESSAGES) >= message_selection:
            #updating
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
            print 'Your updated status message is: %s' % (updated_status_message)
        else:
            print "Invalid choice. Try again."
    else:
        print 'The option you chose is not valid! Press either y or n.'
    return updated_status_message