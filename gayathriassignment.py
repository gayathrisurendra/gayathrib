#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    number_of_attempts = 0
    guessed = False

    print("Welcome to 'Guess the Number' game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed:
        guess = input("Enter your guess: ")

        try:
            guess = int(guess)
            number_of_attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number in {number_of_attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if _name_ == "_main_":
    guess_the_number()

