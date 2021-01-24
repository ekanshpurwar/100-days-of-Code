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
import random

user_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_chose>2:
    print("Enter valid choice")
    exit(-1)
list_choice = [rock, paper, scissors]
comp_chose = random.choice(list_choice)
if (user_chose == 0 and comp_chose == paper):
    print(rock)
    print("Computer chose:")
    print(comp_chose)
    print("You lose")
elif user_chose == 1 and comp_chose == scissors:
    print(paper)
    print("Computer chose:")
    print(comp_chose)
    print("You lose")
elif user_chose == 2 and comp_chose == rock:
    print(scissors)
    print("Computer chose:")
    print(comp_chose)
    print("You lose")
elif list_choice[user_chose] == comp_chose:
    print(list_choice[user_chose])
    print("Computer chose:")
    print(comp_chose)
    print("Draw")
else:
    print(list_choice[user_chose])
    print("Computer chose:")
    print(comp_chose)
    print("You won")

