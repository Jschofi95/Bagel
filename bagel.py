import random

max_tries = 10

def print_intro():
    print("Bagels, a deductive logic game.")
    print("By Al Sweigart al@inventwithpython.com")
    print("Coded by Aaron Schofield.\n")


def print_rules():
    print("When I say:\t\t\tThat means:")
    print("Pico\t\t\tOne digit is correct but in the wrong position.")
    print("Fermi\t\t\tOne digit is correct and in the right position.")
    print("Bagels\t\t\tNo digit is correct.")


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
            return 'Bagels' # There are no correct digits at all.
    else:
            # Sort the clues into alphabetical order so their original order
            # doesn't give information away.
        clues.sort()
            # Make a single string from the list of string clues.
        return ' '.join(clues)


def main():
    print_intro()

    while(1):
        print_rules()
        won = False
        random_num = str(random.randrange(100, 999))
        print("I have thought up a number.")
        print("You have {} guesses to get it.".format(max_tries))

        for i in range(1, max_tries + 1):
            print("Guess #{}: ".format(i))
            guess = input()

            # Prompts the user to enter another guess if their guess is not 3 digits
            while len(guess) != 3 or guess.isdigit() == False:
                print("Guess must be 3 digits and have only numbers. Try again!")
                print("Guess #{}: ".format(i))
                guess = input()

            result = getClues(guess, random_num)

            if result == "You got it!":
                won = True
                print(result)
                break
            else:
                print(result)

        if won == False:
            print("Sorry! The number was {}".format(random_num))
        choice = input("Try again? y/n: ".lower())
        if choice == 'n':
            break

    print("Goodbye")

if __name__ == "__main__":
    main()
