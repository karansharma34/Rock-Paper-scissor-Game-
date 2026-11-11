'''
workflow of project:
1. input form user(rock,paper,scissors)
2. generate random choice for computer
3. compare choices and determine winner
4. display result

case:
1.rock
rock - rock = tie
rock - paper = paper wins
rock - scissor = rock wins

2.paper
paper - paper = tie
paper - rock = paper wins
paper - scissor = scissor wins

3.scissor 
scissor - scissor = tie
scissor - rock = rock wins
scissor - paper = scissor wins

'''

import random
choices = ["rock", "paper", "scissors"]

user_choice = input("enter your choice = rock, paper, scissor=")
computer_choice = random.choice(choices)
print(f"user_choice: {user_choice}, computer_choice: {computer_choice}")

if user_choice == computer_choice:
    print("tie")
    
elif user_choice == "rock":
    if computer_choice == "paper":
        print("paper wins")
    else:
        print("rock smashes scissor = rock wins")
    
elif user_choice == "paper":
    if computer_choice == "scissor":
        print("scissor wins")
    else:
        print("paper covers rock = paper wins")
        
elif user_choice == "scissor":
    if computer_choice == "rock":
        print("rock wins")
    else:
        print("scissor cuts paper = scissor wins")
    








