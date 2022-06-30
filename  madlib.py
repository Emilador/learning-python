import random

def no_verarsche(wort):
    while not wort.isalpha():
        wort=input("This is not a correct Verb. Please be serious this time: ")
    return wort
def matlib1():
    verb1 = input("Verb: ")
    verb1 = no_verarsche(verb1)
    verb2 = input("Verb: ")
    verb2 = no_verarsche(verb2)
    verb3 = input("Verb: ")
    verb3 = no_verarsche(verb3)
    adjkt1 = input("Adjektiv: ")
    adjkt1 = no_verarsche(adjkt1)
    print(f"Rafa is really good in {verb1}ing but really bad in {verb2}ing. Emil however is {adjkt1} and likes to {verb3}. ")

def matlib2():
    verb1 = input("Verb: ")
    verb1 = no_verarsche(verb1)
    verb2 = input("Verb: ")
    verb2 = no_verarsche(verb2)
    verb3 = input("Verb: ")
    verb3 = no_verarsche(verb3)
    adjkt1 = input("Adjektiv: ")
    adjkt1 = no_verarsche(adjkt1)
    print("")
def matlib3():
    verb1 = input("Verb: ")
    verb1 = no_verarsche(verb1)
    verb2 = input("Verb: ")
    verb2 = no_verarsche(verb2)
    verb3 = input("Verb: ")
    verb3 = no_verarsche(verb3)
    adjkt1 = input("Adjektiv: ")
    adjkt1 = no_verarsche(adjkt1)
while True:
    madlibs=[1,2,3]
    madlib_choice=random.choice(madlibs)
    if (madlib_choice==1):
        matlib1()
    elif (madlib_choice==2):
        matlib2()
    elif (madlib_choice==3):
        matlib3()

    again=input("You wan´t to play again?  [yes/no]")
    while ((again!="yes" and again!="no")):
        print("Please enter [yes/no]")

    if again


