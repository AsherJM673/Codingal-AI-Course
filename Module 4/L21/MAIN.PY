import requests
import json
from colorama import Fore, Style, init

init(autoreset=True)

API_URL = "https://uselessfacts.jsph.pl/random.json?language=en"


def fetch_fact():
    try:
        r = requests.get(API_URL, timeout=5)
        if r.status_code == 200:
            d = r.json()
            return d.get("text", None)
        return None 
    except:
        return None 
    

def save_fact(text):
    entry = {"fact": text}
    with open("facts.json", "a", encoding="utf-8") as fp:
        json.dump(entry, fp)
        fp.write("\n")

def read_saved():
    try:
        with open("facts.json", "r", encoding="utf-8") as fp:
            lines = fp.readlines()
            if not lines:
                print(Fore.LIGHTBLACK_EX + "No saved facts found.")
                return
        print(Fore.CYAN + "\n=== Saved Facts ===")
        for line in lines:
            obj = json.loads(line.strip())
            print(Fore.GREEN + "- " + obj["fact"])
    except FileNotFoundError:
        print(Fore.LIGHTBLACK_EX + "No saved facts found.")


def menu():
    print(Fore.CYAN + "\n=== Random Fact Explorer ===")
    print(Fore.YELLOW + "[1] Get a new random fact")
    print(Fore.YELLOW + "[2] View saved facts")
    print(Fore.YELLOW + "[q] Quit")



def main():
    while True:
        menu()
        choice = input(Fore.WHITE + "Select: ").strip().lower()
        if choice == "q":
            break

        elif choice == "1":
            fact = fetch_fact()
            if not fact:
                print(Fore.RED + "Failed to retrieve fact.")
                continue

            print(Fore.GREEN + "\nFact:")
            print(Fore.CYAN + fact)

            save = input(Fore.WHITE + "Save this fact? (y/n): ").strip().lower()
            if save == "y":
                save_fact(fact)
                print(Fore.GREEN + "Saved successfully.")

        elif choice == "2":
            read_saved()

        else:
            print(Fore.RED + "Invalid selection.")

if __name__ == "__main__":
    main()
1