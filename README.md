# STEM103_Final_Project  
# By Kaleb Palilla  
This is my first project involving Python and has me using everything I learned up until now and add something new.  
I chose to use the keyboard library as my something new and will be using two functions from it.  
This includes keyboard.record and keyboard.wait which allows the recording of all keyboard inputs  
and allow them to be saved into a global variable. Meanwhile keyboard.wait is necessary as it halts the program until  
user provides the trigger for recording.  

# Hooked on Coding  
This project is using the keyboard library in order to record all keyboard events happening in or out of the program.  
The idea is that a user would have this running while doing other tasks and then could use a trigger,  
in this case the 'escape' key, in order to start/stop recording and submit user information for a trouble ticket.  
The project simulates a working enviroment as kinda shown with a welcome screen but shows that this program could be  
used with other systems and user can come back to make the ticket.  
So the 'escape' key causes both the recording and ticket generator due to the tied intended function.  
The trigger functions goal is to filter out bad data while handling the user if they say 'yes' or 'no' in wanting a ticket.  
If 'no' or user hits the limit of 5 then process stops. If user says 'yes' then they are asked clarifying information for ticket.  
This includes what department they work in, what they expected to happen before running into issue, and a error code if able.  
All this information gets written into a text file so another technician could look at it and use it in their troubleshooting.  

# How I tested if this works  
While running this code I tried giving bad data during the ticket submission and was successfully handled in the way I wanted.  
Due to the complexity I don't have the same handling on the latter portion for example: which department the user works in  
but could come back and make changes in the future.  
I also verified it was capturing the data I wanted as I have the data put into a text file and can visually verify.

# What I learned  
I learned how to use the prior knowledge I gained in order to make my own thing.  Also after much headache learned how to use  
a library someone else created by going through their readme file and looking at their functions itself to see how it works.  

# What issues I came across  
I initially was going to use different functions from the keyboard library in order to record start and stop but found that  
keyboard.record did exactly what I wanted which simplified what I needed to add. Other issues I came across was my  
trigger_activated function was not working as intended and wasn't catching correct inputs. I found it was due to me using != so  
my boolean operators of 'or' needed to be 'and'. Also ran into a issue of getting keyboard.record to work and found I wasn't  
calling it correctly as it needed a key to be listed to work and a global variable to save to. I wouldn't have figured that  
out if not for looking into the library itself to look at the code and try to make sense of it.  