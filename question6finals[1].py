import random

def roll_dice():
    return random.randint(1, 6)

def main():
    player1_wins = 0
    player2_wins = 0

    print("Welcome to the Dice Rolling Simulator!")
    print("Best of three. The first to win two rounds wins the game.")

    while player1_wins < 2 and player2_wins < 2:
        print("\nRound Start:")
        input("Press Enter to roll the dice...")

        player1_roll = roll_dice()
        player2_roll = roll_dice()

        print(f"\nPlayer 1 rolled: {player1_roll}")
        print(f"Player 2 rolled: {player2_roll}")

        if player1_roll > player2_roll:
            player1_wins += 1
            print("Player 1 wins this round!")
        elif player2_roll > player1_roll:
            player2_wins += 1
            print("Player 2 wins this round!")
        else:
            print("It's a tie!")

        print(f"Score: Player 1 {player1_wins} - {player2_wins} Player 2")

    if player1_wins > player2_wins:
        print("\nPlayer 1 wins the game!")
    else:
        print("\nPlayer 2 wins the game!")

if __name__ == "__main__":
    main()