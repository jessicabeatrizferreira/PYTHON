# Guess the number (computer)
import random #importando a biblioteca random

def guess (x): #definindo a função
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < random_number: #se menor que o numero random
            print("Sorry! Guess again. Too low.")
        elif guess > random_number:  #se maior que o numero random
            print("Sorry! Guess again. Too high.")
            
    print(f"Yes! You did it! The random number is {random_number}!")
    
guess(10) #determina o o numero limite
    
        
    
