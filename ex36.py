# This is an adventure to be in Mamamoo Company
from time import sleep
from sys import exit


def Solar():
    print "You got a lesson from Solar. Your singing skills improved very much!"
    print "What would you do next?"
    print "Audition\nGet tutor from WheeIn"
    sleep(1)

# Should add a while statement here!!!!!!!!!!!!!!!!!!!!!!!!!!!
    choice = raw_input("> ")

    if choice == "Audition":
        CEO()
    elif choice == "Get tutor from WheeIn":
        WheeIn()

def WheeIn():
    print """You got a lesson from WheeIn. Your performance skills improved a lot!."""
    print "What would you like to do next?"
    print "Audition\nGet lessons from Solar"
    sleep(1)

# Here also should add a while statement!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    performance= raw_input("> ")

    if performance == "Audition":
        CEO()
    elif performance == "Get lessons from Solar":
        Solar()

def CEO():
    print "Welcome to Mamamoo Company's audition! I specifically have genres that I like, so I hope you can choose a good one!"
    print "Are you going to apply as singing or performing?"

    audition = raw_input("> ")

    if audition== "singing":
        singing()

    if audition == "performing":
        performing()

def singing():
    print "What genre are you going to sing?"
    print "Please sing the song."
    print "Options are\n-K-Pop\n-Pop\n-Jazz"

    songs = raw_input("> ")

    if songs == "K-Pop":
        print "I do not prefer that genre. I'm sorry even though you feel me as a Nazi."
        print "Hope you have a good day"
        exit(0)

    if songs == "Pop":
        print "Your singing was good. However, I think you should practice more as a trainee."
        print "We can support you for an year and you will become a singer."
        exit(0)

    if songs == "Jazz":
        print "You were amazing!!!"
        print "You will be a singer right away. Congratulations!"
        exit(0)

def performing():
    print "What are you going to perform?"
    print "Please show the performance."
    print "Options are\n-Break-dancing\n-Ballet\n-Poppin"

    perform = raw_input("> ")

    if perform == "Break-dancing":
        print "Excellent! I love your dance moves.\nYou can be a professional dancer right away."
        exit(0)

    if perform == "Ballet":
        print "I do not like your moves. I'm sorry but you are disqualified\nHope you have a good day."
        exit(0)

    if perform == "Poppin":
        print "Your dance moves were okay. However, I think you need some more practice as a trainee."
        print "We will support you from an year and you will become a professional dancer."

def start():
    print """You are an applicant to Mamamoo Company.
You have to get in by showing your skills of singing and performing.
Hope to see you in Mamamoo Company."""
    print "Which way will you go?"
    print "You can go straight or right."
    sleep(1)

    way = raw_input("> ")

    if way == "straight":
        Solar()
    elif way == "right":
        WheeIn()


start()
