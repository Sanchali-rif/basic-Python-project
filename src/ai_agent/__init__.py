from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


@tool
def calculator(a: float, b: float) -> str:
    """Add two numbers together."""
    print("Tool has been called.")
    return f"The sum of {a} and {b} is {a + b}"


@tool
def say_hello(name: str) -> str:
    """Greet a user by name."""
    print("Tool has been called.")
    return f"Hello {name}, I hope you are well today!"


def print_response(content):
    """Print Gemini responses whether they are strings or content blocks."""

    if isinstance(content, str):
        print(content)
        return

    if isinstance(content, list):
        for part in content:
            if isinstance(part, dict):
                if part.get("type") == "text":
                    print(part.get("text", ""), end="")
            else:
                print(part, end="")
        print()
        return

    print(content)


def main():
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
    )

    tools = [calculator, say_hello]

    agent = create_agent(
        model=model,
        tools=tools,
    )

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        response = agent.invoke(
            {
                "messages": [
                    HumanMessage(content=user_input)
                ]
            }
        )

        print("\nAssistant: ", end="")
        print_response(response["messages"][-1].content)


if __name__ == "__main__":
    main()