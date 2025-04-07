# Problem: High Low
# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

# We've provided a sample run below.


#Solution


import random

NUM_ROUNDS = 3


def game():
     # Milestone 5: keep track of your score
    SCORE = 0


    print("Welcome to the High-Low Game!")

     # Milestone 4: Play multiple rounds
    for round_num in range(NUM_ROUNDS):
       
        # Milestone 1: Generate the random numbers and print them out
       computer = random.randint(0 , 99)
       user = random.randint(0 , 99)
    #    round_num  = round_num + 1lower
       print( "\nRound" , round_num + 1)
       print("Your random number is" , user)

         # Extension 1: Make sure the player inputs a valid choice (higher or lower)
       user_input = input("Do you think your number is higher or lower than the computer's?:").lower().strip()

         # Milestone 3: Map out all the ways to win the round
       if user_input == "higher" :
            if user > computer :
                print("✅ You were right! The computer's number was " , computer)
                 #Milestone 5: keep track of  score
                SCORE += 1
            else:
                print("❌ Aww, that's incorrect. The computer's number was " , computer)

       elif user_input == "lower":
            if user < computer :
                print("✅You were right! The computer's number was " , computer)
                # Milestone 5: keep track of  score
                SCORE += 1
            else:
                print("❌ Aww, that's incorrect. The computer's number was " , computer)

       else:
          print("⚠️ Invalid input! Please enter 'higher' or 'lower'.")      

    # Milestone 5: keep track of your score

       print("Your score is:" , SCORE)       
  
      # Extension 2: Conditional ending messages based on performance    
    print("Game over. Your Total score is :" , SCORE)    

    if SCORE == 3:
        print("Wow! You played perfectly!")
    elif SCORE == 2:
        print("Good job, you played really well!")    
    else:
        print("Better luck next time")        
              
                  

if __name__ == "__main__":
    game()          