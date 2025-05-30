# Greet the user
print("Hello! I am Gemini Pro. What's your name?")

# Get the user input
name = input()

# Respond to the user's name
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

# Ask the user about their favorite color
print("What's your favorite color?")
favorite_color = input() 
print(f"That's a nice color, {name}!")

# Ask the user about their favorite food
print("What's your favorite food?")
favorite_food = input()
print(f"Yum! {favorite_food} sounds delicious, {name}!")

# Ask the user about their favorite hobby
print("What's your favorite hobby?")
favorite_hobby = input()
print(f"That's great! {favorite_hobby} is a fun way to spend time, {name}!")

# Ask the user about their favorite movie
print("What's your favorite movie?")
favorite_movie = input()
print(f"{favorite_movie} is a fantastic choice, {name}!")

# Ask the user about their favorite book
print("What's your favorite book?")
favorite_book = input()
print(f"{favorite_book} is a wonderful read, {name}!")

# End the conversation
print("Thank you for chatting with me, " + name + "! Have a great day!")