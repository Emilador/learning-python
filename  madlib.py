import random
adjkt1=input("Adjektiv: ")
adjkt2=input("Adjektiv: ")
verb1=input("Verb: ")
madlibs=[f"Rafas balkon is so {adjkt1} and also really {adjkt2}. Actually my uncle Rafa is {verb1} on his balkon right now."
         ,f"My nephew Emil is better than me in {verb1}ing"]



madlib=random.choice(madlibs)
print(madlib)