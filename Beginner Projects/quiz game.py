print("Welcome to my computer game!")
      
playing = input("Do you wan to play the game? ")

if playing.lower() != "yes":
    quit()
    
print("Let's play!")
score = 0

answer = input("What does the CPU stand for? ")
if answer.lower() =="central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
answer = input("What does the GPU stand for? ")
if answer.lower() =="graphics processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() =="random access memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
answer = input("What does the PSU stand for? ")
if answer.lower() =="power supply":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
print("You go "+str(score)+" questions correct!")
print("You go "+str((score / 4 * 100))+" %")
