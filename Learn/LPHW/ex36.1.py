from sys import exit
import random


def hotel():
    print("Welcome to the Dogan Hotel!")
    exit(0)

def disco():
    print("Welcome to the Dogan Disco!")
    exit(0)

def restaurant():
    print("Welcome to the Dogan Restaurant!")
    print("You've sit a nice table next to window")
    print("Waiter: What would you like to order sir?\n")
    print("Menu.....")
    print("Soups")
    print("""* 1. Tomato soup
    * 2. Chicken soup
    * 3. Mercimek soup
    """)
    soup_selection = input("> ")

    print("\nMain course")
    print("""* 1. Adana kebab
    * 2. Kofte - Piyaz
    * 3. Kuzu Pirzola
    """)
    main_course_selection = input("> ")

    print("You have chosen {} and {}".format(soup_selection, main_course_selection))

    exit(0)

def what_to_do():
    print("Now thinking what to do...")
    print("There are several options")
    print("* 1. Go to hotel\n* 2. Go to disco\n* 3. Go to a nice restaurant")
    choose_what_to_do = int(input("> ")) # input() function always gives string therefore we convert them where necessary
    if choose_what_to_do == 1:
        hotel()
    elif choose_what_to_do == 2:
        disco()
    elif choose_what_to_do == 3:
        restaurant()
    else:
        print("None is chosen!")
        print("Learn how to type number")
        print("..........GAME OVER..........")
        exit(0)





def leave_casino(money):
    current_money = money
    print("Congrats..")
    print("You've made enough money for today")
    print(f"You have {current_money} bucks")
    print("Leaving the casino....\n")

    what_to_do()

# Poker game
def poker():
    print("Welcome to the poker table")
    print("Table is not set up yet")
    print("Going to play roulette\n")
    roulette()

# Roulette game
def roulette():
    print("Welcome to the roulette table")
    print("Rules...!")
    print("You need to choose the correct color; black or red")
    print("There is no limit on minumum amount of bet")
    print("If you know the color you will get double of your bet if not you will loose the amount of money you bet")
    print("I.e. if you put $20 and know color you will get $40")
    print('You aim is to make minumum 1000 bucks or more. You can\'t get out of Casino untill you make it')

    print("\nRoulette cark is turning.....")
    print("Make your bet!")
    initial_money = 50
    possibilities = ["black", "red"]

    while True:
        print("\nBet amount")
        bet_amount = abs(int(input("> "))) # absolut value taken in the case user puts negative value

        print("Selection of color")
        selection = input("> ")

        if initial_money >= bet_amount and initial_money > 0:
            if selection == possibilities[random.randint(0,1)]:
                print("You won!")
                initial_money += bet_amount
                print("Your have $", initial_money)
                if initial_money >= 1000:
                    leave_casino(initial_money)
            else:
                initial_money -= bet_amount
                print("You lost!")
                print("Your have $", initial_money)
                if initial_money <= 0:
                    print("\nYou've lost all your money.")
                    print("Get the out of here.")
                    print("..........GAME OVER..........")
                    exit(0)
        elif initial_money < bet_amount and initial_money > 0:
            print("Maximum amount you can bet is: {}".format(initial_money))
        else:
            print("You've lost all your money.")
            print("Get the out of here.")
            print("..........GAME OVER..........")
            exit(0)


def game_selection():
    print("Congrats, you are now able to play casino games with your 50 bucks")
    print("Select which game you would like to play")
    print("""Options:
    * 1 for Poker
    * 2 for Roulette
    """)
    selection = int(input("> "))
    if selection == 1:
        poker()
    elif selection == 2:
        roulette()
    else:
        print("Learn how to write numbers!")
        print("..........GAME OVER..........")
        exit(0)


def card_drops():
    print("""You are approaching to the front door of the Casino and wonder how to enter with your super nice smell! :)
    There is one guy who came by limousine also walks in front of you. You saw that the guy has dropped a card from his pocket!
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
            game_selection()
        else:
            print("Show your card next time!")
            print("..........GAME OVER..........")
            exit(0)

    elif "don't" in take_card or "dont" in take_card:
        print("You did not take the card!")
        print("You now approached the bodyguards and would like to enter")
        print("Bodyguards: You smell very bad man, you can't enter")
        print("Now say something smart so that bodyguards will allow you to enter")
        show_card = input("> ")
        print("Bodyguards: Get the out of here man. You don't have a card.")
        print("Take the card next time.")
        print("..........GAME OVER..........")
        exit(0)
    else:
        print("You weren't able to neither grab the card nor walk away.")
        print("..........GAME OVER..........")
        print("Hahahahah")
        exit(0)


def public_bus():
    print("""You stepped in and paid 2 bucks.
    Buss finally arrived (after 2 hours) to the Casino and you get off the buss with a bad smell passed to you from homeless guy.
    What a wonderful day!!! :)
    """)
    card_drops()


def start():
    print("......................")
    print("Welcome to Casino Royal...")
    print("Money talks!")
    print("......................")

    print("November 13, 2018,", end = '   ')
    print("North Cyprus Turkish Republic\n")


    print("Your aim is to go to the casino, enter and make minumum 1000 bucks")

    print("""You have 52 bucks in your pocket and standing on the corner
    and waiting for publicbus to go to Kaya Artemis Casino. Bus approaches to you and stops 35 meters away from you.
    """)

    print("Run to catch the buss or wait another one")

    decision = input("> ")

    if "run" in decision or "Run" in decision:
        print("Good run. You cathed the bus")
        public_bus()
    elif "wait" in decision or "Wait" in decision:
        print("Lazy man!, next bus comes after one hour. Get the out of here!")
        print("..........GAME OVER..........")
        exit(0)
    else:
        print("Write words correct man. Don't waste my time.")
        exit(0)


start()
