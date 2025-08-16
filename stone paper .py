import random


print("Welcome to Stone-Paper-Scissors Game!🌟")
print("Choices: Stone, Paper, Scissors")

choices = ["stone", "paper", "scissors"]


while True:
    user_choice = input("Enter your choice (stone/paper/scissors or quit): ").lower()
    
    if user_choice == "quit":
        print("Thanks for playing! Goodbye👋🏻")
        break

   
    if user_choice not in choices:
        print("Invalid choice! Please choose stone, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice} ", end="")
    if user_choice == "stone":
        print("🪨")
    elif user_choice == "paper":
        print("📰")
    else:
        print("✂")

    print(f"Computer chose: {computer_choice} ", end="")
    if computer_choice == "stone":
        print("🪨")
    elif computer_choice == "paper":
        print("📰")
    else:
        print("✂")

    if user_choice == computer_choice:
        print("It's a tie! 🤝")
    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win! 🎉")
    
    else:
        print("computer wins this round 💻!!")

    print("." * 50)