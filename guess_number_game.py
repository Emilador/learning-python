import random

print("Hello and welcome to my little game. The Computer will make up a number between 1 and a 100. \n Your goal is it to guess the number  \n ")
zahl=(random.randint(0,100))
tries=0


def reset_game():
    print("OK. Let´s go again")
    tries = 0
    zahl = (random.randint(0, 100))
    return zahl,tries
while True:
    if (tries>5):
        print("You used too many tries. You fucking suck man!")
        user_inputend = str(input("You wanna play again? [yes/no]\n  "))
        while (user_inputend!="yes")and( user_inputend!="no"):
            user_inputend=input("Please enter [yes/no]")
        if (user_inputend == "yes"):
            zahl,tries=reset_game()
        elif (user_inputend=="no"):
            print("OK. Hope you come back soon")
            break

    user_input = input("Please guess a number: ")
    try:
        user_input = float(user_input)
    except ValueError:
        print("That is not a number, you dumbass! Try again:")
        continue
    tries = tries + 1
    print("Your number of tries:" ,tries)
    if (user_input==zahl) :
        print("Wow! Very impressiv. \n")
        user_inputend = str(input("You wanna play again? [yes/no]\n  "))
        while ((user_inputend !="yes") and (user_inputend != "no")):
            print(user_inputend)
            user_inputend=input("Please enter [yes/no]")
        if (user_inputend=="yes") :
            zahl,tries=reset_game()
        elif (user_inputend=="no"):
            print("OK. Hope you come back soon")
            break
        else:
            print("Please say yes or no")
    elif (user_input<zahl) :
        print("Your number is a bit too small")

    elif (user_input>zahl) :
        print("Your number is a bit too big")




