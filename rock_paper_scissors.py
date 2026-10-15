# Rock-Paper-Scissors Game
# The player plays 5 rounds against the computer.
# Rock breaks Scissors, Scissors cut Paper, Paper covers Rock.

import random  # lets the computer pick a random choice

# Score and round counters
player_score = 0
computer_score = 0
tie = 0
rounds = 0

# Play until 5 valid rounds are finished
while rounds < 5:

  # Take the player's choice; .lower() makes "ROCK" and "Rock" work too
  player_choice = input("Choose any one of the options: rock/paper/scissors: ").lower()

  # The computer picks one option randomly
  computer_choice = random.choice(["rock", "paper", "scissors"])

  # The list of valid options, used to check the player's input
  choices = ["rock", "paper", "scissors"]

  # If the player typed something else, show a message and ask again.
  # continue skips the rest, so no round is used and no point is given.
  if player_choice not in choices:
    print("Invalid choice, try again")
    continue

  # Only valid choices reach here, so count this round
  rounds = rounds + 1

  # Same choice by both: it's a tie
  if player_choice == computer_choice:
    tie += 1
    print("Tie")

  # Cases where the computer wins
  elif player_choice == "rock" and computer_choice == "paper":
    computer_score += 1
    print("Paper covers rock...computer wins!!!")
  elif player_choice == "paper" and computer_choice == "scissors":
    computer_score += 1
    print("Scissors cuts the paper...computer wins!!!")
  elif player_choice == "scissors" and computer_choice == "rock":
    computer_score += 1
    print("Rock breaks the Scissors... computer wins!!!")

  # Cases where the player wins
  elif player_choice == "scissors" and computer_choice == "paper":
    player_score += 1
    print("Scissors cuts the paper...player wins!!!")
  elif player_choice == "paper" and computer_choice == "rock":
    player_score += 1
    print("Paper covers rock...player wins!!!")

  # The only case left is rock vs scissors, so the player wins
  else:
    player_score += 1
    print("Rock breaks the Scissors... player wins!!!")

# After 5 rounds, compare the scores to decide the final result
if player_score > computer_score:
  print("You won")
elif player_score < computer_score:
  print("You lost")
else:
  print("Match draw")

# Show the final scores
print("Player:", player_score, "Computer:", computer_score)
