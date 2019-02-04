#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 23:02:48 2018

@author: raymondzano
This is the text adventure game where the basic mastermind game is part of.
Do the adventure and see the other games.
There are fail points that you may encounter, please let me know.
I have a longer version idea of the game. I hope I have time to sit on it and release.
"""
"""
DocString:
    
    A) Introduction:
    You are a student finishing your requirement when suddenly a strong
    earthquake strikes your place. You need to stay alive and reach your
    apartment. Along the way, you will encounter different scenarios
    incorporated with games that will test you knowledge and a little bit of
    luck.
    
    B) Gameplay
    The story starts in your school. Your next adventure depends on you:
        Run along the seashore
        Climb the hill
        Traverse a long forgotten dirt road
    
    There are two instances where you need to decide your next step.
    
    There are three games with two variations each strategically located on
    each route:
        Mastermind
        Guess the Passcode
        Q&A
    
    There are nine exit points with only two being successful.
   
    C) Known Bugs and/or Errors:
    'THE END' ASCII is distorted
    After successfully finishing the game, it goes back to the "unfinished"
    games.
    
    D) Possible Areas of Improvement
    I have at least four but will exceed the 150-word requirement for docstring.
"""

def game_start():
    global player
    global firstname
    #this is the start of the game. it sets the tone and pace of the adventure
    print("""
===============================================================================
    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
===============================================================================
          Welcome to 
          
            ____ _   _  ___   ___  ____  _____                      
           / ___| | | |/ _ \ / _ \/ ___|| ____|                     
          | |   | |_| | | | | | | \___ \|  _|                       
          | |___|  _  | |_| | |_| |___) | |___                      
          _\____|_|_|_|\___/_\___/|____/|_____|                     
          \ \ / / _ \| | | |  _ \                                   
           \ V / | | | | | | |_) |                                  
            | || |_| | |_| |  _ <                                   
            |_| \___/_\___/|_|_\_\___ _   _ _____ _   _ ____  _____ 
            / \  |  _ \ \   / / ____| \ | |_   _| | | |  _ \| ____|
           / _ \ | | | \ \ / /|  _| |  \| | | | | | | | |_) |  _|  
          / ___ \| |_| |\ V / | |___| |\  | | | | |_| |  _ <| |___ 
         /_/   \_\____/  \_/  |_____|_| \_| |_|  \___/|_| \_\_____|
               ______       _       ____    ____  ________  _  
             .' ___  |     / \     |_   \  /   _||_   __  || | 
            / .'   \_|    / _ \      |   \/   |    | |_ \_|| | 
            | |   ____   / ___ \     | |\  /| |    |  _| _ | | 
            \ `.___]  |_/ /   \ \_  _| |_\/_| |_  _| |__/ ||_| 
             `._____.'|____| |____||_____||_____||________|(_) 
             """)
                                                                                                              

    player = input("""
          Before we start I need three information from you:
              Tell me your name. Please type it:
                   """)
    print(f"""
          Welcome {player}!
          
          In this game, you will experience alternative adventure and ending
          depending on your choice, wisdom, and luck.
          """)
    firstname = input("""   
          Now give me a name of your best friend or friend.
          
          Do not worry! We will contact your friend.
                      """)
    print(f"""
          Alright {player}! You are a student and needs to arrive safely to 
          your apartment after an event.
          """)
    input("""
          Sit back and relax! If you are ready to be engaged in the next five
          minutes, press Enter.
          
===============================================================================
    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
===============================================================================
          """)
    input()
    print("""
          You close your eyes for a while and recline back to your chair. “I 
          need this quick rest” you thought to yourself. You made a quick 
          glance to the time in your laptop and saw 11:05PM “Good! I still have 
          54 more minutes before the deadline”. And close your eyes once again.
          """)
    input("""
          <Press Enter to continue>
          """)
    print("""
          You arrived in your school after changing from your morning run 
          outfit. You just had a hearty lunch. This will be a long day - study 
          group for two final exams and a final report due end-of-day today. 
          But you are prepared, you packed your dinner and brought it with you 
          in the school.
          """)
    input("""
          <Press Enter to continue>
          """)
    print("""
          Beeep!

          You heard your phone made the empty-battery sound. “How can I forgot
          to charge my phone” you thought to yourself. You straighten your 
          chair up and reach for your bag. You fish for the charger and cable 
          inside. There it is. You pull it out of your bag and plug it to the 
          wall and insert the cable to your phone. You wait for a while and 
          turned on your phone. 2%. This may take a while and place it beside 
          your laptop. You turn to your laptop and submitted your report. 
          11:14PM! “Great now I can start packing apartment but first”, you 
          thought once again.
          """)
    input("""
          <Press Enter to continue>
          """)
    print("""
          “Okay, what’s happening in the outside world?!” You opened WhatsApp
          in your laptop and check your feeds. Mostly about the exams and the
          paper. Then there are thank you messages from your group mates in the
          group study posted three hours ago. You replied ‘No problem guys! You
          are welcome’ with a smiley emoji. The recent feeds are about an 
          escaped serial killer from the jail near your school. Messages of 
          concern follow after that. Then you read ‘big built, skull tattoos on 
          both arms’. You were still reading when you feel the ground shake. An 
          earthquake! 
          """)
    stayorleave()

def stayorleave():
    #after the earthquake, the hero needs to decide what to do after the earthquake
    print("""
          You lost your balance and fall to the ground. The table 
          and chairs are shaking very vigorously. This is a strong one! Then 
          you remember: drop-cover hold. You crawl towards the table like a 
          baby starting to learn one – you can barely hold your ground and 
          slide twice. After reaching under the table, you do as you remember 
          and close your eyes. It felt like an eternity. You hear shelves 
          tumbling down. Window glasses breaking and falling. You feel sharp 
          objects hit slightly your arms and face. Then the lights go dark and 
          suddenly everything stopped.
          """)
    input("""
          <Press Enter to continue>
          """)
    print("""
          You listen for a while and slowly open your eyes. You barely see 
          anything.Then your sight adjusted. Your phone fell to the floor. Lit, 
          still plugged but not charging. You reach for it and reads 14%. You 
          slowly stand up. I need to stay safe and alive. What will you do.
          """)
    input("""
          <Press Enter to continue>
          """)
    to_do = 0
    to_do = input("""
          a. Pack my bag and leave for my apartment
          b. Stay, call 911, and wait for the rescue to come
          
          Enter the letter or keywords of your choice below.
          """)
    if to_do == 'a' or to_do == 'pack' or to_do == 'leave':
        leave()
    elif to_do == 'b' or to_do == 'stay' or to_do == 'wait':
        stay()
    else:
          print("""
          Please type the correct letter.
              """)
          
def stay():
    #the hero decided to stay not knowing this is the end
    print("""
          You chose to stay. You pick up your phone and dial 911. It took a 
          while before a dispatcher answered your call. You can tell from the 
          background noise that they are extremely busy and receiving similar
          calls. This is really a big earthquake. You share your location 
          details. The dispatcher asked for your safety status. After assessing 
          and sharing further information, you are told that help may come 
          between 10-20 minutes but is not guaranteed. You are also advised to
          stay away from the sea due to tsunami warning and possible stronger
          aftershock. After you bade good bye and hang up the call, you 
          immediately pack your things up. You reach for your bag, place your 
          laptop inside, pull the cables and chargers, and place them same 
          inside your bag. You can hear distant sirens - both from ambulance 
          and firetrucks. The half-moon barely lit the room, but you are okay,
          you just hope that help will come… quick.
          """)
    input("""
          <Press Enter to continue>
          """)  
    print("""
          After five minutes, you hear sound of water rushing in. Your school 
          is near the sea but not close enough to hear the waves. This is 
          different. This is the tsunami that the 911 dispatcher had warned 
          you about. You walk towards the window facing the sea and watch as a 
          wall of water, from your third floor where you are, bumps everything 
          on its path towards your school. This is huge. As it hit your school,
          you feel it shake a little. You hope your school is strong enough to
          withstand the strength brought by this torrent of water.
          """)
    input("""
          <Press Enter to continue>
          """)  
    print("""
          Another 5 minutes has pass and the ground started to shake again – 
          the aftershock. This time it is stronger than the first. You drop to
          the floor again not caring whether it is on broken glasses or clear 
          space. As you cover, you hear a loud crack. Then followed by a second
          one. Your school is collapsing. Before you can move a single muscle, 
          you feel your chest suppressed. You cannot breathe. You tried pushing
          it, but you can’t. Then something hit your head.
          """)
    fail()

def leave():
    #our hero leaves the building to continue the adventure into the world
    print("""
          You decided to pack your things and leave for your apartment. You 
          reach your bag, place your laptop inside, pull the cables and 
          chargers, and place them same inside your bag. Using the light from 
          your phone, you walk carefully but quickly towards the emergency exit
          of your school building. You walked down two levels of stairs before 
          reaching the lobby. You can hear distant sirens - both from ambulance
          and firetrucks. The half-moon barely helps lighting the area, but
          you need to get to your apartment… quick. Your school building is 
          beside a hill and your apartment is on the other side.
          """)
    input("""
          <Press Enter to continue>
          """)
    print("""
          You have three routes to your apartment. Your usual route is along 
          the seashore. It takes you 40 minutes going to school and 55-60 
          minutes back - due to elevation difference. The second route is 
          through a dirt road around the hill. Elevation increase 
          slower but takes you 90 minutes to school and two hours back. The 
          third route is thru the hill - would have been the mid-way if not for
          the steep stairs. Before you decided what route to take, you feel 
          your stomach growl. You remember sharing your packed dinner with your
          study group earlier and now you need one.
          """) 
    input("""
          <Press Enter to continue>
          """)
    where_to=0
    where_to=input("""
          What route will you take?
          a. Take the seashore - my usual route
          b. Thru the dirt road around the hill
          c. Up and down thru the hill
          """)
    if where_to == 'a' or where_to == 'usual' or where_to == 'seashore' or where_to == 'sea':
        seashore()
    elif where_to == 'b' or where_to == 'dirt road' or where_to == 'around' or where_to == 'dirt':
        dirtroad()
    elif where_to == 'c' or where_to == 'hill':
        prehill()
    else:
        print("""
              Please type the correct letter
              """)

def seashore():
    #our hero chooses to traverse the seashore route - the usual route
    print("""
          You chose to take the seashore route. You are practically running to
          your apartment. You will be home in no time. Then you hear a familiar
          siren. It is longer and louder. You heard it several times before but
          only remembered the word TEST in the announcement that follows. It is
          a tsunami warning! You look to your right and notice the sea is gone.
          You run faster. Then you hear a rushing sound coming.
          """)
    input("""
          <Press Enter to continue>
          """)
    print("""
          The tsunami is coming. You run faster. You are now halfway. You now 
          hear the wave coming louder. Can you make it? You made a quick glance
          to the right. Before you can even look forward; a strong wave hit 
          your left side and push you towards the wall separating the road to
          the hill. Instinctively, you reach for something and was able to grab
          a branch. You should be able to hold on tight and not be carried away.           
          """)
    input("""
          <Press Enter to continue>
          """)
    print("""
          Or the waves will carry out to the open sea?
          """)
    input("""
          <Press Enter to continue>
          """)
    mastermindseashore()

def mastermindseashore():
    #this game has eight chances to guess the combination, lower than the other
    import random

    colors = ["black", "white", "red", "blue", "yellow"]
    color1 = random.choice(colors)
    color2 = random.choice(colors)
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
    
    while guessesTaken < 7:
        RightPosition1 = 0
        RightPosition2 = 0
        TotRightPosition = 0 
       
        userColor1 = input(f"""
          Number of guess/es made : {guessesTaken}
          Remember you only have seven chances.
          Possible colors: black, blue, red, white, yellow
              
          First color: 
                  """)
        userColor2 = input("""
          Second color: 
                  """)

        if userColor1 == color1:
            RightPosition1 += 1

        if userColor2 == color2:
            RightPosition2 += 1
        
        TotRightPosition =  RightPosition1 + RightPosition2

        guessesTaken = guessesTaken + 1
    
        if TotRightPosition != 2:
            print(f"""
          Sorry! You did not guess both colors correctly.
          HINT: You have {TotRightPosition} color in right position
              """)
 
        elif TotRightPosition == 2:
            print(f"""
          Wow! You guess the correct colors in their correct positions.

          As you guessed, they are {color1} as first and
              
                                   {color2} as second.          
          You did it in {guessesTaken} guesses only.

              """)
            input("""
          <Press Enter to continue>

    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
===============================================================================
              """)
            hillfromtsunami()
            break

    print(f"""
          The correct colors are {color1} as first and
              
                                 {color2} as second.

          Sorry! You did not guess correctly the two colors.
      """)
    input("""
          <Press Enter to continue>
              """)
    failseashore()

def failseashore():
    print("""
          You lose your hold on the branch. The strong current brought you
          towards the solid wall and bump your head on it. Thud! You lose
          your consciousness.
          """)
    input("""
          <Press Enter to continue>
              """)
    fail()
    
def hillfromtsunami():
    #after surviving the tsunami, our hero is forced to take the hill route
    print("""
          You made it. It is a good thing your bag is waterproof, and you 
          are sure your gadgets are dry. You swim towards the hill. This 
          changes your plan. You now have to traverse up the hill down to 
          your apartment. You rest for a while to dry and start to climb 
          to the cemented trail.
          """)
    input("""
          <Press Enter to continue>
          """)
    hill()

def prehill():
    #our hero started the hill climb - entry from both seashore and after route
    #decision
    print("""
          You chose to traverse the hill. You just run through this hill 
          this morning. You do not normally pass by here this time of the 
          night. But this is a different night. It is an emergency and you
          need to be home as soon as possible. You are careful with your 
          steps. Checking whether there are loose stones or falling trees.
          """)
    input("""
          <Press Enter to continue>
              """)
    hill()

def hill():
    #our hero continues the hill climb
    print("""
          You are in your climbing pace now. As you climb higher, you feel
          another tremor – the aftershock. You feel your adrenaline rise up
          again. This is stronger than the first one. You drop to the 
          ground again, cover yourself, and hold that position. You hear 
          leaves shaking and some branches fell from afar. Then it stopped.
          This is shorter than the first one. You uncurl yourself and look
          around you. Silence. You slowly stand up. Nothing worse can 
          happen here, you thought to yourself. You continue walking up the
          hill when you hear a creaking sound.
          """)
    input("""
          <Press Enter to continue>
          """)
    print("""
          Sounds like something is splitting apart and it is getting louder.
          You turn around and saw a big shadow increasing in size. A tall 
          tree is falling towards you.
          """)
    print("""
          You run to the right and make a huge leap. A loud thud followed
          by a strong wind sweep from your back. The tree fall just inches 
          away from you. But you are safe. How much worse can this night
          get, you thought to yourself. You are about to walk away when you
          hear a scream for help. Where is it coming from? 
          """)
    input("""
          <Press Enter to continue>
          """)
    print("""
          You walk towards the tree. Slowly. Estimating where the sound is
          coming from. Then you see it – a man trapped under the tree. It
          seems you are not alone taking refuge on the hill for safety. You
          cannot see him through the darkness but the goodness in you
          dictated you need to help him.
                    """)
    input("""
          <Press Enter to continue>
          """)
    print("""
          You look for a part where you can hold and lift and let him slide
          out. After scraping across the trunk, you hope you made a good 
          decision for that position. The darkness is keeping you from 
          making quick and clever visual decisions. Then you tell the man 
          that in count of three both of you push the tree up. You make
          your countdown then you muster all your strength. 
          """)
    qandahill()

def dirtroad():
    #our hero chooses the dirt road
    print("""
          You chose the dirt road. You can’t even recall when is the last time
          you pass thru here. The unpaved road is covered with larger than 
          usual gravel thus it hurts your feet whenever you pass thru here. It
          is a two-way road but is seldom use. Your transition your thought to
          your situation. Is your house still standing after such earthquake? 
          Do you still have the exams this week? Is your school still safe 
          after such shaking? You are also checking your right side every now
          and then for possible landslide.
          """)
    input("""
          <Press Enter to continue>
          """)
    print(f"""
          Suddenly your stomach growls again. You need to find something to 
          eat. You remember your high school best friend {firstname} lives 
          along this road. You studied together in high school, but was accepted
          in a university on the east coast, where you are from. You remember 
          how your friend disarm their alarm if he forgot his keys. Fun days! 
          You can pass by it, check them if his family are okay, and if you are 
          lucky, they’ll offer you something to eat. Sounds like a plan – you 
          agree to yourself.
          """)
    input("""
          <Press Enter to continue>
          """)
    print("""
          You are still several hundred meters and you already see their house.
          As you scale towards the house, you notice the house is dark – its 
          emergency lights are off. That is odd. But their old car is still 
          park outside. They must have used a cab or got a newer car. Anyway, 
          you need to eat. You thought to yourself. You approach their lawn, 
          walk towards the door. You press the doorbell. It is broken. No 
          choice now but to disarm the alarm. Is it possible they still keep 
          the old passcode combination? You are taking your chances. You enter
          the passcode.
          """)
    input("""
          <Press Enter to continue>
          """)
    mastermindhill()

def mastermindhill():
    #this game has 10 chances to guess the combination - higher than the other one
    import random

    colors = ["black", "white", "red", "blue", "yellow"]
    color1 = random.choice(colors)
    color2 = random.choice(colors)
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
      
          Your fate depends on the hands, whether you enter the correct
          passcode or not. Well, actually your fingers and brain.
      
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
          
          3. You have eight chances to guess.
          
          4. At the end of each guess, there will be one hint:
              number of color in correct position
          
          Good luck and see you in the other side.
          
    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
===============================================================================
          """)
    guessesTaken = 0
    
    while guessesTaken < 8:
        RightPosition1 = 0
        RightPosition2 = 0
        TotRightPosition = 0
    
        userColor1 = input(f"""
          Number of guess/es made : {guessesTaken}
          Remember you only have eight chances.
          Possible colors: black, blue, red, white, yellow
              
          First color: 
                  """)
        userColor2 = input("""
          Second color: 
                  """)

        if userColor1 == color1:
            RightPosition1 += 1

        if userColor2 == color2:
            RightPosition2 += 1
        
        TotRightPosition =  RightPosition1 + RightPosition2

        guessesTaken = guessesTaken + 1
    
        if TotRightPosition != 2:
            print(f"""
          Sorry! You did not guess both colors correctly.
          HINT: You have {TotRightPosition} color in right position
              """)
 
        elif TotRightPosition == 2:
            print("""
          Wow! You guess the correct colors in their correct positions.
          
          Your adventure continues!
              """)
            input("""
          <Press Enter to continue>

    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
===============================================================================
              """)
            decoded()
            break

    print(f"""
          The correct colors are {color1} as first and
              
                                 {color2} as second.
          Sorry! You did not guess correctly the two colors.
      """)
    input("""
          <Press Enter to continue>
              """)
    print("""
          You were unsuccessful. The alarm rings. You panic.
          """)
    input("""
          <Press Enter to continue>
              """)
    print("""
          You do not know how to stop it. You tried entering another passcode.
          Still unsuccessful. What will you do? Run away? Knock louder? Then
          you hear siren. A police car siren.
          """)
    input("""
          <Press Enter to continue>
              """)
    print("""   
          You are now sweating heavily.What am I thinking? You thought to 
          yourself. You try dialing your friend’s number but there is no 
          signal. Damn this earthquake! You thought to yourself. The siren 
          grows louder. They are police siren. Why will you think they kept the
          same passcode for a long time? As the red and blue lights stop in 
          front of the house, you have no choice but to surrender.
            """)
    input("""
          <Press Enter to continue>
              """)
    print("""         
          You face towards them and put your hands up. Breathing heavily as the
          police positioned themselves in a defense mode advancing towarsd you
          pointing their guns to your direction.
          """)
    input("""
          <Press Enter to continue>
              """)
    fail()

def decoded():
    #our hero successfully decoded the door password
    print("""
          Alright! You are successful! They keep the same passcode all this 
          time. You open then close the door behind you slowly. Take out your 
          phone for lighting. It is cold. They must have left the heater off.
          You look around. The earthquake caused considerable damage inside the
          house. You pass by the laundry room and see clothes on the floor - as
          if someone is looking for something. Then a trail of red liquid flows
          to the kitchen. Did someone just get hurt from the earthquake? You 
          follow it, careful not to step on them. Then you see the broken 
          plates and glasses everywhere. This is unusual. You thought to 
          yourself. Did a fight just occur here? Then you see a knife tainted 
          with the red liquid. It is blood!
          """)
    input("""
          <Press Enter to continue>
              """)
    print(""" 
          You had goosebumps. It must be more than a fight. Then, you focus on 
          their back door – it is open with its glass smashed. There are foot 
          prints coming from the outside. Did you friend’s parent get hurt 
          badly or worse? You feel your adrenaline goes up. You need to leave. 
          You run back to the living room and found the door open!!
          """)
    input("""
          <Press Enter to continue>
              """)
    print("""
          You perfectly remember closing it after you. Someone else is still 
          here and just exited after you enter. You pick up a lamp. For my
          defense, you thought. You move closer to the door and look outside. 
          You see a man behind the car’s trunk. You immediately hide behind the
          door. You listen. You hear the trunk close, then after some time the 
          car door opens. You remember your phone. You try to dial 911. No 
          signal! Damn this earthquake! The car engine starts. You again have a
          look - still behind the door. He exits the car. It is NOT your 
          friend’s father - you are sure – this one’s huge. Is he trying to 
          steal the car? The moon light hit him. He is wearing a shirt smaller 
          for his size. Then you see his left arm – skull tattoos. Your face
          flushes.
           """)
    input("""
          <Press Enter to continue>
              """)
    print("""         
          You remember the feed in WhatsApp earlier – big build, skull tattoos 
          on both arms. Could this be the escaped serial killer? What did he do
          to your friend’s parents? He is now walking back inside the house.
          You freeze. What will I do? I need to stop him. You raise your hands
          holding the lamp you picked up earlier. You plan to knock out the man. 
          The steps grow louder. The door opens a little then you see his back.
          This is it! You swing your arms with all your might!
          
          Are you successful? 
          """)
    qandadirt()

def qandahill():
    #
    import random

    QandA = [
            ['Multiple 37 and 3','111'],
            ['Highest mountain in the world is _______','Everest'],
            ['In light colorwheel, green and blue makes?','cyan'],
            ['Complete the sequence - 2 3 6 15 ________','42'],
            ['What is the month of the Signing of the US Declaration of Independence?','August']
            ]

    random.shuffle(QandA)

    numRight = 0
    qNum = 0
    rightAnswer = 0

    print("""
===============================================================================
    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

             _  _  ____  __     ___  __   _  _  ____ 
            / )( \(  __)(  )   / __)/  \ ( \/ )(  __)
            \ /\ / ) _) / (_/\( (__(  O )/ \/ \ ) _) 
            (_/\_)(____)\____/ \___)\__/ \_)(_/(____)
              ____  __         _  _  __   _  _  ____  
             (_  _)/  \       ( \/ )/  \ / )( \(  _ \ 
               )( (  O )       )  /(  O )) \/ ( )   / 
              (__) \__/       (__/  \__/ \____/(__\_) 
.------..------..------..------..------..------.     .------..------..------..------.
|S.--. ||E.--. ||C.--. ||O.--. ||N.--. ||D.--. |.-.  |G.--. ||A.--. ||M.--. ||E.--. |
| :/\: || (\/) || :/\: || :/\: || :(): || :/\: ((5)) | :/\: || (\/) || (\/) || (\/) |
| :\/: || :\/: || :\/: || :\/: || ()() || (__) |'-.-.| :\/: || :\/: || :\/: || :\/: |
| '--'S|| '--'E|| '--'C|| '--'O|| '--'N|| '--'D| ((1)) '--'G|| '--'A|| '--'M|| '--'E|
`------'`------'`------'`------'`------'`------'  '-'`------'`------'`------'`------'
              
          Or first... depending on what route you take. Either way, you made
          it this far. Good job!
              
          This is a very simple game.
              """)
    input("""
          <Press Enter to continue>
              """)      
    input("""       
          You just need to answer three questions correctly. They are
          randomly selected from the universe of knowledge.
          
          If you answered all them correctly, you will be able to lift the tree.
              
          If you are ready, please press Enter.
          """)

    while rightAnswer <3:

        answer = input(f"""
          Here is question number {qNum + 1}:
            
                  {QandA[qNum][0]} :
                      """)

        if answer == QandA[qNum][1]:
            numRight += 1
            rightAnswer += 1
            qNum += 1
            if qNum !=3:
                print(f"""
          Correct! You advance to question number {qNum + 1}.
              
          Good luck!
                  """)
            input("""
          <Press Enter to continue>                 
                  """)
        
        else:
            print(f"""
          Sorry! You are incorrect. For question:
              
              {QandA[qNum][0]}
              
              the answer is
              
              {QandA[qNum][1]}
              """)
            input("""
          <Press Enter to continue>
              """)
            print("""
          The tree is just too heavy. Then you hear something is sliding.
          You are progressing, but the earth is going down. What is
          happening? You realize that the two earthquakes caused a
          landslide and you are sliding down with the tree. It was too late
          now. You, the man, together with the tree are falling down the
          cliff. Faster and faster. Then somethin hit you.
              """)
            fail()
    print("""
              Three correct answers!
          
              (    (    (             )  (     (    (       ____ 
              )\ ) )\ ) )\ )       ( /(  )\ )  )\ ) )\ )   |   / 
              (()/((()/((()/(  (    )\())(()/( (()/((()/(   |  /  
              /(_))/(_))/(_)) )\  ((_)\  /(_)) /(_))/(_))  | /   
              (_)) (_)) (_))  ((_)  _((_)(_))_ (_)) (_))_   |/    
              / __|| _ \| |   | __|| \| | |   \|_ _| |   \ (      
              \__ \|  _/| |__ | _| | .` | | |) || |  | |) |)\     
              |___/|_|  |____||___||_|\_| |___/|___| |___/((_)
              
              Your adventure continues!

    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
===============================================================================
          """)
    criminal()

def qandadirt():
    import random

    QandA = [
            ['Multiply 37 and 3','111'],
            ['Second highest mountain in the world is _______','K2'],
            ['In light colorwheel, green and blue makes?','cyan'],
            ['Complete the sequence - 2 3 6 15 ________','42'],
            ['What is the month of the Signing of the US Declaration of Independence?','August'],
            ['In Ohm s law equation, V=IR, what is I?','current'],
            ['What is gravity in feet/second rounded to the nearest one?','32'],
            ['Rounded to the nearest ones what degree does the Tropic of Cancer located?','23'],
            ['What era are we in now in terms of Earth history? Clue: Proper noun','Cenozoic']
            ]

    random.shuffle(QandA)

    numRight = 0
    qNum = 0
    rightAnswer = 0

    print("""
===============================================================================
    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

             _  _  ____  __     ___  __   _  _  ____ 
            / )( \(  __)(  )   / __)/  \ ( \/ )(  __)
            \ /\ / ) _) / (_/\( (__(  O )/ \/ \ ) _) 
            (_/\_)(____)\____/ \___)\__/ \_)(_/(____)
              ____  __         _  _  __   _  _  ____  
             (_  _)/  \       ( \/ )/  \ / )( \(  _ \ 
               )( (  O )       )  /(  O )) \/ ( )   / 
              (__) \__/       (__/  \__/ \____/(__\_) 
.------..------..------..------..------..------.     .------..------..------..------.
|S.--. ||E.--. ||C.--. ||O.--. ||N.--. ||D.--. |.-.  |G.--. ||A.--. ||M.--. ||E.--. |
| :/\: || (\/) || :/\: || :/\: || :(): || :/\: ((5)) | :/\: || (\/) || (\/) || (\/) |
| :\/: || :\/: || :\/: || :\/: || ()() || (__) |'-.-.| :\/: || :\/: || :\/: || :\/: |
| '--'S|| '--'E|| '--'C|| '--'O|| '--'N|| '--'D| ((1)) '--'G|| '--'A|| '--'M|| '--'E|
`------'`------'`------'`------'`------'`------'  '-'`------'`------'`------'`------'
              
          Or first... depending on what route you take. Either way, you made
          it this far. Good job!
              
          This is a very simple game.
              """)
    input("""
          <Press Enter to continue>
              """)      
    input("""       
          You just need to answer five questions correctly. They are
          randomly selected from the universe of knowledge.
          
          If you answered all them correctly, you will knock out the killer.
              
          If you are ready, please press Enter.
          """)

    while rightAnswer <5:

        answer = input(f"""
          Here is question number {qNum + 1}:
            
                  {QandA[qNum][0]} :
                      """)

        if answer == QandA[qNum][1]:
            numRight += 1
            rightAnswer += 1
            qNum += 1
            if qNum !=5:
                print(f"""
          Correct! You advance to question number {qNum + 1}.
              
          Good luck!
                  """)
            input("""
          <Press Enter to continue>                 
                  """)
        
        else:
            print(f"""
          Sorry! You are incorrect. For question:
              
              {QandA[qNum][0]}
              
              the answer is
              
              {QandA[qNum][1]}
              """)
            input("""
          <Press Enter to continue>
              """)
            print("""
          You are not successful! You hit his back, not his nape. He turns
          toward you and slam the door close. You are cornered. You point the
          lamp towards him – breathing heavily. He appears not threaten. He 
          approaches you and grab you by the neck. You try to hit his head with
          the lamp, but he blocks it with the other hand. It fell to the floor.
          He lifts you up and quickly slams you to the floor. Your head hit the
          floor. You blackout.
              """)
            fail()
    input("""
              FIVE correct answers!
          
              (    (    (             )  (     (    (       ____ 
              )\ ) )\ ) )\ )       ( /(  )\ )  )\ ) )\ )   |   / 
              (()/((()/((()/(  (    )\())(()/( (()/((()/(   |  /  
              /(_))/(_))/(_)) )\  ((_)\  /(_)) /(_))/(_))  | /   
              (_)) (_)) (_))  ((_)  _((_)(_))_ (_)) (_))_   |/    
              / __|| _ \| |   | __|| \| | |   \|_ _| |   \ (      
              \__ \|  _/| |__ | _| | .` | | |) || |  | |) |)\     
              |___/|_|  |____||___||_|\_| |___/|___| |___/((_)
              
              Your adventure continues!

          <Press Enter to continue>

    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
===============================================================================
          """)
    escaped()

def criminal():
    print("""
          Great teamwork! You are able to let the man out. “Are you okay?” 
          you ask him while kneeling down on one knee. The man is still
          lying on his back on the ground. He did not reply. He must be in
          pain, you thought to yourself. You tell him to stay still. You 
          bring out your phone and tell the man you will call 911 for help.
          You are about to put the phone on your ears when he slaps the 
          phone away from you. You are surprised with his demeanor. Then 
          the man suddenly stands up. He is taller than you. “You cannot do
          that!” he tells you forcefully in a hoarse voice.
          """)
    input("""
          <Press Enter to continue>
          """)
    print("""
          You try to make sense of the situation. Who doesn’t want help
          after two earthquakes, a tsunami, and being fallen upon by a
          tree? You look at the man’s big-built silhouette. Maybe he is not
          hurt after all. Then the half-moon suddenly shine through the 
          trees revealing the man’s overall physique. He is wearing 
          oversize shirt and short. It is striped horizontally with white
          and another color you cannot distinguish with that amount of 
          light. Then it hit you, could this be the.. 
           """)
    input("""
          <Press Enter to continue>
          """)
    print("""             
          Before you can finish your thought, the man pick you up with his
          two hands and slam you against the tree. He is shouting questions
          repeatedly: where are you from? what are you doing here? are you
          a police?. You cannot answer because you are losing air.
           """)
    input("""
          <Press Enter to continue>
          """)
    print("""              
          You hold on to his shirt sleeves and try to push him away. He is
          stronger than you. Then you accidentally tear his shirt sleeves 
          causing your head to jerk forward and hit his head. Both of you 
          fell to the ground. For a moment, you feel like vomiting and
          light-headed. Excruciating pain radiates from your forehead and
          your back. Then you recover. You look around to find where he is.
           """)
    input("""
          <Press Enter to continue>
          """)
    print("""               
          You found him. You can see his exposed skull tattoo after you
          accidentally tear his sleeves. He is definitely the escaped 
          serial killer. He already standing up. 
          """)
    jump()
def escaped():
    print("""
          You did it! But he only falls to his knees. He stands up and turns 
          toward you. You feel his raging gaze towards you. You didn’t hit him 
          hard enough. You are cornered. You point the lamp towards him – 
          breathing heavily. He appears not threaten. He approaches you and 
          grabs you by the neck. You try to hit his head with the lamp again.
          It is successful! Both of you drop to the floor. You quickly stand up
          and check. He is now unconscious. Now you can escape. You open the 
          door fully and run outside. You turn to the car – you can use the car
          to escape. You take the driver seat. Taking another look towards the 
          house – he is still down. You drive out of the lawn. Way down the 
          road, you can see police lights.
          """)
    input("""
          <Press Enter to continue>          
          """)
    print("""
          You are halfway to your place when you spot the police. You stop your
          car. Surprisingly they also try to stop you. You see one of them 
          talking to the radio and pulls out something from his pocket. The 
          other officer slowly approaches you. He asks for license and 
          registration.
          
          What is going on? You are an earthquake survivor. You just found the
          escaped serial killer. You need their help.
          """)
    input("""
          <Press Enter to continue>          
          """)
    print("""          
          You shared your story. Another patrol car arrives in the scene. Two 
          officers off-board and seem to assume a defensive position. What is 
          happening? The second police man, who radioed earlier, approaches and
          asks if he can check the trunk of the car. You agree and open the 
          trunk. A third police car arrives. You now think of something to say 
          when suddenly the second policeman shouted, “Get out of the car with 
          your hands up.” The first policeman who spoke to you, suddenly pulls 
          out his gun and point to you. What is happening? 
          
          Will you be able to talk out the policemen about the real situation?
          """)
    input("""
          <Press Enter to continue>          
          """)
    passcodedirt()
   
def passcodedirt():
    import random
    input("""
===============================================================================
    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

          Another game!
              
          Still having fun? I hope you are.
              
          This game is simple:

          You just need to guess a number.
          
          It is a number between 1 and 15. You have three chances.
          
          At the end of each guess, a hint of either higher or lower 
          will be shared.
              
          Good luck!
              
          <Press Enter to continue>
              """)

    guessesTaken = 0
    guess = 16

    passcode = random.randint(1,15)

    while guessesTaken < 3 and guess != passcode:

        guess = input(f"""
          Please enter number:
          Remember, it is between 1 and 15.
          You have {3 - guessesTaken} more chances.
              """)

        guessesTaken = guessesTaken + 1
    
        if guessesTaken == 3 and int(guess) != passcode:
            print(f"""
          Sorry! That is your third chance and your number is still wrong.
              
          The passcode is {passcode}.
                  """)
            policefail()

        elif int(guess) < passcode:

            print(f"""
          Sorry! Your passcode value is too low.
              
          You have made {guessesTaken} tries already.
               """)

        elif int(guess) > passcode:

            print(f"""
          Sorry! Your passcode value is too high.
              
          You have made {guessesTaken} tries already.
               """)
        elif int(guess) == passcode:
            input(f"""
          You got it!
                  
          {passcode} is the correct answer! You got it on your
                  """)
            if guessesTaken == 1:
                    print("""
            (     (    (    (                    (        )  
            )\ )  )\ ) )\ ) )\ )  *   )    *   ) )\ )  ( /(  
            (()/( (()/((()/((()/(` )  /(  ` )  /((()/(  )\()) 
            /(_)) /(_))/(_))/(_))( )(_))  ( )(_))/(_))((_)\  
            (_))_|(_)) (_)) (_)) (_(_())  (_(_())(_)) __ ((_) 
            | |_  |_ _|| _ \/ __||_   _|  |_   _|| _ \\ \ / / 
            | __|  | | |   /\__ \  | |      | |  |   / \ V /  
            |_|   |___||_|_\|___/  |_|      |_|  |_|_\  |_|   

          Your adventure continue!
          
          <Press Enter to continue>

    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
===============================================================================                                                              
                          """)
            elif guessesTaken == 2:
                    input("""
            (                  )      )  (              (        )  
            )\ )        (   ( /(   ( /(  )\ )     *   ) )\ )  ( /(  
            (()/( (      )\  )\())  )\())(()/(   ` )  /((()/(  )\()) 
            /(_)))\   (((_)((_)\  ((_)\  /(_))   ( )(_))/(_))((_)\  
            (_)) ((_)  )\___  ((_)  _((_)(_))_   (_(_())(_)) __ ((_) 
            / __|| __|((/ __|/ _ \ | \| | |   \  |_   _|| _ \\ \ / / 
            \__ \| _|  | (__| (_) || .` | | |) |   | |  |   / \ V /  
            |___/|___|  \___|\___/ |_|\_| |___/    |_|  |_|_\  |_|  
        
          Your adventure continues!
          
          <Press Enter to continue>

    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
===============================================================================
                          """)
            else:
                    print("""
                      )  (    (    (              (        )  
            *   )  ( /(  )\ ) )\ ) )\ )     *   ) )\ )  ( /(  
            ` )  /(  )\())(()/((()/((()/(   ` )  /((()/(  )\()) 
            ( )(_))((_)\  /(_))/(_))/(_))   ( )(_))/(_))((_)\  
            (_(_())  _((_)(_)) (_)) (_))_   (_(_())(_)) __ ((_) 
            |_   _| | || ||_ _|| _ \ |   \  |_   _|| _ \\ \ / / 
              | |   | __ | | | |   / | |) |   | |  |   / \ V /  
              |_|   |_||_||___||_|_\ |___/    |_|  |_|_\  |_| 
          
          Your adventure continues!
          
          <Press Enter to continue>

    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
===============================================================================
                          """)
            policesuccess()

def policefail():
    print("""
          You failed to convince them. The four other policemen are approaching
          you very fast. A third one opens your door then a fourth pulls you
          out of the car. You tried to fight back but he slams you to the car 
          facing towards it. You hear metal clashing and is attach to your hand
          – you’re handcuffed. He is now stating your Miranda rights. You look 
          towards the direction of the trunk that was opened by second police.
          There, on the road, dripping and is already creating a pool of red
          liquid - it is blood! You look up a little and saw a hand sticking 
          out pointing downward.
          """)
    fail()
    
def policesuccess():
    print("""
          You made it! You are able to convince the policeman.
          
          Then they receive a report that your friend's neighbor saw you help
          find the escaped criminal.
          
          You are good. An ambulance arrives and takes you in. You are going 
          to be safe now.
          """)
    success()
    
def jump():
    print("""
          You turn your back against him. Still feeling light headed, you 
          start to run away from him. It is dark, but you run passed this 
          place for hundreds of time. Your muscle memory is working 100%.
          Then you remember they lock the gates until 5 in the morning and
          you are pretty sure it not 5 in the morning yet.
          """)
    input("""
          <Press Enter to continue>
          """)
    print("""
          You reach the gate and jump over it. It was unsuccessful. You do
          not remember the gate to be that tall. You back track and tried 
          to gather momentum. You jump, and it failed again. You look back.
          You can see him coming. Walking towards you and seems to be 
          carrying something. You need to jump over successfully! 
          """)
    passcodegate()

def passcodegate():
    import random
    input(f"""
===============================================================================
    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

          Another game!
              
          Still having fun {player}? I hope you are.
              
          This game is simple:

          You just need to guess the passcode.
          It is a number between 1 and 20. You have three chances. 
          At the end of each guess, a hint of either higher or lower 
          will be shared.
              
          Good luck!
              
          <Press Enter to continue>
              """)

    guessesTaken = 0
    guess = 21

    passcode = random.randint(1,20)

    while guessesTaken < 3 and guess != passcode:

        guess = input(f"""
          Please enter passcode:
          Remember, it is between 1 and 20.
          You have {3 - guessesTaken} more chances.
              """)

        guessesTaken = guessesTaken + 1
    
        if guessesTaken == 3 and int(guess) != passcode:
            print(f"""
          Sorry! That is your third chance and your passcode is still wrong.
              
          The passcode is {passcode}.
                  """)
            gatefail()

        elif int(guess) < passcode:

            print(f"""
          Sorry! Your passcode value is too low.
              
          You have made {guessesTaken} tries already.
               """) 

        elif int(guess) > passcode:

            print(f"""
          Sorry! Your passcode value is too high.
              
          You have made {guessesTaken} tries already.
               """)
        elif int(guess) == passcode:
            print(f"""
          You got it!
                  
          {passcode} is the correct answer! You got it on your
                  """)
            if guessesTaken == 1:
                    print("""
            (     (    (    (                    (        )  
            )\ )  )\ ) )\ ) )\ )  *   )    *   ) )\ )  ( /(  
            (()/( (()/((()/((()/(` )  /(  ` )  /((()/(  )\()) 
            /(_)) /(_))/(_))/(_))( )(_))  ( )(_))/(_))((_)\  
            (_))_|(_)) (_)) (_)) (_(_())  (_(_())(_)) __ ((_) 
            | |_  |_ _|| _ \/ __||_   _|  |_   _|| _ \\ \ / / 
            | __|  | | |   /\__ \  | |      | |  |   / \ V /  
            |_|   |___||_|_\|___/  |_|      |_|  |_|_\  |_|   

          Your adventure continues!
          
          <Press Enter to continue>

    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
===============================================================================                                                  
                          """)
            elif guessesTaken == 2:
                    print("""
            (                  )      )  (              (        )  
            )\ )        (   ( /(   ( /(  )\ )     *   ) )\ )  ( /(  
            (()/( (      )\  )\())  )\())(()/(   ` )  /((()/(  )\()) 
            /(_)))\   (((_)((_)\  ((_)\  /(_))   ( )(_))/(_))((_)\  
            (_)) ((_)  )\___  ((_)  _((_)(_))_   (_(_())(_)) __ ((_) 
            / __|| __|((/ __|/ _ \ | \| | |   \  |_   _|| _ \\ \ / / 
            \__ \| _|  | (__| (_) || .` | | |) |   | |  |   / \ V /  
            |___/|___|  \___|\___/ |_|\_| |___/    |_|  |_|_\  |_|  

          Your adventure continues!
          
          <Press Enter to continue>

    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
===============================================================================
                          """)
            else:
                    print("""
                      )  (    (    (              (        )  
            *   )  ( /(  )\ ) )\ ) )\ )     *   ) )\ )  ( /(  
            ` )  /(  )\())(()/((()/((()/(   ` )  /((()/(  )\()) 
            ( )(_))((_)\  /(_))/(_))/(_))   ( )(_))/(_))((_)\  
            (_(_())  _((_)(_)) (_)) (_))_   (_(_())(_)) __ ((_) 
            |_   _| | || ||_ _|| _ \ |   \  |_   _|| _ \\ \ / / 
              | |   | __ | | | |   / | |) |   | |  |   / \ V /  
              |_|   |_||_||___||_|_\ |___/    |_|  |_|_\  |_|  

          Your adventure continues!
          
          <Press Enter to continue>

    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
===============================================================================
                          """)
            gatesuccess()

def gatefail():
    print("""
          You failed again. You try to back track once more, but he is already
          behind you. He grabs you by your neck with his strong hands and push
          you against the iron gate. This time he is not asking a question. You
          can see him sweating and blood vessels are bursting out his arms.
          Focused on what he is doing to you. You try kicking the iron gate,
          but you are too weak. This is the end, you thought. As you asphyxiate
          from last breath, you look up and see the moon turn red then black.
          """)
    input("""
          <Press Enter to continue>
          """)
    fail()

def gatesuccess():
    print("""
          You made it – jump up and pass the gate. You drop slamming your bloodied
          face and tired body to the ground. It is wet and muddy. It is the
          road that leads to your house. Then you hear sirens. You slowly hold 
          your head up trying to verify but the lights are blinding you. You 
          only see shadows from your half-open eyes.
          """)
    input("""
          <Press Enter to continue>
          """)
    print(f"""
          {player}!!!!
          {player}!!!!
          {player}!!!!
          We are cheering for you!
          
██╗   ██╗ ██████╗ ██╗   ██╗    ███╗   ███╗ █████╗ ██████╗ ███████╗    ██╗████████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██║╚══██╔══╝
 ╚████╔╝ ██║   ██║██║   ██║    ██╔████╔██║███████║██║  ██║█████╗      ██║   ██║   
  ╚██╔╝  ██║   ██║██║   ██║    ██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██║   ██║   
   ██║   ╚██████╔╝╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ██║   ██║   
   ╚═╝    ╚═════╝  ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═╝   ╚═╝   
                                                                                  
                ██╗  ██╗ ██████╗ ███╗   ███╗███████╗██╗                                       
                ██║  ██║██╔═══██╗████╗ ████║██╔════╝██║                                       
                ███████║██║   ██║██╔████╔██║█████╗  ██║                                       
                ██╔══██║██║   ██║██║╚██╔╝██║██╔══╝  ╚═╝                                       
                ██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗██╗                                       
                ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝          
          """)
    input("""
          <Press Enter to continue>
          """)
    success()

def success():
    input("""
 _________  ____  ____  ________       ________  ____  _____  ______    _  
|  _   _  ||_   ||   _||_   __  |     |_   __  ||_   \|_   _||_   _ `. | |
|_/ | | \_|  | |__| |    | |_ \_|       | |_ \_|  |   \ | |    | | `. \| |
    | |      |  __  |    |  _| _        |  _| _   | |\ \| |    | |  | || | 
   _| |_    _| |  | |_  _| |__/ |      _| |__/ | _| |_\   |_  _| |_.' /|_| 
  |_____|  |____||____||________|     |________||_____|\____||______.' (_) 
  
    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
===============================================================================
            """)
    print(f"""
          {player}! Thank you for playing "Choose your adventure" game!          

          I hope you had fun playing it! 
          """)
    ending()

def fail():
    print("""
          Beeep!
              """)
    input("""
          <Press Enter to continue>
              """)
    print("""
          You jumped on your chair. You find yourself sweating profusely. 
          It was just a dream. No, it was a nightmare. And a really bad one. 
          You thank your phone for the full-charged tone that woke you up. 
          You suddenly remember your report.
              """)
    input("""
          <Press Enter to continue>
              """)
    print("""
          You immediately check the time – 11:54PM. Five more minutes to 
          deadline. You turn your laptop on. But before you can successfully 
          enter your password, you feel dizzy. 
              
          “What is this?” you asked yourself. 
              
          You ate your dinner right? 
              
          Then you look at the water in your bottle – shaking
              """)
    input("""
          <Press Enter to continue>
              """)
    input("""
 _________  ____  ____  ________       ________  ____  _____  ______    _  
|  _   _  ||_   ||   _||_   __  |     |_   __  ||_   \|_   _||_   _ `. | |
|_/ | | \_|  | |__| |    | |_ \_|       | |_ \_|  |   \ | |    | | `. \| |
    | |      |  __  |    |  _| _        |  _| _   | |\ \| |    | |  | || | 
   _| |_    _| |  | |_  _| |__/ |      _| |__/ | _| |_\   |_  _| |_.' /|_| 
  |_____|  |____||____||________|     |________||_____|\____||______.' (_) 
  

    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
===============================================================================
            """)
    print(f"""
          {player}! Thank you for playing "Choose your adventure" game!          

          I hope you had fun playing it! 
          """)
    input("""
          <Press Enter to continue>
              """)
    
    ending()

def ending():
    print("""         
          This is the condensed version of an original fourteen-page story. 
          It will have at least fifteen conditional statements and loops.        
          
          But I have to cut short so it can be played within 5 minutes which
          I think there is still a route that will take you longer.
           
          I hope I will have time to create it before end of this year!
           
          Credits:
              To the author or authors of published Create Your Adventure Game
                  books, I do not recall your name or names but that help me
                  understand fully and immediately the concept;
              To the authors, Edward Stratemeyer, Franklin W. Dixon, and 
                  Carolyn Keene, without your books, I would not have been
                  opened to the world of detectives and mysteries back when I 
                  was a teenager;
              To our dungeon masters way back in high school, I would like to 
                  play the game again. Promise I do! PM me when is our next
                  adventure;
              To Professor Chase, my Python teacher in Hult International 
                  Business School San Francisco, your passion and vigor of 
                  making sure your students learn and enjoy Python is 
                  exceptional. You made Python palatable even to non-coding 
                  people like me, thank you;
              And to you! The adventure hero or heroine of every story, without
                  you, these efforts of creating the story, writing the codes, 
                  debugging it, would have gone to nothing. Thank you!
 
          @ All Rights Reserved!
          
          Please approach the auther for any bugs encounter during gameplay.
          Known bugs are currently being fixed or rootcaused.
          
          Disclaimer: The events, characters and firms depicted in the game are
          ficticious. Any similarity to actual persons, living or dead, or to 
          actual firms, is purely coincidental.
          
          Raymond Zano
          Author, developer, game designer
              """)
    exit()
        
game_start()
