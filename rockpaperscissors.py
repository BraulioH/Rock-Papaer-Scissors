import random
def playGame():
  randomizeChoice = random.choice(computer)
  player = None
  player = input("Rock, paper, or scissors?").lower
  print("Computer: ", computer)
  print("You: ", player)
  while player not in options:
    player = input("Rock, paper, or scissors?").lower
  if player == computer:
    print ("Computer: ", computer)
    print ("Player: ", player)
    print("It's a tie!!")
    