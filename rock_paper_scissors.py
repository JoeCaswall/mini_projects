from computer_choice import computer_choice

def game():
    machine_score = 0
    human_score = 0
    game_running = False
    start_game = input("This is a game of rock, paper, scissors! Want to play? y/n ")
    if start_game == "y":
        game_running = True
        print("Enter q any time to quit and display the final score.")
    while game_running:
        machine_choice = computer_choice()
        human_choice = input("Please choose rock, paper or scissors: ").lower()
        if human_choice == "q":
            break
        if machine_choice == "rock":
            print(f"Computer choice: {machine_choice}")
            if human_choice == "rock":
                print("Draw.")
            elif human_choice == "paper":
                print("You win!")
                human_score += 1
            elif human_choice == "scissors":
                print("You lose!")
                machine_score += 1
            else:
                print("Invalid choice. PLease try again")
        if machine_choice == "paper":
            print(f"Computer choice: {machine_choice}")
            if human_choice == "rock":
                print("You lose!")
                machine_score += 1
            elif human_choice == "paper":
                print("Draw.")
            elif human_choice == "scissors":
                print("You win!")
                human_score += 1
            else:
                print("Invalid choice. PLease try again")
        if machine_choice == "scissors":
            print(f"Computer choice: {machine_choice}")
            if human_choice == "rock":
                print("You win!")
                human_score += 1
            elif human_choice == "paper":
                print("You lose!")
                machine_score += 1
            elif human_choice == "scissors":
                print("Draw.")
            else:
                print("Invalid choice. PLease try again")
    print("\nFinal scores:")
    print(f"Computer Score: {machine_score}")
    print(f"Human Score: {human_score}")
    if human_score > machine_score:
        print("Congratulations You won!")
    elif human_score < machine_score:
        print("Better luck next time!")
    else:
        print("We were evenly matched.")

game()