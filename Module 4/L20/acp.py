import requests
import html
import random

API_URL = "https://opentdb.com/api.php?amount=5&type=multiple"

def fetch_questions():
    response = requests.get(API_URL)
    if response.status_code != 200:
        print("Failed to fetch questions.")
        return []
    data = response.json()
    return data.get("results", [])

def ask_question(q_data, number):
    question = html.unescape(q_data["question"])
    correct = html.unescape(q_data["correct_answer"])
    incorrect = [html.unescape(ans) for ans in q_data["incorrect_answers"]]

    options = incorrect + [correct]
    random.shuffle(options)

    print(f"\nQuestion {number}: {question}")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        choice = input("Your answer (1-4): ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            break
        print("Please enter a valid option number.")

    chosen = options[int(choice) - 1]
    if chosen == correct:
        print("Correct!")
        return True
    else:
        print(f"Wrong. The correct answer was: {correct}")
        return False

def main():
    print("Welcome to the Trivia Quiz!")
    questions = fetch_questions()
    if not questions:
        return

    score = 0
    for i, q in enumerate(questions, start=1):
        if ask_question(q, i):
            score += 1

    print(f"\nQuiz finished! You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    main()
