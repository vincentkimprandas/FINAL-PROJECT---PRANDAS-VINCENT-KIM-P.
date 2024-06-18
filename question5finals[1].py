import random

def get_player_choice():
    while True:
        print("Choose (1) Rock, (2) Paper, or (3) Scissors:")
        choice = input("Enter your choice (1/2/3): ")
        if choice in ('1', '2', '3'):
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    player_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")
    print("Best of three. The first to win two rounds wins the game.")

    while player_score < 2 and computer_score < 2:
        print("\nRound Start:")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if "win" in result:
            player_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Score: Player {player_score} - {computer_score} Computer")

    if player_score > computer_score:
        print("\nCongratulations! You won the game!")
    else:
        print("\nComputer wins the game. Better luck next time!")

if __name__ == "__main__":
    main()