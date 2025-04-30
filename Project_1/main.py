'''
1 for snake
-1 for water
0 for gun
'''

import random


userDict = {"s": -1, "w": 0, "g": 1}
reverseDict = {-1: "Snake", 0: "Water", 1: "Gun"}
ch = "y"

while (ch.lower() == "y"):
      print('''
            s for snake
            w for water
            g for gun
      ''')

      computer = random.choice([-1, 0, 1])
      
      userInput = input("Enter your choice: ").lower()


      if (userInput =="s" or userInput == "w" or userInput == "g"):
            
            user = userDict[userInput]
            print(f"You chose {reverseDict[user]} and Computer chose {reverseDict[computer]}.")

            if (user == computer):
                  print("It's a Draw!")
            elif(user == -1 and computer == 0):
                  print("You Win!")
            elif(user == -1 and computer == 1):
                  print("You Lose!")
            elif(user == 0 and computer == -1):
                  print("You Lose!")
            elif(user == 0 and computer == 1):
                  print("You Win!")
            elif(user == 1 and computer == -1):
                  print("You Win!")
            elif(user == 1 and computer == 0):
                  print("You Lose!")

            #------------------------------------------------------
            '''An alternate way to make same game but in less line of code 
            It is analyzed on the basis of user - computer.
            '''
            # if (user == computer):
            #       print("It's a Draw!")
            # elif (user - computer == -1 or user - computer == 2):
            #       print("You Win!")
            # else:
            #       print("You Lose!")

      else:
            print("Something went Wrong!")
      
      ch = input("Enter \"y\" to play again or press any other key to exit!: ")