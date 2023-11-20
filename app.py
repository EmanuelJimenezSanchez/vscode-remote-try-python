#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random
import sys
import time

from flask import Flask
app = Flask(__name__)

options = ["Rock", "Paper", "Scissors"]

#Create a rock, paper, scissors game that takes user input and plays against the computer (randomly generated) and outputs the result to the console (win, lose, tie) and the user's score. The player should be able to choose between play again or not after each round. The game should end when the player chooses not to play again or when the player quits the game. The player's score should be displayed at the end of the game.
#The game should be able to handle invalid input and prompt the user to enter a valid input. The game should also be able to handle invalid input for play again and prompt the user to enter a valid input.
def rps():
    print("Welcome to Rock, Paper, Scissors!")
    print("Please enter your name:")
    name = input()
    print("Hello " + name + "!")
    print("Would you like to play a game of Rock, Paper, Scissors?")
    validarSiNo()

def play():
    print("Great!")
    print("Please enter your choice:")
    choice = validarOpciones()
    while(choice == ""):
        choice = validarOpciones()
    print("Now it's my turn!")
    print("Rock, Paper, Scissors, Shoot!")
    computer_choice = random.choice(options)
    print("I chose " + computer_choice + "!")
    if choice == "Rock" and computer_choice == "Rock":
        print("It's a tie!")
    elif choice == "Rock" and computer_choice == "Paper":
        print("I win!")
    elif choice == "Rock" and computer_choice == "Scissors":
        print("You win!")
    elif choice == "Paper" and computer_choice == "Rock":
        print("You win!")
    elif choice == "Paper" and computer_choice == "Paper":
        print("It's a tie!")
    elif choice == "Paper" and computer_choice == "Scissors":
        print("I win!")
    elif choice == "Scissors" and computer_choice == "Rock":
        print("I win!")
    elif choice == "Scissors" and computer_choice == "Paper":
        print("You win!")
    elif choice == "Scissors" and computer_choice == "Scissors":
        print("It's a tie!")
    print("Would you like to play again?")
    print("Please enter yes or no:")
    play_again = input()
    if play_again == "yes":
        play()
    elif play_again == "no":
        print("Thanks for playing!")
        sys.exit()


def validarSiNo():
    print("Please enter yes or no:")
    answer = input()
    if answer == "yes":
        play()
    elif answer == "no":
        print("Okay, maybe next time!")
        sys.exit()
    else:
        print("Invalid option:")
        validarSiNo()

def validarOpciones():
    print("Rock, Paper, or Scissors?")
    choice = input()
    if choice in options:
        print("You chose " + choice + "!")
        print(choice)
        return choice
    else:
        print("Invalid option:")
        choice = ""
        return choice


rps() #Call the function to start the game