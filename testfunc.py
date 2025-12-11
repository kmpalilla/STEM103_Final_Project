# Functions for main.py

# This will include functions for keyboard library and parts of the user ticket process in order to modularize my code.


def welcome_banner():
    print("Welcome to Hooked on Coding Industries. ")
    print("Be advised all keyboard inputs are subject to be recorded on this system. ") # disclaimer while keyboard library is active.
    print("To log in please provide your first and last name. ")




def trigger_activated():
    start_ticket_failure = 1
    start_ticket_limit = 5
    print("We see you activated the error trigger. ") # Check if trigger was used correctly
    need_ticket.upper() = input("Do you want to sumbit a ticket? Y for yes N for no: ")
    while need_ticket != "Y":
        if need_ticket == "N":
            print("We see you don't need to make a ticket. Please refrain from using trigger for ticket if no problem is detected. ")
            exit(0)
        else:
            print("Wrong input given. ")
        start_ticket_failure += 1
        need_ticket = input("Please provide Y or N depending on your need. ")
        if start_ticket_failure == start_ticket_limit:
            print("You have exceeded the maximum allowed attempts to start ticket. Session will be terminated. ")
            exit(0)
    else: 
        print("Lets get some information from you. ")