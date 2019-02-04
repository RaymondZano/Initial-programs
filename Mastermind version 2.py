#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 23:38:43 2019

Version 2 of the Mastermind game
This is a transition program to the final version.

I used loop thru the dataframe 

@author: raymondzano
"""

import random 
import pandas as pd

colors = ["black", "white", "red", "blue", "yellow"] #possible colors to guess
colorRightCount = [0, 0, 0, 0, 0] #initializing the values of the soon-to-be dataframe
colorRightGuess = [0, 0, 0, 0, 0] #initializing the values of the soon-to-be dataframe
colorGuessCount = [0, 0, 0, 0, 0] #initializing the values of the soon-to-be dataframe
colorWrongPosCount = [0, 0, 0, 0, 0] #initializing the values of the soon-to-be dataframe
labels = ['Colors', 'Actual Count', 'Right Guess Count','Guess Count', 'Wrong Position Count'] #different labels to be used in the dataframe
list_cols = [colors, colorRightCount, colorRightGuess, colorGuessCount, colorWrongPosCount] #
zipped = list(zip(labels, list_cols))
data = dict(zipped)
colorListCount = pd.DataFrame(data)

color1 = random.choice(colors) #choosing the four colors to be guess
color2 = random.choice(colors)
color3 = random.choice(colors)
color4 = random.choice(colors)
tobeguess = [color1, color2, color3, color4] #puts the guessed color to a list

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
maxGuess = 2
while guessesTaken < maxGuess:
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
 
    for i in range(len(userGuessColor)):        #for correct color in correct place
        if str(userGuessColor[i]) == str(tobeguess[i]):
            RightPosition += 1                  #counts the right positions
    
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
            guessesTaken = maxGuess * 20 #forcing exit after guessing the puzzle
