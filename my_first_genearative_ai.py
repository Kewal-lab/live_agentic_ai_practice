import ollama;

SYSTEM_PROMPT = """
You are a Docker Expert. you can explain things in 1-2 line max.
you don't  overthink, hullicinate or keep reasoining , you Reason and act accordingly.
these are the thing you do
1/ You tell about the errors (what went wrong, etc)
2/ You tell about the root cause.
3/ You tell the solution in short
"""

while True:
  user_input = input("Enter your message:\n")

  if user_input == "exit":
     break

  response = ollama.chat(
     model="gemma4:26b",
     messages=[
        {
          "role": "system",
          "content": SYSTEM_PROMPT,
        },
        {
          "role": "user", 
          "content": user_input, 
               }
            ]  
  )  
  
  print(response["message"]["content"])
