# Rock, Paper, Scissors, Lizard, Spock

from random import randint

print("Welcome to Rock, Paper, Scissors, Lizard, Spock")
print("")
print("The rules are simple:")
print("")
print("Scissors cuts Paper, Paper covers Rock,")
print("Rock crushes Lizard, Lizard poisons Spock,")
print("Spock smashes Scissors, Scissors decapitates Lizard,")
print("Lizard eats Paper, Paper disproves Spock,")
print("Spock vaporizes Rock, and as it always has, Rock crushes Scissors.")
print("")
print("")


#----------Player Options----------
   
player_choice = input("Choose either Rock, Paper, Scissors, Lizard, Spock:  ")


print("")

while player_choice == "Rock" or "Paper" or "Scissors" or "Lizard" or "Spock":

    if player_choice == "Rock":
        print("The player chose Rock")

    elif player_choice == "Paper":
        print("The player chose Paper")
        
    elif player_choice == "Scissors":
        print("The player chose Scissors")

    elif player_choice == "Lizard":
        print("The player chose Lizard")

    elif player_choice == "Spock":
        print("The player chose Spock")
    else:
        print("Invalid option: Please choose Rock, Paper, Scissors, Lizard, or Spock")
        print("")
        player_choice = input("Choose either Rock, Paper, Scissors, Lizard, Spock:  ")
        if player_choice == "Rock" or "Paper" or "Scissors" or "Lizard" or "Spock":
            continue

    print("")


#----------Computer Options----------

    computer_options = ["Rock","Paper","Scissors","Lizard","Spock"]

    computer_choice = computer_options[randint(0,4)]
    
    if computer_choice == "Rock":
        print("The computer chose Rock")

    if computer_choice == "Paper":
        print("The computer chose Paper")
        
    if computer_choice == "Scissors":
        print("The computer chose Scissors")

    if computer_choice == "Lizard":
        print("The computer chose Lizard")

    if computer_choice == "Spock":
        print("The computer chose Spock")

    print("")

#----------Gameplay----------

#---Player Choice: Rock---

    if player_choice == "Rock" and computer_choice == "Rock":
        print("The game is a tie!")
    elif player_choice == "Rock" and computer_choice == "Paper":
        print("Paper covers Rock, Computer Wins!")
    elif player_choice == "Rock" and computer_choice == "Scissors":
        print("Rock crushes Scissors, Player Wins!")
    elif player_choice == "Rock" and computer_choice == "Lizard":
        print("Rock crushes Lizard, Player Wins!")
    elif player_choice == "Rock" and computer_choice == "Spock":
        print("Spock vaporizes Rock, Computer Wins!")
        

#---Player Choice: Paper---

    if player_choice == "Paper" and computer_choice == "Rock":
        print("Paper covers Rock, Player Wins!")
    elif player_choice == "Paper" and computer_choice == "Paper":
        print("The game is a tie!")
    elif player_choice == "Paper" and computer_choice == "Scissors":
        print("Scissors cuts Paper, Computer Wins!")
    elif player_choice == "Paper" and computer_choice == "Lizard":
        print("Lizard eats Paper, Computer Wins!")
    elif player_choice == "Paper" and computer_choice == "Spock":
        print("Paper disproves Spock, Player Wins!")

#---Player Choice: Scissors---

    if player_choice == "Scissors" and computer_choice == "Rock":
        print("Rock crushes Scissors, Computer Wins!")
    elif player_choice == "Scissors" and computer_choice == "Paper":
        print("Scissors cuts Paper, Player Wins!")
    elif player_choice == "Scissors" and computer_choice == "Scissors":
        print("The game is a tie!")
    elif player_choice == "Scissors" and computer_choice == "Lizard":
        print("Scissors decapitates Lizard, Player Wins!")
    elif player_choice == "Scissors" and computer_choice == "Spock":
        print("Spock smashes Scissors, Computer Wins!")

#---Player Choice: Lizard---

    if player_choice == "Lizard" and computer_choice == "Rock":
        print("Rock crushes Lizard, Computer Wins!")
    elif player_choice == "Lizard" and computer_choice == "Paper":
        print("Lizard eats Paper, Player Wins!")
    elif player_choice == "Lizard" and computer_choice == "Scissors":
        print("Scissors decapitates Lizard, Computer Wins!")
    elif player_choice == "Lizard" and computer_choice == "Lizard":
        print("The game is a tie!")
    elif player_choice == "Lizard" and computer_choice == "Spock":
        print("Lizard poisons Spock, Player Wins!")

#---Player Choice: Spock---

    if player_choice == "Spock" and computer_choice == "Rock":
        print("Spock vaporizes Rock, Player Wins!")
    elif player_choice == "Spock" and computer_choice == "Paper":
        print("Paper disproves Spock, Computer Wins!")
    elif player_choice == "Spock" and computer_choice == "Scissors":
        print("Spock smashes Scissors, Player Wins!")
    elif player_choice == "Spock" and computer_choice == "Lizard":
        print("Lizard poisons Spock, Computer Wins!")
    elif player_choice == "Spock" and computer_choice == "Spock":
        print("The game is a tie!")

    print("")
    player_choice = input("Choose either Rock, Paper, Scissors, Lizard, Spock:  ")

















