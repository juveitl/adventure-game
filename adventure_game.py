import time
import random

list = ["wicked fairy", "pirate", "troll"]
items = []


def print_pause(message):
    print(message)
    time.sleep(2)


def house(figure):
    print_pause("You approach the door of the house."
                " You are about to knock when the door opens and out steps a "
                + figure + "."
                " Eep! This is the " + figure + "'s house!"
                " The " + figure + " attacks you!")
    if "sword" in items:
        print_pause("As the " + figure +
                    " moves to attack, you unsheath your new sword."
                    " But the " + figure +
                    " takes one look at your shiny new toy and runs away!"
                    " You have rid the town of the " + figure +
                    ". You are victorious!")

    elif "sword" not in items:

        print_pause(" You feel a bit under-prepared for this,"
                    "what with only having a tiny dagger.")
        choice_fight = input("Would you like to (1) fight or (2) run away?")
        if choice_fight == "1":
            print_pause("You do your best..."
                        " but your dagger is no match for the " + figure + "."
                        " You have been defeated!")

            play_again = input("Would you like to play again? (y/n)")
            if play_again == "y":
                print_pause("Excellent! Restarting the game ...")
                field()
            elif play_again == "n":
                print_pause("Thanks for playing! See you next time.")

            else:
                print_pause("Please enter y or n.")
        elif choice_fight == "2":
            print("You run back into the field. Luckily,"
                  " you don't seem to have been followed.")
            field()


def cave():
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now."
                    " You walk back out to the field.")
        field()

    elif "sword" not in items:
        print_pause("It turns out to be only a very small cave."
                    " Your eye catches a glint of metal behind a rock."
                    " You have found the magical Sword of Ogoroth!"
                    " You discard your silly old dagger"
                    "and take the sword with you."
                    " You walk back out to the field.")
        items.append("sword")
        field()


def intro():
    print_pause("You find yourself in a dark dungeon.")

    print_pause("In front of you are two passageways.")

    print_pause("To your right is a dark cave.")

    print_pause("In front of you is a house.")

    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger.")


def field():
    figure = random.choice(list)
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")

    choice = input("What would you like to do?\n(Please enter 1 or 2.)\n")

    if choice == "1":
        house(figure)

    elif choice == "2":
        cave()

    else:
        print("Please enter 1 or 2.")
        field()


intro()
field()
