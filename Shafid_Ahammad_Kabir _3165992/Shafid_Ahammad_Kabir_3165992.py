#importing random and time module
import random 
import time

# Define function to generate random number between 1 and 100
def generate_random_number():
     return random.randint(1,100) 

# Define function to play the game
def play_game():
     # Print welcome messages and instructions
    print("Hello Player")
    print("I have a number in my mind! Can you guess it? You have 30 seceonds to get it right")
    print("Try guessing a number between 1 and 100")
    # generate a random number
    secret_number = generate_random_number()
    # Intialising the number of guesses to 0
    num_guesses = 0
    # get the current time for the timer to start
    start_time = time.time()
    # Loop until the user guesses the correct number or runs ot of time 
    while True:
          #Get a guess from the user 
          guess = input("Start guessing (or press 'q' to quit):")
          # If user types 'q' then ends the game with the goodbye message
          if guess == 'q':
               print("Sad to see you leave! Bye!")
               return
          try:
               # To convert the user's guess to an integer
               guess = int(guess)
          except ValueError:
               # If the user didn't enter a number, asks them to try again
               print("Invalid input. Please enter a number or 'q' to quit.")
               continue
          # Increment the number of guesses
          num_guesses += 1
          # Gives feedback on the guess whether it is too low or high
          if guess < secret_number:
               print("Too low! Try again.")
          elif guess > secret_number:
               print("Too high! Try again.")
          else:
               # If the guess is correct, Gives the number of guesses and duration to complete
               end_time = time.time()
               duration = end_time - start_time
               if duration > 30:
                    print("Sorry,your time is up.")
               else:
                    print(f"Congratulations! You guessed the number in {num_guesses} guesses and {duration:.2f}seconds!")
               return
          # if the user has run out of time, Prints the failure message and ends the game
          end_time = time.time()
          duration = end_time - start_time
          if duration > 30:
               print("Sorry, your time is up")
               return
# Call the play_game function to start the game    
play_game()