# Greet the user
print("Hello! I am AI Bot. What's your name?")

# Get the user input
name = input()

# Respong to the user's name
print(f"Nice to meet you, {name}!")

# Ask a question
print("How are you feeling today?  (good/bad)  :  ")
mood = input().lower()

# Use conditional statements to respong based on input
if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that. I hope your day gets better!")
else:
    print("I see. Sometimes it's hard to put feelings into words.")

    # End the conversation
print("Thank you for chatting with me, " + name + "! Have a great day!")