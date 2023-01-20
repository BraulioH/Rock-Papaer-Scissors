import random
from main import choices
def win():
  print("Congradulations, you beat a computer.")
  
def lost():
  print("You lost to a computer smh")
  
def playGame(list):
  computer = ("rock", "paper", "scissors")
  randomizeChoice = random.choice(choices)
  player = None
  player = input("Rock, paper, or scissors?").lower
  print("Computer: ", computer)
  print("You: ", player)
  def results():
    print ("Computer: ", computer)
    print ("Player: ", player)  
  while player not in computer:
    player = input("Rock, paper, or scissors?").lower
  if player == computer:
    print(results)
    print("It's a tie!!")
    
  elif player == "rock":
    if computer == "paper":
      print(results)
      print(win)
    if computer == "scissors":
      print(results)
      print(lost)
      
  elif player == "paper":
    if computer == "scissors":
      print(results)
      print(win)
    if computer == "rock":
      print(results)
      print(lost)
      
  elif player == "scissors":
    if computer == "paper":
      print(results)
      print(win)
    if computer == "rock":
      print(results)
      print(lost)