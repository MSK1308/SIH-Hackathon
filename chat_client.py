import requests

API_URL = "http://127.0.0.1:8000/chat"

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        break

    response = requests.post(API_URL, json={"user_input": user_input})
    print("Neurox: ", response.json().get("reply"))