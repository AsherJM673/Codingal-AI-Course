import requests

BASE_URL = "https://uselessfacts.jsph.pl"

def get_random_fact(language="en"):
    """Fetch a completely random fact."""
    url = f"{BASE_URL}/random.json?language={language}"
    response = requests.get(url)
    return response.json()

def get_fact_by_category(category, language="en"):
    """Fetch a fact from a specific category."""
    url = f"{BASE_URL}/random.json?language={language}&category={category}"
    response = requests.get(url)
    return response.json()

def display_fact(data):
    """Pretty-print the fact."""
    print(f"\n🧠 Fact: {data['text']}")
    print(f"📌 Source: {data.get('source', 'Unknown')}")
    print(f"🔗 URL: {data.get('source_url', 'N/A')}\n")

# --- Example usage ---
print("Fetching a completely random fact...")
fact1 = get_random_fact()
display_fact(fact1)

print("Fetching facts from different categories...")
categories = ["science", "history", "general"]  # only works if API supports them

for category in categories:
    print(f"Category: {category}")
    fact = get_fact_by_category(category)
    display_fact(fact)
