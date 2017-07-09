#importing datetime for timestamp
from datetime import datetime

#class spy where all the attributes are present
class Spy:
    def __init__(self, name, salu, age, rating):
        self.name = name
        self.salu = salu
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMsg:
    # Dictionary for the chat
    def __init__(self, msg, sent_by_me):
        self.msg = msg
        self.time = datetime.now()  # Created a timestamp by using datetime module
        # now function return current date  and time

        self.sent_by_me = sent_by_me


spy = Spy('bond', 'Mr.', 24, 4.7)
#these are our friends..
friend_first = Spy('Naman', 'Mr.', 4.5, 21)
friend_second = Spy('Rajat', 'Mr.', 4.33, 24)
friend_third = Spy('Ekta', 'Dr.', 4.80, 28)

friends = [friend_first, friend_second, friend_third]
