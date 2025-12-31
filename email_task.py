import sys
inbox = []   


# Class for the email
class Email():

    has_been_read = False

    def __init__(self, email_address, Subject_line, email_content):

        self.email_address = email_address
        self.Subject_line = Subject_line
        self.email_content = email_content


# Sample mails for the class
def populate_inbox():
    global inbox

    # Create 3 sample emails and add them to the inbox list.
    thabo = Email("thabo@gmail.com", "Business", "Cars")
    tumisang = Email("tumisangrancho@gmail.com", "Programming", "Python")
    portia = Email("portiamphagi@gmail.com", "Investigation", "Anglo")
    # The list of emails are placed inside a list
    inbox = [thabo, tumisang, portia]


# Function for the user wants to generate a list of all emails
def list_emails(inbox):

    for index, Email in enumerate(inbox):
        print(index, Email.Subject_line)


# Function for the user to read emails that are selected
def read_email():
    populate_inbox()

    user = int(input("Hi! to open emails for :\n\
    1. thabo\n\
    2. tumisang\n\
    3. portia\n\
    Select a value between '1' , '2' or '3':\n"))

    # if function to check which integer is selected
    if 1 <= user <= 3:
        index = user - 1 
        email = inbox[index]
        email.has_been_read = True
        print(f"Selected email:\n\
             {email.Subject_line}\n\
             Content:\n\
             {email.email_content}\n\
             from:\n\
             Email address:\n\
             {email.email_address}")

    else:
        # if wrong input is given by the user
        print("Wrong value selected")       


# Function for the user to view unread emails
def view_unread_emails():

    populate_inbox()

    # Loop function to check whether all the messages are read
    for index, email in enumerate(inbox):
        if email.has_been_read:
            print(f"{index} {email.Subject_line} marked as read")
        else:
            print("No message has been read")
            sys.exit()


# while to check what output those the user want
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        ))

    # If function to check what input did the user insert
    if user_choice == 1:
        read_email()

    elif user_choice == 2:
        view_unread_emails()

    elif user_choice == 3:
        sys.exit()

    else:
        print("Oops - incorrect input.")