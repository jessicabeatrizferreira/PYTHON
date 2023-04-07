import random

user = 0
computer = 0
tie = 0

options = ["rock", "paper","scissors"]

while True:
    user_input = input("Type rock, paper or scissors or Q to quit: ").lower()
    if user_input =='q':
       break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    #rock =0, paper=1, scissors=2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input =="rock" and computer_pick =="scissors":
        print("You won!")
        user =+1
    
    elif user_input =="scissors" and computer_pick =="paper":
        print("You won!")
        user =+1
       
    elif user_input =="paper" and computer_pick =="rock":
        print("You won!")
        user =+1
        
    elif user_input =="paper" and computer_pick =="paper":
        print("It's a tie!")
        tie =+1
        
    elif user_input =="rock" and computer_pick =="rock":
        print("It's a tie!")
        tie =+1
        
    elif user_input =="scissors" and computer_pick =="scissors":
        print("It's a tie!")
        tie =+1
        
    elif user_input =="scissors" and computer_pick =="rock":
        print("You lost!")
        computer =+1
        
    elif user_input =="paper" and computer_pick =="scissors":
        print("You lost!")
        computer =+1
        
    elif user_input =="rock" and computer_pick =="paper":
        print("You lost!")
        computer =+1
        