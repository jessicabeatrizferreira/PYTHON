import random

top_range = input("Type a number: ") // o usuario entra com um valor maximo

if top_range.isdigit():
    top_range = int(top_range)
    
    if top_range <= 0:
        print("Please type a number larger than 0 next time:")
        quit()
        
else:
    print("PLease, type a number ")
    quit()
    
randon_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses +=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time: ")
        continue
    
    if user_guess == randon_number:
        print("You got it!")
        break
    elif user_guess >randon_number:
        print("You were above the number!")
    else:
        print("You were below the number!")
            
print("You got it in",guesses, "guesses!")