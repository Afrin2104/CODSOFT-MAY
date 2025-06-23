import random

user = input("Choose rock, paper or scissors: ").lower()
computer = random.choice(["rock", "paper", "scissors"])
print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")
