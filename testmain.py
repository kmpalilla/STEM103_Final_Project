# Project: Hooked on Coding
from functions import * # pull all functions from my functions file
import keyboard
# Goal is to be able to capture keyboard and mouse inputs to be used in conjuction with trouble ticket submission.
# Allowing user to attach exact keypresses leading up to a issue. User will be asked questions during submission of ticket.
# These questions include what they were attempting to accomplish and any other information they feel is pertinent to ticket.
# So starting off a process will be running continiously in order to catch all user inputs. A "trigger" key will be used by user to capture last inputs.
# "Trigger" should be used when user runs into a issue. This will cause the last inputs to be saved to another file to be used.
# After error occurs user will submit ticket which will ask for user's name, error encountered, what they wanted done.
# If they have more than one ticket needing submitted they will be asked before leaving ticket creation.

# Using the keyboard library to capture keyboard events.

global keypress_list


welcome_banner()

tech_first_name = input("What is your first name?: ")
tech_last_name = input("What is your last name?: ")
print("Thank you " + tech_first_name + " " + tech_last_name + " for logging in. ")
print("If you want to start recording please press the escape key. ")
keyboard.wait("esc")
print("Recording activated. Please continue your work. \nIf you have any issues please press the escape key to submit ticket. ")
keypress_list = keyboard.record(until="esc")
print("Recording stopped. ")

# Trigger activated, stop logging keyboard. (file input/output)
trigger_activated()

# Which department is user working in
user_dept = input(tech_first_name + " " tech_last_name + " which department do you work in?: ")
# State what the user was intending to do
user_intentions = input("What were you intending to accomplish before running into error?: ")
# What error happened
users_error = input("What was the error that occured? Please provide a error code if able: ")

# Send ticket off (file input/output)


# Other ticket? (make function restart?)


# Resume logging keyboard




