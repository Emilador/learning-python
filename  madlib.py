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

matlib1()