import resources
import os

def main():
    play = True

    while play:
        os.system('cls')
        print(resources.treasure_chest)
        print("Welcome to Treasure Island.")
        print("Your mission is to find the treasure.")

        if (input("(l)eft or (r)ight?")).lower() != 'l':
            print("You fell into a hole.  And died.")
        elif (input("(s)wim or (w)ait?")).lower() != 'w':
            print("Attacked by a herring.  That killed you.")
        else:
            door = input("Which door: (r)ed, (y)ellow or (b)lue?").lower()
            if door == 'r':
                print("You were burned by fire.  Nasty way to go.")
            elif door == 'b':
                print("You were eaten by beasts.  One bite at a time.  And died screaming.")
            elif door == 'y':
                print("You win!")
            else:
                print("Game over.")

        if input("Play again? y/n").lower() != 'y':
            play = False

main()