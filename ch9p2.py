'''
2.
The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
'''

import random

def game():
    print("You are playing a Game...")
    score = random.randint(1, 99)
    
    with open("high_score.txt") as f:
        high_score = f.read()
        if(high_score != ""):
            high_score = int(high_score)
        else:
            high_score = 0
            
    print(f"Your score is: {score}")
    
    if(score > high_score):
        with open("high_score.txt", "w") as f:
            f.write(str(score))
                
    return score

game()