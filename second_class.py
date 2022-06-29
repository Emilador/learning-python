codewort = "haha"

while True:
    user_input = input("Gib bitte das Codewort ein dass es endlich aufhört: ")
    print("Deine Eingabe war: ", user_input)
    if (user_input==codewort) :
        print("Richtig gemacht.\n Dankeschön")
        break
    else:
        print("Flasches Passwort")
