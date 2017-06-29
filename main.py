# importing from another file spy details some attributes

from spydetails import spy, Spy, ChatMsg, friends

# for installing module...steganography in terminal do pip install steganography
# import steganography as written

from steganography.steganography import Steganography
# for Timestamp
from datetime import datetime

# printing the status messages which can be updated

STATUS_MESSAGES = ['Welcome to SpyChat', 'Keeping every detail Secret', 'Provide best security']
# printing hello

print "Hello! Let\'s get started"  # we have make use of \ which take whole program in '' We can also make use of ""

# Asking if he/she wants to continue as the provided names and salutations
question = "Do you want to continue as " + spy.salu + " " + spy.name + " (Y/N)? "
existing = raw_input(question)


# Adding new status or updating
def add_status():
    updated_status_msg = None

    if spy.current_status_msg != None:

        print 'Your current status message is %s \n' % spy.current_status_msg
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_msg = raw_input("What status message do you want to set? ")

        if len(new_status_msg) > 0:
            STATUS_MESSAGES.append(new_status_msg)
            updated_status_msg = new_status_msg

    elif default.upper() == 'Y':

        item_position = 1

        for msg in STATUS_MESSAGES:
            print '%d. %s' % (item_position, msg)
            item_position = item_position + 1

        msg_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= msg_selection:
            updated_status_msg = STATUS_MESSAGES[msg_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_msg:
        print 'Your updated status message is: %s' % (updated_status_msg)
    else:
        print 'You current don\'t have a status update'

    return updated_status_msg

#Adding a friend
def add_friend():
    new_friend = Spy('', '', 0, 0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salu = raw_input("Add Salutation Mr. or Ms.?: ")

    new_friend.name = new_friend.salu + " " + new_friend.name

    new_friend.age = raw_input("Friend's Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("His Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Congratulations!!!, Friend Added!'
    else:
        print 'Sorry! Sorry your entry is Invalid. We can\'t add spy with the details you provided'

    return len(friends)


# selecting a friend...checking its status

def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salu, friend.name,
                                                                friend.age,
                                                                friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


# Sending a secret message

def send_msg():
    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")

    # image file where encoding take place

    output_path = "Koala.jpg"
    text = raw_input("What do you want to say? ")
    # Encode is a function of steganography
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMsg(text, True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


# Reading a Secret message

def read_msg():
    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)  # decode is another function of steganography

    new_chat = ChatMsg(secret_text, False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"


# Reading History of chats if any saved earlier..

def read_chat_history():
    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:

            # we will make use of strftime which is an fuction of datetime.datetime object
            # it converts the input time to a string format

            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.msg)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.msg)


# Starting the chat...by autheticating and using conditions

def start_chat(spy):
    spy.name = spy.salu + " " + spy.name

    # Checking if the spy is in correct age criteria

    if spy.age > 12 and spy.age < 50:

        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True
        # setting up a menu by providing choices to the spy what he wants to do

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)
            #
            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_msg = add_status()
                elif menu_choice == 2:
                    no_of_friends = add_friend()
                    print 'You have %d friends' % no_of_friends
                elif menu_choice == 3:
                    send_msg()
                elif menu_choice == 4:
                    read_msg()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'


if existing == "Y":
    start_chat(spy)

else:

    spy = Spy('', '', 0, 0.0)

    # Asking the Details of the spy..

    spy.name = raw_input("Hi There Welcome to spy chat, tell us your spy name first: ")

    if len(spy.name) > 0:
        spy.salu = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please add a valid spy name'
