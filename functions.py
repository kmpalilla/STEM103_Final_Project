# Functions for main.py

# This will include functions for keyboard library and parts of the user ticket process in order to modularize my code.


def welcome_banner(): # Just a quick welcome to company that user will first see
    print("Welcome to Hooked on Coding Industries. ") # Listing company name
    print("Be advised all keyboard inputs are subject to be recorded on this system. ") # disclaimer while keyboard library is active.
    print("Keyboard inputs will also be recorded outside this program. ") # Letting user know that ALL inputs are recorded
    print("To log in please provide your first and last name. ") # Prompts user to get their first and last name




def trigger_activated(): # This function runs if user stops the recording by pressing the escape the second time
    start_ticket_failure = 0 # assigns value 0 for start ticket failure if the user provides wrong input.
    start_ticket_limit = 5 # maximum allowed attempts by user if providing bad input
    print("We see you activated the error trigger. ") # Check if trigger was used correctly
    need_ticket = input("Do you want to sumbit a ticket? Y for yes N for no: ").upper() # ask user if they want to submit ticket
    # This also makes any lower case letter inputted to become uppercase to lower bad inputs possibility
    while (need_ticket != 'Y') and (need_ticket != 'N') and (need_ticket != "5"):
        # check if user provided Y , N , or hits limit of 5.
        print("Wrong input given. ") # tell user they gave the wrong input
        start_ticket_failure += 1 # increases counter by 1
        if start_ticket_failure == start_ticket_limit: # checks to see if failed attempts reach 5
            need_ticket = "5" # assign value of 5 to need_ticket variable
        else:
            need_ticket = input("Please provide Y or N depending on your need. ").upper()
            # re-prompt user for correct input
    return need_ticket # return the value of either Y , N, or 5 back to main for use