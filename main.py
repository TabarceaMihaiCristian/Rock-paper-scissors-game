# Rock, paper, scissors game

import random
import time

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
round_count = 1

while True:
    computer = random.choice(choices)
    player = None
    time.sleep(0.5)
    print("Round" + str(round_count) + "\n")
    while player not in choices:
        player = input("rock, paper or scissors?:").lower()
    time.sleep(0.8)
    for i in range(3, 0, -1):
        print(i)
        time.sleep(0.8)

    if player == computer:
        print('Computer chose:', computer)
        print('You chose:', player)
        time.sleep(0.8)
        print("It's a tie!")
        time.sleep(0.8)
        print("The score is still: " + str(player_score) + " - " + str(computer_score))
    elif player == "scissors":
        if computer == "rock":
            print('Computer chose:', computer)
            print('You chose:', player)
            time.sleep(0.8)
            print("You lose! :(")
            time.sleep(0.8)
            computer_score += 1
            print("The score is: " + str(player_score) + " - " + str(computer_score))
        elif computer == "paper":
            print('Computer chose:', computer)
            print('You chose:', player)
            time.sleep(0.8)
            print("Congrats! You won!")
            time.sleep(0.8)
            player_score += 1
            print("The score is: " + str(player_score) + " - " + str(computer_score))
    elif player == "rock":
        if computer == "paper":
            print('Computer chose:', computer)
            print('You chose:', player)
            time.sleep(0.8)
            print("You lose! :(")
            time.sleep(0.8)
            computer_score += 1
            print("The score is: " + str(player_score) + " - " + str(computer_score))
        elif computer == "scissors":
            print('Computer chose:', computer)
            print('You chose:', player)
            time.sleep(0.8)
            print("Congrats! You won!")
            time.sleep(0.8)
            player_score += 1
            print("The score is: " + str(player_score) + " - " + str(computer_score))
    elif player == "paper":
        if computer == "scissors":
            print('Computer chose:', computer)
            print('You chose:', player)
            time.sleep(0.8)
            print("You lose! :(")
            time.sleep(0.8)
            computer_score += 1
            print("The score is: " + str(player_score) + " - " + str(computer_score))
        elif computer == "rock":
            print('Computer chose:', computer)
            print('You chose:', player)
            time.sleep(0.8)
            print("Congrats! You won!")
            time.sleep(0.8)
            player_score += 1
            print("The score is: " + str(player_score) + " - " + str(computer_score))

    # if player_score % 5 == 0 and player_score > computer_score:
        # print("Great job! You are leading!")
    # elif computer_score % 5 == 0 and player_score < computer_score:
        # print("Oh no! The computer is leading!")
    round_count += 1
    time.sleep(0.8)
    answer = input("Do you want to play again?: (Yes/No)").lower()
    if answer != "yes":
        break
    else:
        print("\n")
time.sleep(0.7)
print("Thanks for playing! See you next time!")
time.sleep(1.5)
