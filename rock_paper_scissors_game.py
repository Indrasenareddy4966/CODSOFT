import random 
choices = ["Rock","Paper","Scissors"]
user_choice = input("Choose rock,paper, or scissors:")
computer_choice = random.choice(choices)
winner = None 
if user_choice == computer_choice:
    winner = "Tie"
elif user_choice == "Rock" and computer_choice == "Scissors":
    winner= "User"
elif user_choice == "Paper" and computer_choice == "Rock":
    winner = "User"
elif user_choice == "Scissor" and computer_choice == "Paper": 
    winner = "User"
else: 
    winner = "Computer"
print(f"You chose {user_choice} and the computer chose {computer_choice}.")
if winner == "Tie":
    print("It's aa tie!")
else:
    print(f"{winner} wins!")
play_again = input("Do you want to play again? (y/n)")
if play_again == "y":
    user_choice = None 
    computer_choice = None 
    winner = None 
else: 
    print("Thanks for playing!") 
