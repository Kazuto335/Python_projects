import random
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print("\n\t\tWelcome To Rock-Paper-Scissors Game..!\n")
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

# Create Choices Globally
choices = ["Rock", "Paper", "Scissors"]
# Users input
player_choices = int(input('\n\tPress 0 for "Rock", 1 for "Paper", and 2 for "Scissors" : \n\t'))
if player_choices >= 3:
    print("\n \tYou select Wrong no. you loose")
else:
    print(f"\tSo you choose : \n    {choices[player_choices]} \n")
    # Random Choice Made By CPU
    random_int = random.randint(0, 2)
    print(f"\tComputer choose : \n    {choices[random_int]} \n")
    # Conditions start here :-
    if player_choices == 0 and random_int == 2 :
        print("\n   You win...!    \n")
    elif player_choices == 1 and random_int == 0 :
        print("\n   You win...!    \n")
    elif player_choices == 2 and random_int == 1 : 
        print("\n   You win...!    \n")
    elif random_int == player_choices:
        print("\tIt's a draw...!")
    else :
        print("\tYou Loose...!")
