#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 23:38:43 2019

@author: raymondzano
"""

import random #for the color randomization
import pandas as pd

colors = ["black", "white", "red", "blue", "yellow"] #possible colors to guess
colorRightCount = [0, 0, 0, 0, 0]
colorRightGuess = [0, 0, 0, 0, 0]
colorGuessCount = [0, 0, 0, 0, 0]
colorWrongPosCount = [0, 0, 0, 0, 0]
labels = ['Colors', 'Actual Count', 'Right Guess Count','Guess Count', 'Wrong Position Count']
list_cols = [colors, colorRightCount, colorRightGuess, colorGuessCount, colorWrongPosCount]
zipped = list(zip(labels, list_cols))
data = dict(zipped)
colorListCount = pd.DataFrame(data)
colorListCount.iloc[:,2]
color1 = random.choice(colors) #choosing the four colors to be guess
color2 = random.choice(colors)
color3 = random.choice(colors)
color4 = random.choice(colors)
tobeguess = [color1, color2, color3, color4]
tobeguess[0]
print(tobeguess)

for i in range(len(tobeguess)): #updates the Actual Count column of the colorListCount table
    for j in range(len(colorListCount)):
        if str(tobeguess[i]) == str(colorListCount.iloc[j,0]):
            colorListCount.iloc[j,1] += 1

print("""
          1. Guess the correct four colors AND its correct position.
          2. There are five possible colors: black, blue, red, white, and yellow.
          3. You have twelve chances to guess.
          4. At the end of each guess, there will be two hints:
              number of color/s in correct position/s
              number of correct color but in wrong position
          """) #mechanics
guessesTaken = 0 #initializing the guess taken by the player
maxguess = 2
while guessesTaken < maxguess:
    RightPosition = 0
    
    userGuessColor1 = input(f"""
    Number of guess/es made : {guessesTaken} out of {maxguess}.
    Possible colors: black, blue, red, white, yellow            
    First color: """)
    userGuessColor2 = input("""
    Second color: """)
    userGuessColor3 = input("""
    Third color: """)
    userGuessColor4 = input("""
    Fourth color: """)       
    userGuessColor = [userGuessColor1, userGuessColor2, userGuessColor3, userGuessColor4]
    #userGuessColor[2]

    for i in range(len(userGuessColor)):        #for correct color in correct place
        if str(userGuessColor[i]) == str(tobeguess[i]):
            RightPosition += 1                  #counts the right positions

    #for i in range(len(tobeguess)):             #for the right color
    #    if str(userGuessColor[i]) == str(tobeguess[i]):
    #        colorListCount.loc[str(userGuessColor[1]),0]
    #        colorListCount.iloc[i,2] += 1       #put in the table the right guess per color

    #colorListCount.keys()

    #pd.print
    #to reset the Guess Count column to zero
    # userGuessColor[i]==0
    #for i in range(len(userGuessColor)):        #counts the guess per color
    #    for j in range(len(colorListCount)):
    #        if str(userGuessColor[i]) == str(colorListCount.iloc[j,0]):
    #            colorListCount.iloc[j,3] += 1   #puts in the table the count per guess per color 
    
    #for i in range(len(colorListCount)):
    #    if colorListCount.iloc[i,1] > colorListCount.iloc[i,2]:
    #        colorListCount.iloc[i,4] = colorListCount.iloc[i,3] - colorListCount.iloc[i,2]

    #colorListCount.iloc[:,2]
    
    guessesTaken = guessesTaken + 1
    
    if RightPosition != 4:
            print(f"""
    Sorry! You did not guess both colors correctly.
    HINT: You have {RightPosition} color in right position """)
            colorListCount.iloc[:,2] = 0 #to do: reset the guess count to 0
    
    elif RightPosition == 4:
            print(f"""
     Wow! You guess the correct colors in their correct positions.
     As you guessed, they are {color1} as first,
                              {color2} as second,
                              {color3} as third, and
                              {color4} as the fourth one.
     You did it in {guessesTaken} guesses only.""")
            guessesTaken = 20 #forcing exit after guessing the puzzle

#there is a counter on how many a specific color is compared already