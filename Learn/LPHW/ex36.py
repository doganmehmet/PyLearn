# Designing and Debugging

from sys import exit
import random

print("......................")
print("Welcome to Casino Royal...")
print("Money talks!")
print("......................")

print("November 13, 2018,", end = '   ')
print("North Cyprus Turkish Republic")

print("""You have 52 bucks in your pocket and standing on the corner
and waiting for publicbus to go to Kaya Artemis Casino. Bus approaches to you and stops 35 meters away from you.
""")

print("Run to catch the buss or wait another one")


# defining a function which is responsible for taking user to the bus and leaves in Artemis hotel
def public_bus():
    print("""You stepped in and paid 2 bucks.
    Buss finally arrived (after 2 hours) to the Casino and you get off the buss with a bad smell passed to you from homeless guy.
    What a wonderful day!!! :)
    """)

def card_drops():
    print("""You are approaching to the front door of the Casino and wonder how to enter with your super nice smell! :)
    There is one guy who came by limousine also walks in front of you.You saw that the guy has dropped a card from his pocket!
    You quickly approached the card and saw that it is a loyal member card which only 10 people have.
    """)
    print("Take the card or don't")
    take_card = input("> ")
    if "take" in take_card or "Take" in take_card:
        print("You took the card")
        print("You now approached the bodyguards and would like to enter")
        print("Bodyguards: You smell very bad man, you can't enter")
        print("Now say something smart so that bodyguards will allow you to enter")
        show_card = input("> ")
        if "have card" in show_card or "have member card" in show_card or "show" in show_card:
            print("Showing the card....")
            print("Bodyguards: Apologize sir. Welcome please.")
            print("You now entered to the casino.")
        else:
            print("Show your card next time!")
            print("You have FAILED!!!")
            exit(0)

    elif "don't" in take_card or "dont" in take_card:
        print("You did not take the card!")
        print("You now approached the bodyguards and would like to enter")
        print("Bodyguards: You smell very bad man, you can't enter")
        print("Now say something smart so that bodyguards will allow you to enter")
        show_card = input("> ")
        print("Bodyguards: Get the out of here man. You don't have a card.")
        print("FAILED!!!")
        print("Take the card next time.")
        exit(0)
    else:
        print("You weren't able to neither grab the card nor walk away.")
        print("FAILED!!!")
        print("Hahahahah")

# Poker game
def poker():
    print("Welcome to the poker table")
# Roulette game
def roulette():
    print("Welcome to the roulette table")
    print("Rules for game: There is only two color; black and red")
    print("The minumum amount is $10 for each try")
    print("If you know the color you will get double of your bet if not you will loose the amount of money you bet")
    print("I.e. if you put $20 and know color you will get $40 ")

    print("Poker cark is turning.....")
    print("Make your bet!")
    initial_money = 50
    possibilities = ["black", "red"]

    while True:
        print("Bet amount")
        bet_amount = abs(int(input("> "))) # absolut value taken in the case user puts negative value

        print("Selection of color")
        selection = input("> ")

        if initial_money >= bet_amount and initial_money > 0:
            if selection == possibilities[random.randint(0,1)]:
                print("You won!")
                initial_money += bet_amount
                print("Your have $", initial_money)
            else:
                initial_money -= bet_amount
                print("You lost!")
                print("Your have $", initial_money)
                if initial_money <= 0:
                    print("You've lost all your money.")
                    print("Get the out of here.")
                    print("FAILED")
                    exit(0)
        elif initial_money < bet_amount and initial_money > 0:
            print("Maximum amount you can bet is: {}".format(initial_money))
        else:
            print("You've lost your money.")
            print("Get the out of here.")
            exit(0)



def game_selection():
    print("Congrats, you are now able to play casino games")
    print("Select which game you would like to play")
    print("""* Write 1 for Poker
    * 2 for Roulette
    """)
    selection = int(input("> "))
    if selection == 1:
        poker()
    elif selection == 2:
        roulette()
    else:
        print("Learn how to write numbers!")
        print("FAILED!!!")
        exit(0)

def test():
    print("Aha simdi ciktim!")
    exit(0)


while True:
    decision = input("> ")

    if "run" in decision or "Run" in decision:
        print("Good run. You cathed the bus")
        public_bus()
        card_drops()
        game_selection()
        test()
    elif "wait" in decision or "Wait" in decision:
        print("Lazy man!, next bus comes after one hour. Get the out of here!")
        print("FAILED!!!")
        exit(0)
    else:
        print("Write correct man. Don't waste my time.")
