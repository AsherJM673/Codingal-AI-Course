import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama for colored output
colorama.init()

# Emojis for the start of the program
print(f"{Fore.CYAN} 🌟 Welcome to Sentiments Spy! 🌟{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL} ").strip()
if not user_name:
    user_name = "Mystery Agent" # Fallback if user doesn't provide a name

    # Store conversation as a list of tuples: (text, polarity, sentiment_type)
conversation_history = [] 

print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a Sentence and I will analyze your sentences with TextBlob and show you the sentiment. ")
print(f"{Fore.YELLOW}Type 'exit' to end the conversation.{Style.RESET_ALL}")
while True:
    user_input = input(f"{Fore.GREEN}You: {Style.RESET_ALL} ").strip()
    
    if not user_input:
        print(f"{Fore.RED}Please enter a valid sentence.{Style.RESET_ALL}")
        continue

    # Check for exit command
    if user_input.lower() == 'exit':
        print(f"{Fore.CYAN}Goodbye, Agent {user_name}! Stay safe!{Style.RESET_ALL}")
        break

    elif user_input.lower() == 'reset':
        conversation_history.clear()
        print(f"{Fore.YELLOW}Conversation history cleared.{Style.RESET_ALL}")
        continue 
      
    elif user_input.lower() == 'history':
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history available.{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
               # Choose color & emoji based on sentiment 
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                
                print(f"{color}{idx}. {emoji} {text} | Polarity: {polarity:.2f} | Sentiment: {sentiment_type}{Style.RESET_ALL}")
        continue
    
    # Analyze sentiment
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

        # Store in history
    conversation_history.append((user_input, polarity, sentiment_type)) 

       # Print the result with color and emojis, and polarity
    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
                f"Polarity: {polarity:.2f}{Style.RESET_ALL}")