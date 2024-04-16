print("Welcome to my computer quiz!")
print("Do you want to play ?")
playing = input("Yes or No : ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1


else:
    print("Incorrect!")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access unit":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("What does PSU stands for? ")
if answer == "power supply":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")


print("You got " + str(score) + " Questions Correct")
print("You got " + str((score / 4) * 100) + "%.")
