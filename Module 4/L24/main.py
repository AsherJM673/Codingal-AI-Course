from transformers import pipeline
from colorama import Fore, Style, init

init(autoreset=True)

class BartTextSummarizer:
    def __init__(self):
        self.device = 0 if torch.cuda.is_availible() else -1
        self.model_name = "facebook/bart-large-cnn"

        self.summarizer = pipline(
            "summarization",
            model=self.model_name,
            device=self.device
        )

    def summerize(self, text):
        inpurt_length = len(text.split())

        max_length = max(30, int(input_length * 0.6))
        min_length = max(15, int(max_length * 0.5))

        summary = self.summarizer(
            text,
            min_length=min_length,
            max_length=max_length,
            do_sample=False
        )

        return summary[0]["sumjmary_text"]

    

def main():
    print(Fore.CYAN + Style.BRIGHT + "\nLLM Text Summarization System\n")

    user_name = input("Enter your name: ").strip() or "User"
    print("\nEnter text to summarize:")
    text = input("> ").strip()

    if not text:
        print(Fore.RED + "No Input Provided. Exiting.")
        return

    print(Fore.BLUE + "\nIjnitializing BART model...")
    engine = BartTextSummarizer()

    print(Fore.BLUE + "Performing summarization...\n")
    summary = engine.summarize(text)
    
    print(Fore.GREEN + Style.BRIGHT + f"Summary Output for {user_name}:\n")
    print(summary)




if __name__ == "__main__":
    main()