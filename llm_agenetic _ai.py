import ollama

while True:
    user_input = input("Enter your message:\n")

    if user_input.lower() == "exit":
        break

    response = ollama.chat(
        model="gemma4:26b",
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
    )

    print(response["message"]["content"])