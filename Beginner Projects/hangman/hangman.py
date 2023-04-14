import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word =random.choice(words)
        
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 7
    
    while len(word_letters) > 0 and lives> 0:
        print("you have",lives, "lives left and you have used these letters:','".join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print("Current word:"," ".join(word_list))
        
        user_letter = input("Guess a letter:").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            
            else:
                lives = lives -1
                print ("\nYour letter,",user_letter,"is not in the word.")
                
        elif user_letter in used_letters:
            print("You have already used that character before. Please, guess another letter:")
        else:
            print("Invalid Character!")
    if lives==0:
        print(lives_visual_dict[lives])
        print ("You lost! The word was",word)
    else:
        print("Congrats! You won!")
if __name__ == '__main__':
    hangman()
            
    
user_input = input("Type something:")  
print(user_input)  