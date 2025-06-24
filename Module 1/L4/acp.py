import random
from colorama import init, Fore, Style
init(autoreset=True)

def get_player_choice():
    choice = ''
    while choice not in ['ROCK', 'PAPER', 'SCISSORS']:
        choice = input(Fore.GREEN + "Choose Rock, Paper, or Scissors: " + Style.RESET_ALL).upper()
    return choice

def get_ai_choice():
    return random.choice(['ROCK', 'PAPER', 'SCISSORS'])

def display_choices(player, ai):
    print(Fore.CYAN + f"\nYou chose: {Fore.YELLOW + player}")
    print(Fore.CYAN + f"AI chose: {Fore.MAGENTA + ai}" + Style.RESET_ALL)

def determine_winner(player, ai):
    if player == ai:
        return "tie"
    elif (player == 'ROCK' and ai == 'SCISSORS') or \
         (player == 'PAPER' and ai == 'ROCK') or \
         (player == 'SCISSORS' and ai == 'PAPER'):
        return "player"
    else:
        return "ai"

def play_game():
    print(Fore.CYAN + "Welcome to Rock-Paper-Scissors!")
    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    while True:
        player_choice = get_player_choice()
        ai_choice = get_ai_choice()
        display_choices(player_choice, ai_choice)

        winner = determine_winner(player_choice, ai_choice)
        if winner == "tie":
            print(Fore.BLUE + "It's a tie!")
        elif winner == "player":
            print(Fore.GREEN + f"Congrats {player_name}, you win!")
        else:
            print(Fore.RED + "AI wins! Better luck next time.")

        again = input(Fore.YELLOW + "\nPlay again? (yes/no): " + Style.RESET_ALL).lower()
        if again != 'yes':
            print(Fore.CYAN + "Thanks for playing!")
            break

if __name__ == '__main__':
    play_game()
