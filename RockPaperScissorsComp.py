import random

loop = True
result = 0
playerScore = 0
compScore = 0
moves = ["rock","paper","scissors"]

def checkChoice(playerChoice,compChoice):
    global result,playerScore,compScore
    if playerChoice == compChoice:
        result = "Draw"
    if playerChoice=="rock" and compChoice=="scissors":
        result = "Player Wins"
        playerScore += 1
    if playerChoice=="rock" and compChoice=="paper":
        result = "Computer Wins"
        compScore += 1
    if playerChoice=="paper" and compChoice=="scissors":
        result = "Computer Wins"
        compScore += 1
    if playerChoice=="paper" and compChoice=="rock":
        result = "Player Wins"
        playerScore += 1
    if playerChoice=="scissors" and compChoice=="rock":
        result = "Computer Wins"
        compScore += 1
    if playerChoice=="scissors" and compChoice=="paper":
        result = "Player Wins"
        playerScore += 1

while loop == True:
    print("Player Score: ", playerScore)
    print("Computer Score: ", compScore)
    print("\n")
    playerChoice = (input("Choose Rock, Paper or Scissors \n")).lower()
    compChoice = random.choice(moves)
    print("\n")
    checkChoice(playerChoice,compChoice)
    print("Player went ", playerChoice)
    print("Computer went ", compChoice)
    print("\n")
    print(result)
    print("\n")