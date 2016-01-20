# This is an adventure to be in Mamamoo Company
from time import sleep

def start():
    print """You are an applicant to Mamamoo Company.
You have to get in by showing your skills of singing and performing.
Hope to see you in Mamamoo Company."""
    print "Which way will you go?"
    print "1.Left\n2.Straight\n3.Right."
    sleep(1)

    choice = raw_input("> ")

    if choice == 1:
        restroom()
    elif choice == 2:
        Solar()
    elif choice == 3:
        WheeIn()
    else:
        print "Oh! Are you leaving? Hope to see you next time!"

def restroom():
    print "You can rest here and calm yourself first."
    print "Are you done resting?"
    print "Yes\nNo"
    sleep(1)

    choice = raw_input("> ")

    if choice == "Yes":
        start()
    elif choice == "No":
        restroom()
    else:
        print "You have slipped and got a stroke."

def Solar():
    print "You can get a tutor from Solar.\n You can improve your singing skills.\nHowever, if you do not want any tutor,\n you can audition right now or get a lesson from WheenIn for performance. "
    print "What would you like to do?"
    print "1.Get tutor by Solar\n2.Audition\n3.Get tutor from WheeIn"
    sleep(1)

# Should add a while statement here!!!!!!!!!!!!!!!!!!!!!!!!!!!
    choice = raw_input("> ")

    if choice == 1:
        print "Your singing skills got much better! Good luck on your audition!"
    elif choice == 2:
        CEO()
    elif choice == 3:
        WheeIn()

def WheeIn():
    print """You can get a lesson from WheeIn. You can improve your performance skills.
However, if you do not want any lessons,
you can audition in CEO's room right now or get a lesson from Solar to improve singing skills."""
    print "What would you like to do?"
    print "1.Get lessons from WheeIn\n2.Auditoin\n3.Get lessons from Solar"
    sleep(1)

# Here also should add a while statement!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    choice = raw_input("> ")

    if choice == 1:
        print "Your performing skills got much better! Good luck on your audition!"
    elif choice ==2:
        CEO()
    elif choice == 3:
        Solar()

def CEO():
    print "Welcome to Mamamoo Company's audition! I specifically have genres that I like, so I hope you can choose a good one!"
    print "Are you going to apply as singing or performing?"

    choice = raw_input("> ")

    if choice == "singing":
        singing()

    if choice == "performing":
        performing()

def singing():
    print "What genre are you going to sing?"
    print "Please sing the song."
    print "Options are\n-K-Pop\n-Pop\n-Jazz"

    choice = raw_input("> ")

    if choice == "K-Pop":
        print "I do not prefer that genre. I'm sorry even though you feel me as a Nazi."
        print "Hope you have a good day"
        exit.(0)

    if choice == "Pop":
        print "Your singing was good. However, I think you should practice more as a trainee."
        print "We can support you for an year and you will become a singer."

    if choice == "Jazz":
        print "You were amazing!!!"
        print "You will be a singer right away. Congratulations!"

def performing()
start()
