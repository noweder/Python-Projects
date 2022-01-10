import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice == 0:
  player_selection = rock
  print(player_selection)
if choice == 1:
  player_selection = paper
  print(player_selection)
if choice == 2:
  player_selection = scissors
  print(player_selection)


if 0 <= choice <= 2:

  computer_selection = random.choice(options)
  print("Computer chose:\n" + computer_selection)

  if player_selection == rock:
    if computer_selection == rock:
      print("Draw!")
    elif computer_selection == paper:
      print("You lose!")
    elif computer_selection == scissors:
      print("You win!")

  elif player_selection == paper:
    if computer_selection == rock:
      print("You win!")
    elif computer_selection == paper:
      print("Draw!")
    elif computer_selection == scissors:
      print("You lose!")

  elif player_selection == scissors:
    if computer_selection == rock:
      print("You lose!")
    elif computer_selection == paper:
      print("You win!")
    elif computer_selection == scissors:
      print("Draw!")

else:
  print("Wrong selection! Please select 0, 1, or 2 only!")