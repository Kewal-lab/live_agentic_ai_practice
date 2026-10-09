agent_ai_working.py
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent

import subprocess


SYSTEM_PROMPT = """
You are a Docker Expert. You can explain things in 1-2 lines maximum.

You don't overthink or hallucinate. Reason and act accordingly.

These are the things you do:

1. Tell about the errors (what went wrong, etc.)
2. Tell about the root cause.
3. Tell the solution in short.
"""


@tool
def show_running_containers():
    """Show all currently running Docker containers."""
    
    result = subprocess.run(
        ["docker", "ps"],
        capture_output=True,
        text=True,
        check=False
    )

    return result.stdout


@tool
def show_containers_logs_by_name(container_name: str):
    """Show logs of a Docker container by its name."""
    
    result = subprocess.run(
        ["docker", "logs", container_name],
        capture_output=True,
        text=True,
        check=False
    )

    return result.stdout if result.stdout else result.stderr


llm = ChatOllama(
    model="gemma4:26b",
    temperature=0.8
)


tools = [
    show_running_containers,
    show_containers_logs_by_name
]


agent = create_agent(
    llm,
    tools
)

while True:


    user_input = input("Enter your message:\n")
    if user_input == "exit":
        break

    response = agent.invoke(
    {
    "messages": [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
    }
    )


    print(response["messages"][-1].content)
