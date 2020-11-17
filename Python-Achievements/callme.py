import sys
import time

def callMe(name, number):
    print("&: Hello?")
    time.sleep(1)
    print("&: who's there?")
    time.sleep(1)
    print("#: I'am sorry, you are speaking with "+ name)
    time.sleep(1)
    print("&: Hey "+ name+ " How are you?")
    time.sleep(1)
    print("#: I'am pretty good how are you?")
    time.sleep(1)
    print("&: Good to hear mate, I'am pretty good aswel")
    time.sleep(1)
    print("&: But is it okay if i call you back later have to go back to work")
    time.sleep(1)
    print("#: Nice good to hear, btw i have a new phonenumber "+ number)
    time.sleep(1)
    print("#: Sure, Have a great day at work")
    time.sleep(1)
    print("&: Thanks mate! Good to know. Cya mate!")
    time.sleep(1)
    print("#: Later mate!")
    time.sleep(1)
    print("click....")

callMe(sys.argv[1], sys.argv[2])
    
