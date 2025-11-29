import requests

def main():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
        return

    todo = response.json()

    print("Todo information from API:")
    print(f"- ID: {todo['id']}")
    print(f"- User ID: {todo['userId']}")
    print(f"- Title: {todo['title']}")
    print(f"- Completed: {todo['completed']}")

if __name__ == "__main__":
    main()
