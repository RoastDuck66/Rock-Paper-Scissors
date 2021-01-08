"""
ROCK PAPER SCISSORS
A Python Project by Nick N.
01/08/2021
"""
import random
from datetime import datetime

def computeRPS():
    # Generate random number:
    resultNumber = random.randint(1, 3)
    if resultNumber == 1: # 1 is Rock
        print("The AI chose ROCK (r)")
        return "r"
    elif resultNumber == 2: # 2 is Paper
        print("The AI chose PAPER (p)")
        return "p"
    elif resultNumber == 3: # 3 is Scissors
        print("The AI chose SCISSORS (s)")
        return "s"
    else:
        print("ERROR: resultNumber is invalid") # Error catch

def didPlayerWin(userMove, aiMove):
    if (userMove == aiMove): # If equal matches, it was a tie
        print("Tie detected!")
        return False
    elif ((userMove == "r" and aiMove == "s") or (userMove == "p" and aiMove == "r") or (userMove == "s" and aiMove == "p")):
        return True # Return True if ai is defeated
    else:
        return False # Return False if player is defeated


# Main Function:
if __name__ == "__main__":
    # Seed random number generator:
    random.seed(datetime.now())
    # Create a list of what inputs are valid for this program's prompt:
    acceptableInputs = ["r", "p", "s", "q"]
    # Initialize main function variables:
    aiDecision = ""
    gameLoop = True
    playerWon = False
    userScore = 0
    # Main Game Loop:
    while gameLoop:
        print("**************************")
        userInput = ""
        # Input until user inputs a r, p, or s, or wants to quit:
        while userInput not in acceptableInputs:
            userInput = input("Rock (r), Paper (p), or Scissors (s) (or q to Quit)?")
        # If input is to quit, then break from the loop:
        if userInput == acceptableInputs[-1]:
            break
        # Compute AI Decision:
        aiDecision = computeRPS()
        # Decide if player won or not:
        playerWon = didPlayerWin(userInput, aiDecision)
        if playerWon == True:
            # Award points if player won:
            userScore += 1
            print("Nice, you won! One more point for you!")
        else:
            # Lost game message:
            print("Better luck next round!")
        # Output score:
        print("Score so far: {}".format(userScore))
        # Prompt player if they want to play again:
        playAgain = input("Hit y to play again, else to quit:")
        if playAgain == "y":
            # If yes, restart game loop:
            continue
        else:
            # Otherwise, end program:
            print("I'll take that as a no. Bye.")
            break