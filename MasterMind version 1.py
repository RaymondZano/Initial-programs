#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 03:25:19 2019

@author: raymondzano

Game: Mastermind - Most Basic Version

This code is part of a Choose Your Own Adventure game - I  cut-paste-modified
accordingly to fit this page. The game was originally created last October 2018
as one of the requirements for my Business Analytics master degree.

This is limited to guessing two colors only.

The more advanced Mastermind game is almost complete and will be posted immediately
after I finished it. 

"""

import random

colors = ["black", "white", "red", "blue", "yellow"] #list of color that can be guess
color1 = random.choice(colors) #chooses the first color to be guess
color2 = random.choice(colors) #chooses the second color to be guess
print("""
===============================================================================
    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

          You are about to have your
      .------..------..------..------..------.     .------..------..------..------.
      |F.--. ||I.--. ||R.--. ||S.--. ||T.--. |.-.  |G.--. ||A.--. ||M.--. ||E.--. |
      | :(): || (\/) || :(): || :/\: || :/\: ((5)) | :/\: || (\/) || (\/) || (\/) |
      | ()() || :\/: || ()() || :\/: || (__) |'-.-.| :\/: || :\/: || :\/: || :\/: |
      | '--'F|| '--'I|| '--'R|| '--'S|| '--'T| ((1)) '--'G|| '--'A|| '--'M|| '--'E|
      `------'`------'`------'`------'`------'  '-'`------'`------'`------'`------'
      
          Got it? FIRST GAME.
      
          Sorry, it not a cards game - I just like the font.
      
          Your fate depends on the hands, whether you hold on or not. Well, 
          actually your fingers and brain.
      
          This game is the modified version of Mastermind - smaller scale.
      
          If you have not played or forgot the mechanics, do not worry, just
          press Enter for the MECHANICS.
        """)
input("""
          <Press Enter to continue>
          """)
print("""
          .------..------..------..------..------..------..------..------..------.
          |M.--. ||E.--. ||C.--. ||H.--. ||A.--. ||N.--. ||I.--. ||C.--. ||S.--. |
          | (\/) || (\/) || :/\: || :/\: || (\/) || :(): || (\/) || :/\: || :/\: |
          | :\/: || :\/: || :\/: || (__) || :\/: || ()() || :\/: || :\/: || :\/: |
          | '--'M|| '--'E|| '--'C|| '--'H|| '--'A|| '--'N|| '--'I|| '--'C|| '--'S|
          `------'`------'`------'`------'`------'`------'`------'`------'`------'
          1. Guess the correct two colors AND its correct position:
              either first or second.
          
          2. There are five possible colors:
              black, blue, red, white, and yellow.
          
          3. You have seven chances to guess.
          
          4. At the end of each guess, there will be one hint:
              number of color in correct position
          
          Good luck and see you in the other side.
          """)
guessesTaken = 0
maxGuess = 7 #can be change to increase or decrease difficulty
    
while guessesTaken < maxGuess: #loop for checking whether the guesses are correct
    RightPosition1 = 0
    RightPosition2 = 0
    TotRightPosition = 0 
       
    userColor1 = input(f"""
          Number of guess/es made : {guessesTaken}
          Remember you only have seven chances.
          Possible colors: black, blue, red, white, yellow
              
          First color: 
                  """) #first guess
    userColor2 = input("""
          Second color: 
                  """) #second guess

    if userColor1 == color1: #checks if the first guess is the same as the first correct color
        RightPosition1 += 1

    if userColor2 == color2: #checks if the second guess is the same as the second correct color
        RightPosition2 += 1
        
    TotRightPosition =  RightPosition1 + RightPosition2 #adds the correct guess, it must be two to win

    guessesTaken = guessesTaken + 1
    
    if TotRightPosition != 2: #if the number of correct guess is less than 2, allows user to guess again as along as less than maximum number of gueses
        print(f"""
          Sorry! You did not guess both colors correctly.
          HINT: You have {TotRightPosition} color in right position
              """)
 
    elif TotRightPosition == 2: #if the player guesses the two correct colors
        print(f"""
          Wow! You guess the correct colors in their correct positions.

          As you guessed, they are {color1} as first and
              
                                   {color2} as second.          
          You did it in {guessesTaken} guesses only.

              """)
        guessesTaken = maxGuess * 2  #ensures the code will end once the correct colors are guess
