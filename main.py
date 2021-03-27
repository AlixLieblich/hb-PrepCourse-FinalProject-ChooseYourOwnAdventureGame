# author: Alix Lieblich

import time
import random

def chooseAdventure():
    ### function to create a game
  import time
  print()
  print("Narrator: From a deep sleep, you become aware of a sensation on your face...")
  time.sleep(1)
  print()
  print("Drip...")
  time.sleep(1)
  print()
  print("Drip...")
  time.sleep(1)
  print()
  print("Drip.....")
  time.sleep(1)
  print()
  print("-----------------")
  time.sleep(1)
  print()
  print("Narrator: You sit up and look around, wiping the cold water from your face.")
  time.sleep(1)
  print()
  print("Me: Where am I?")
  time.sleep(1)
  print()
  print("Narrator: You look around, and find that you are in a cave.")
  time.sleep(1)
  print()
  print("Me: Who am I?")
  time.sleep(1)
  print()
  print("Me: What is going on???")
  time.sleep(1)
  print()
  print("-----------------")
  time.sleep(1)
  print()
  print("Narrator: You find that you are tired, scared and cold, and have no clue who you are or how you came to be here.")
  time.sleep(2)
  print()
  choice = ("OPTION: Do you BEGIN the journey to find out who you are, or do you CURL up in a ball on the floor?")
  print(choice)
  option = input("> ")
  option = option.upper()
  notebook=[]
  while True:
    if option == "NOTEBOOK":
      print("Pocket Sized Spiral Bound Notebook")
      print("-----------------")
      while True:
        print("You can ADD / VIEW / CLOSE notebook.")
        option = input("> ")
        option = option.upper()
        if option == "CLOSE":
          print("Narrator: You close your notebook and stash it in your pocket.")
          print(choice)
          option = input("> ")
          option = option.upper()
          break
        if option == "ADD":
          print("Narrator: What observation would you like to add to your notebook?")
          obser = input("> ")
          notebook.append(obser)
          print(f"You added: {obser}")
        if option == "VIEW":
          print("My Observations:")
          for observations in notebook:
            print(observations)
    elif option == "GO BACK":
      print("Narrator: You've decided to go back to the cave you originally found yourself in.")
      time.sleep(1)
      choice = ("OPTION: You now have the option to EXIT the cave or EXPLORE the tunnel from the cave.")
      print(choice)
      option=input("> ")
      option=option.upper()
    elif option == "BEGIN":
      print()
      print("Narrator: You decide to explore the cave that you find yourself in.")
      print("You find a puddle and see your appearance.")
      time.sleep(1)
      print()
      print("What color is your hair?")
      hair=input("> ")
      print()
      print("What color are your eyes?")
      eyes=input("> ")
      print()
      print(f"Narrator: You have {hair} colored hair and {eyes} eyes. You also notice that your ears are elongated. These appearance traits seem to tigger something in your memory. Focus, what do you remember?")
      time.sleep(1)
      print("...")
      print()
      print("Me: I... remember... red rocks.")
      time.sleep(1)
      print()
      print("Narrator: Interesting, a clue to your past.")
      time.sleep(1)
      print()
      print("Narrator: You look through your pockets and find a granola bar, which you eat, and a pocket sized spiral bound notebook. You decide to write down all the clues to who you are in order to keep track of them.")
      time.sleep(2)
      print()
      print("Narrator: To access your notebook at any point to view or add observations, type NOTEBOOK. You can now add the observations about your appearance and the memory they triggered.")
      print()
      print("OPTION: You find a mouth to exit the cave, but you also find a tunnel that goes deeper, lit with gas lamps. You know have the choice to EXIT, EXPLORE, or add clues to your NOTEBOOK.")
      choice = ("OPTION: Would you like to EXIT, EXPLORE, or add clues to your NOTEBOOK?")
      option = input("> ")
      option = option.upper()
    elif option == "EXPLORE":
      print()
      print("Narrator: You walk down the cold, dank tunnel lit with an eerie yellow light from the gas lamps for what feels like multiple hours. Finally, you come to a fork in the tunnel. To the left seems you see a vauge light, possibly sunlight, another exit of the tunnel.")
      time.sleep(1)
      print()
      print("Narrator: To the right, however, you hear faint sounds, like a conversation. You also smell food, strange cuisine you can't remember from your life before. Your stomach grumbles; you are weak with hunger. A small part of you wonders if both options feel wrong in your gut, and you think turning around and back tracking the tunnel might be a good idea, too.")
      time.sleep(3)
      print()
      choice = ("OPTION: Do you choose to go to the LEFT, RIGHT, or GO BACK? >")
      print(choice)
      option=input("> ")
      option=option.upper()
    elif option == "LEFT":
      print()
      print("Narrator: You walk a short distance until you find yourself at a crack in the wall of the tunnel. You are hundreds of feet from the ground, high above the wilderness.")
      time.sleep(2)
      print()
      print("Me: That fresh air ... I feel like it should be relieving after the cave .. and yet...")
      time.sleep(1)
      print()
      print("Narrator: Perhaps another clue, you seem to prefer indoor spaces to those wide open.")
      time.sleep(1)
      print()
      print("Narrator: There are no answers here, so you turn around and head back to the fork in the tunnel.")
      time.sleep(1)
      print()
      choice = ("OPTION: Do you go to the RIGHT, towards the unfamiliar sound of others and smell of food? Or would you like to GO BACK to the original mouth of the cave?")
      print(choice)
      option = input("> ")
      option = option.upper()
      print("-----------------")
    elif option == "RIGHT":
      print()
      print("Narrator: You feel nervous as you head down the tunnel towards the smells and sounds. Eventually, you come around a bend and see two individuals sitting around a small camp fire with a pot hanging over it, a wide opening in the tunnel behind them allows you a view of a land surrounded with beautiful snow capped mountains, sunny, plush green valleys below.")
      time.sleep(1)
      print()
      print("Narrator: The two individuals become rigid with your presence, and stand up, instantly arming themselves with short swords. As they stand, you realize they both must be nearly six and a half feet tall. You are about the same height. The male on the right has dark hair, and a stunningly beautiful face, with almost unnervingly feline features, then you notice a black and white cat tail sweeping behind him. Your eyes dart to the female beside him, her hair flaming red and her features foxy, to match her fluffy tail.")
      time.sleep(2)
      print()
      print("Narrator: You feel a power radiate off of them, a scary, primal feeling.")
      time.sleep(1)
      print()
      choice = ("OPTION: You can SPEAK with them, or run for your life and GO BACK the way you came.")
      print(choice)
      option = input("> ")
      option = option.upper()
    elif option == "SPEAK":
      print()
      print("ME: Wh-who are you?")
      time.sleep(1)
      print()
      print("Narrator: The female speaks first, turning her head to get a better view of you.")
      print()
      print("Lucine: My name is Lucine.")
      print()
      print("Felix: And I am Felix. Who are you? How did you find the entrance to the Fae Land?")
      print()
      choice = ("OPTION: Would you like to respond ONE: 'I don't know who I am. I just woke in this tunnel. I'm trying to figure out who I am.' Or TWO: 'Who are YOU? Or, WHAT are you? What is the land of the Fae?'")
      print(choice)
      option = input("> ")
      option = option.upper()
    elif option == "ONE":
      print()
      print("Me: I don't know who I am. I just woke in this tunnel. I'm trying to figure out who I am.")
      time.sleep(1)
      print()
      print("Felix: Good news, we can help you with that.")
      time.sleep(1)
      print()
      print("Narrator: You are nervous at the hungry in Felix's eyes, in both of their eyes, you realize as you look at Lucine.")
      time.sleep(1)
      print()
      print("Me: How?")
      time.sleep(1)
      print()
      print("Lucine: We have a little test we can conduct, to see if your one of us.")
      time.sleep(1)
      print()
      print("Me: And what if I take this test, and I'm not one of you?")
      time.sleep(1)
      print()
      print("Felix: We'll let you turn around right now.")
      time.sleep(1)
      print()
      print("Narrator: The pair do not seem to be trustworthy, and you don't know what the consequences of failing their test is. And yet you have elongated ears, perhaps less pointed than their ears, and you're all fairly tall. Maybe this is the answer, maybe you're one of them and there is only one way to find out.")
      print()
      choice = ("OPTION: Do you take the TEST or do you GO BACK the way you came?")
      print(choice)
      option = input("> ")
      option = option.upper()
    elif option == "TEST":
      questions = [
      "Do you feel most alive during dawn, day, twilight, or night?",
      "How quickly do you wounds heal?",
      "How easily do you find telling lies?"
    ]
      answers=[
      "a",
      "b",
      "c"
    ]
      def check_answer():
        ## function to make a small questionaire and grade the responses
        result=0
        j = 0
        for i in questions:
          print(i)
          answer=input("> ")
          if answer == answers[j]:
            result+=1
            print(result)
          j+=1
        return result
      def play():
        i=0
        while i < 1:
          answers_correct=check_answer()
          if answers_correct > 1:
            print("Felix: You should have turned back when we gave you the chance. But unfortunatey, you did not. And now you have failed the test. You are not a Faerie. Our's is not the past you do not remember.")
            time.sleep(1)
            print()
            print("Me: Unfor-unfortunate how ... ?")
            time.sleep(1)
            print()
            print("Narrator: You look desperatley back and forth between the two; Felix, staring intently at you, and Lucine ideally cleaning her nails with the tip of her short sword. She looks up slowly at you, and you feel your blood cool, and continue to freeze. Pain courses through you as cold reaches your heart and you fall to your knees, your eyes locked on the cruel foxlike ones.")
            time.sleep(1)
            print()
            print("Lucine: We cannot let word of realm past this cave.")
            time.sleep(1)
            print()
            print(...)
            print("Narrator: You have failed to live long enough to regain your memories.")
            time.sleep(1)
            print()
            print("GAME OVER")

          i+=1
          break

      play()
      break
    elif option == "TWO":
      print()
      print("Me: Who are YOU? Or, WHAT are you? What is the land of the Fae?")
      time.sleep(1)
      print("Felix: The more you know, the more of a ... liability you are.")
      time.sleep(1)
      print()
      print("Me: So, I have to option to walk away right now?")
      time.sleep(1)
      print()
      print("Narrator: Lucine looks to be dissapointed by this thought, as she turns her head to the side to further assess you.")
      time.sleep(1)
      print()
      print("Lucine: What is it you wamt? That you seek?")
      time.sleep(1)
      print()
      print("Me: I don't know who I am. I just woke in this tunnel. I'm trying to figure out who I am.")
      time.sleep(1)
      print()
      print("Felix: Good news, we can help you with that.")
      time.sleep(1)
      print()
      print("Narrator: You are nervous at the hungry in Felix's eyes, in both of their eyes, you realize as you look at Lucine.")
      time.sleep(1)
      print()
      print("Me: How?")
      time.sleep(1)
      print()
      print("Lucine: We have a little test we can conduct, to see if your one of us.")
      time.sleep(1)
      print()
      print("Me: And what if I take this test, and I'm not one of you?")
      time.sleep(1)
      print()
      print("Felix: We'll let you turn around right now.")
      time.sleep(1)
      print()
      print("Narrator: The pair do not seem to be trustworthy, and you don't know what the consequences of failing their test is. And yet you have elongated ears, perhaps less pointed than their ears, and you're all fairly tall. Maybe this is the answer, maybe you're one of them and there is only one way to find out.")
      print()
      choice = ("OPTION: Do you take the TEST or do you GO BACK the way you came?")
      print(choice)
      option = input("> ")
      option = option.upper()
    elif option == "EXIT":
      print()
      print("Narrator: You exit the cave and walk for multiple miles until you begin to smell the ocean breeze in the air. You approach a sign which says, 'Welcome to the Silican Valley'.")
      time.sleep(1)
      print()
      print("Me: Hmmm, I don't remember why, but this place seems familiar.")
      time.sleep(1)
      print()
      print("Narrator: Another clue, perhaps you should add it to your notebook.")
      time.sleep(1)
      print()
      print("OPTION: You can now add to your NOTEBOOK, ENTER the Silicon Valley, to see why it feels familiar to you, or you can you can GO BACK to the cave.")
      print()
      choice = ("You can more add to your NOTEBOOK, ENTER the Silicon Valley, to see why it feels familiar to you, or you can you can GO BACK to the cave to explore the tunnel.")
      option=input("> ")
      option=option.upper()
      print()
      print("-----------------")
    elif option == "ENTER":
      print()
      print("Narrator: You enter the Silicon Valley and are completely taken by surprise when-")
      time.sleep(1)
      print()
      print("Random Bystander: OMG Elon Musk! Can I get a selfie with you?")
      time.sleep(1)
      print()
      print("Me: What? Who is Elon Musk?")
      time.sleep(1)
      print()
      print("Narrator: You grow more concerned and confused as more people around you seem to notice and recognize you and start to come over.")
      time.sleep(1)
      print()
      print("Random Bystander: Elon Musk? That is you, I know it is, I see you in the news all the time; you just passed Jeff Bezos as the richest man in the world!")
      time.sleep(1)
      print()
      print("Narrator: The bystander pulls up an article on his phone, showing you a photo of yourself as proof of who you are.")
      time.sleep(1)
      print()
      choice = ("OPTION: Your now have the choice to add an observation to your NOTEBOOK, or respond to the bystander FIRST: 'Well, that certainly seems to be me, doesn't it?'' Or SECOND: 'Since you know so much about me, could I give you a selfie and an autograph for you to call me an Uber to my company? That article says I work for Tesla.'")
      print(choice)
      option = input("> ")
      option = option.upper()
    elif option == "FIRST":
      print()
      print("Me: Well, that certainly seems to be me, doesn't it?")
      time.sleep(1)
      print()
      print("Random Bystander: Do you need help, sir? What if I call you an uber to your company in exchange for that selife and an autograph?")
      time.sleep(1)
      print()
      choice = ("OPTION: Access your NOTEBOOK, ACCEPT the bystander's offer, or GO BACK to the cave.")
      print(choice)
      option = input("> ")
      option = option.upper()
    elif option =="SECOND":
      print()
      print("Me: Since you know so much about me, could I give you a selfie and an autograph for you to call me an Uber to my company? That article says I work for Tesla.")
      time.sleep(1)
      print()
      print("Random Bystander: Sounds good to me!")
      option = "TESLA"
    elif option == "ACCEPT":
      print()
      print("Me: Sure, that sounds like a deal to me.")
      time.sleep(1)
      print()
      print("Random Bystander: Awesome!")
      option = "TESLA"
    elif option == "TESLA":
      print()
      print("-----------------")
      print()
      print("Narrator: You approach the big shiny Tesla buidling, and notice a Dragon X rocket in the back, preparing for lift off.")
      time.sleep(1)
      print()
      print("Me: Wait, I remember this, its launch day! Our rocket, the Dragon X, is taking the first passengers to Mars... and... and... I had wanted to fight my way onto that ship... I can't remember why I wanted to go to Mars so badly, though.")
      time.sleep(1)
      print()
      print("Narrator: Another clue as to who you are!")
      time.sleep(1)
      print()
      choice = ("OPTION: Access your NOTEBOOK, RUN to the launch to commandeer a seat on the rocket, or GO BACK to the cave.")
      print(choice)
      option = input("> ")
      option = option.upper()
      print()
      print("-----------------")
    elif option == "RUN":
      print()
      print("Narrator: You make the rash decision run to the rocket. At the divider between the crowd there to watch the launch and the rocket, you grab a gun from the holster of a police officer. You run to the hatch, and get cover as they start shooting. Gasps of surprise at your actions and screams of fear shoot through the crowd.")
      time.sleep(1)
      print()
      print("Narrator: It becomes clear you will have to shoot the three armed guards in order to gain access to Mars.")
      time.sleep(1)
      print()
      print("Me: I seem... to know... that I had wanted to go to Mars before, before I lost my memories...")
      time.sleep(1)
      print()
      choice = ("OPTION: Access your NOTEBOOK, run away and GO BACK to the cave, or SHOOT your way onto the rocket.")
      print(choice)
      option = input("> ")
      option = option.upper()
      print()
      print("-----------------")

    elif option == "SHOOT":
      import random
      guard = 3
      while guard > 0:
          input("Press RETURN to fire:")
          
          if random.randint(1, 2) == 1:
              print("You hit a guard!")
              guard -= 1
          else:
              print("You miss.")
          print(f"Guards left: {guard}")
          print()

      print("You win!")
      option = "ONBOARD"
    elif option == "ONBOARD":
      print()
      print("Narrator: You have some time before you arrive at Mars so you wander around the ship. You discover a computer with a Rock Paper Scissors game.")
      time.sleep(1)
      print()
      choice = ("OPTION: You can access your NOTEBOOK, sit back and relax until you ARRIVE, or you can PLAY Rock, Paper, Scissors.")
      print(choice)
      option = input("> ")
      option = option.upper()
    elif option == "PLAY":
      import random
      import time
      def rock_paper_scissors():
        player1_score = 0
        comp_score = 0
        while True:
          options =['Rock', 'Paper', 'Scissors']
          options2 = ['R', 'P', 'S']
          print("Choose your Champion: ROCK, PAPER, or SCISSORS")
          print("Type 'R' for Rock, 'P' for Paper, and 'S' for Scissors, or 'Q' to quit.")
          print()
          player1 = input("> ")
          player1 = player1.upper()
          if player1 not in options2:
            print("Please choose only ROCK, PAPER, or SCISSORS.")
          comp = random.choice(options)
          print()
          if player1 == "R":
            print("Your Champion: Rock")
            if comp == "Paper":
              print("Computer's Champion: Paper")
              print()
              time.sleep(0.5)
              print("Computer wins!")
              comp_score += 1
            if comp == "Scissors":
              print("Computer's Champion: Scissors")
              print()
              time.sleep(0.5)
              print("You win!")
              player1_score += 1
            if comp == "Rock":
              print("Computer's Champion: Rock")
              print()
              time.sleep(0.5)
              print("It's a tie.")
          if player1 == "P":
            print("Your Champion: Paper")
            if comp == "Paper":
              print("Computer's Champion: Paper")
              time.sleep(0.5)
              print()
              print("It's a tie.")
            if comp == "Scissors":
              print("Computer's Champion: Scissors")
              time.sleep(0.5)
              print()
              print("Computer wins!")
              comp_score += 1
            if comp == "Rock":
              print("Computer's Champion: Rock")
              time.sleep(0.5)
              print()
              print("You win!") 
              player1_score += 1
          if player1 == "S":
            print("Your Champion: Scissors")
            if comp == "Rock":
              print("Computer's Champion: Rock")
              time.sleep(0.5)
              print()
              print("Computer wins!")
              comp_score += 1
            if comp == "Paper":
              print("Computer's Champion: Paper")
              time.sleep(0.5)
              print()
              print("You win!")
              player1_score += 1
            if comp == "Scissors":
              print("Computer's Champion: Scissors")
              time.sleep(0.5)
              print()
              print("It's a tie.")
          print()
          print(f"Your overall wins: {player1_score}")
          print(f"Computer's overall wins: {comp_score}")
          print()
          if player1 == "Q":
            break

        print("Final Scores: ")
        print(f"You: {player1_score}")
        print(f"Computer: {comp_score}")
        if player1_score > comp_score:
          print("You are the Overall Champion!")
        if comp_score < player1_score:
          print("Computer is the Overall Champion!")
        else:
          print("You and computer tied for Overall Champion!")
        print("Thanks for playing!")
      rock_paper_scissors()
      time.sleep(1)
      print()
      choice = ("OPTION: You can PLAY Rock, Paper, Scissors again, or you can WAIT until you arrive.")
      print(choice)
      option = ("> ")
      option = option.upper()
    elif option == "WAIT":
      print()
      print("...")
      time.sleep(1)
      print()
      print("...")
      time.sleep(1)
      print()
      print("...")
      time.sleep(1)
      print()
      print("Narrator: Good news! Today is the day you land on Mars! It'll land on autopilot, so no need to worry.")
      time.sleep(1)
      print()
      print("Narrator: As you land, you go to the window and see ... Red Rocks! A whole city of buildings carved out of Red Rocks!")
      time.sleep(1)
      print()
      print("Me: I remember! The Red Rock City! That's what I had remembered!")
      time.sleep(1)
      print()
      print("Narrator: As the ship gets closer and closer to the surface of Mars, on course to land a safe distance from Red Rock City, you see the Green Martian People gathering with excitement to welcome you home.")
      time.sleep(1)
      print()
      print("Narrator: The rocket touches down. As the ship door opens, and your body adjusts to the Martian Atmosphere, you look down and see that your skin has greened to match those swarming around to welcome you home.")
      time.sleep(1)
      print()
      print("Random Martian 1: Welcome Home, Elon!")
      time.sleep(1)
      print()
      print("Random Martian 2: We missed you so much, Elon!")
      time.sleep(1)
      print()
      print("Narrator: The King and Queen of Mars materialize out of the crowd and approach.")
      time.sleep(1)
      print()
      print("King: Welcome home, son.")
      time.sleep(1)
      print()
      print("Queen: We missed you!")
      time.sleep(1)
      print()
      print("Me: I did it, I remember now, I'm Elon Musk, the Prince of Mars! I made it back, Mom and Dad, I became the richest man on Earth, engineered this rocket, then lost my memories, but I still made it home!")
      time.sleep(1)
      print()
      print("CONGRATULATIONS, YOU WIN!")
      break
    elif option =="CURL":
      print("Narrator: You have lost the will to rediscover yourself. This is the end of the line.")
      time.sleep(1)
      print("GAME OVER")
      option=option.upper()
      break
    else:
      if option != "begin":
        print("That is not one of your options.")
        print(choice)
        option = input("> ")
        option = option.upper()
    
    

chooseAdventure()

while True:
  print("would you like to play again?")
  playAgain= input("yes or no: ")
  playAgain = playAgain.upper()
  if playAgain == "YES":
    chooseAdventure()
  else:
    break