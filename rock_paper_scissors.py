import random
b="YOU WON"
pick=["rock","paper","scissors"]
win=["Damm it!","Sh*t!","F*ck!","Oh nooo!","This can`t be real!","Please tell me I´am dreaming! "]
draw=["OK that`s alright","As long as you don`t win","Don´t get arrogant just because you din´t lose this time","I´m so close to winning!"]
lose=["Hahaha, I knew it!","Your so bad that honestly, you should just never play again!","Hahaha Loooooser!!","I´m in your head."
                                                                                                       "You can´t win. I promise you so!"]
a="MISTER MALSON PICKED: "
user_points=0
computer_points=0
print("""
+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
|R|o|c|k|,| |P|a|p|e|r|,| |S|c|i|s|s|o|r|s|
+-+-+-+-+-+ +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+

    Hi there! I´m mister Malson and i wan´t to play a game of rock, paper, scissors with you. Do I wan´t to have fun
      you might ask yourself?\n No! I just wan´t to demonstrate my power and BEAT THE CRAB OUT OF YOU!!!\n
    """)
while True:
   if (user_points==5):
       print("No. This can´t be true. You beat me! I just can´t believe that.\nYOU WON THIS GAME ")
       break
   elif (computer_points==5):
       print("HAHAHAHA! I knew it! I´m the best in rock,paper,scissors. And you are just a Loser why did I even play with you?!!")
       break
   user_input=str(input("WHAT DO YOU WAN`T TO PICK?  [rock/paper/scissors]:\n "))
   if (user_input not in pick):
       print("What are you doing? I thought we were going to play.")
       continue
   computer_input=(random.choice(pick))
   if (user_input=="rock"and computer_input=="scissors" ):
       print(random.choice(win),a,computer_input)
       print("YOU WON")
       user_points=user_points+1
   elif (user_input=="scissors"and computer_input=="paper"):
       print(random.choice(win),a,computer_input)
       print("YOU WON")
       user_points = user_points + 1
   elif (user_input=="paper"and computer_input=="rock"):
       print(random.choice(win),a,computer_input)
       print("YOU WON")
       user_points = user_points + 1
   elif(user_input==computer_input):
       print(random.choice(draw),)
       print("DRAW")
   else:
       print(random.choice(lose),a,computer_input)
       print("YOU LOSE")
       computer_points=computer_points+1
   print("YOUR POINTS:",user_points,"/MR.MALSON´S POINTS:",computer_points)


