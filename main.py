# Project: Hooked on Coding

## Algorithm ##
# Goal is to be able to capture keyboard and mouse inputs to be used in conjuction with trouble ticket submission.
# Allowing user to attach exact keypresses leading up to a issue. User will be asked questions during submission of ticket.
# These questions include what they were attempting to accomplish and any other information they feel is pertinent to ticket.
# So starting off a process will be running continiously in order to catch all user inputs. A "trigger" key will be used by user to capture last inputs.
# "Trigger" should be used when user runs into a issue. This will cause the last inputs to be saved to another file to be used.
# After error occurs user will submit ticket which will ask for user's name, error encountered, what they wanted done.
# If they have more than one ticket needing submitted they will be asked before leaving ticket creation.

# Using the keyboard library to capture keyboard events.
from functions import * # pull all functions from my functions file
import keyboard # This is the keyboard library that will allow me to record all keyboard events that user has


global keypress_list # Making keypress_list a global variable.
# Needs to be a global variable to be used in the recording function.


welcome_banner() # Calls the function that has a intro to user.

tech_first_name = input("What is your first name?: ") # Get the user's first name
tech_last_name = input("What is your last name?: ") # Get the user's last name
print("Thank you " + tech_first_name + " " + tech_last_name + " for logging in. ") # Reiterate user's name to user
print("If you want to start recording please press the escape key. ") # prompts user to start recording with below function
keyboard.wait("esc") # forces user to press escape key
print("Recording activated. Please continue your work. \nIf you have any issues please press the escape key to submit ticket. ")
print("Please do not input any login info to other programs while this is running. ") # disclaimer to safeguard user login info
# Lets user know the recording is activated.
keypress_list = keyboard.record(until="esc") # this function start recording until escape is pressed again.
# program is halted here until that second escape key input is made
print("Recording stopped. ") # Let user know the recording is stopped


error_encountered = trigger_activated() # make returned value from trigger function into error variable

if error_encountered == "N": # User provided a "no" in needing a ticket made
    print("We see you don't need to make a ticket. Please refrain from using trigger for ticket if no problem is detected. ")
elif error_encountered == "5": # User hit limit of bad input
    print("You have exceeded the maximum allowed attempts to start ticket. Session will be terminated. ")
elif error_encountered == "Y": # User does want to submit ticket
    print("Lets get some information from you. ")
    # Which department is user working in
    user_dept = input(tech_first_name + " " + tech_last_name + " which department do you work in?: ")
    # State what the user was intending to do
    user_intentions = input("What were you intending to accomplish before running into error?: ")
    # What error happened
    users_error = input("What was the error that occured? Please provide a error code if able: ")
    with open('user_info.txt', 'w') as file: # Writes file into the user_info.txt file.
        # Current implementation overwrites all prior entries so only one time use.
        file.write(tech_first_name + "\n" + tech_last_name + "\n" + user_intentions + "\n" + users_error + "\n\n")
        for i in keypress_list: # Writes all keyboard inputs recorded into the file as well
            file.write(str(i) + "\n") # Separates each input with a new line.

