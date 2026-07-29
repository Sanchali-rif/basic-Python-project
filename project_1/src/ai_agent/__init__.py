from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


@tool
def calculator(a: float, b: float) -> str:
    """Add two numbers."""
    print("Tool has been called.")
    return f"The sum of {a} and {b} is {a + b}"


@tool
def say_hello(name: str) -> str:
    """Greet a user."""
    print("Tool has been called.")
    return f"Hello {name}, I hope you are well today!"

@tool
def subtract(a: float, b: float) -> str:
    """Subtract two numbers."""
    return f"The difference is {a - b}"

@tool
def multiply(a: float, b: float) -> str:
    """Multiply two numbers."""
    return f"The product is {a * b}"

@tool
def divide(a: float, b: float) -> str:
    """devide two numbers."""
    return f"The product is {a * b}"

@tool
def square(number: float) -> str:
    """Return the square of a number."""
    return str(number ** 2)

@tool
def cube(number: float) -> str:
    """Return the cube of a number."""
    return str(number ** 3)

@tool
def celsius_to_fahrenheit(celsius: float) -> str:
    """Convert Celsius to Fahrenheit."""
    f = (celsius * 9/5) + 32
    return f"{celsius}°C = {f}°F"

@tool
def bmi(weight: float, height: float) -> str:
    """Calculate BMI from weight in kilograms and height in meters."""
    value = weight / (height ** 2)
    return f"Your BMI is {value:.2f}"

@tool
def even_or_odd(number: int) -> str:
    """Check if a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    return "Odd"

@tool
def is_prime(number: int) -> str:
    """Check whether a number is prime."""
    if number < 2:
        return "Not Prime"

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return "Not Prime"

    return "Prime"

@tool
def reverse_text(text: str) -> str:
    """Reverse a string."""
    return text[::-1]

@tool
def count_words(text: str) -> str:
    """Count the number of words in a sentence."""
    return str(len(text.split()))

@tool
def to_upper(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()

@tool
def to_lower(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()

from datetime import datetime

@tool
def current_date() -> str:
    """Return today's date."""
    return datetime.now().strftime("%d-%m-%Y")

import random

@tool
def roll_dice() -> str:
    """Roll a six-sided dice."""
    return str(random.randint(1, 6))

import random

@tool
def coin_flip() -> str:
    """Flip a coin."""
    return random.choice(["Heads", "Tails"])

import random
import string

@tool
def generate_password(length: int) -> str:
    """Generate a random password."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

import random

@tool
def random_fact() -> str:
    """Return a random programming fact."""
    facts = [
        "Python was released in 1991.",
        "JavaScript was created in just 10 days.",
        "Linux is open source.",
    ]
    return random.choice(facts)


def print_response(content):
    """Print both string and Gemini block responses."""

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
        system_prompt="""
You are a helpful AI assistant.

You have access to tools.

Rules:
- Answer general knowledge questions directly using your own knowledge.
- Use a tool only when it is actually needed.
- Do not refuse a question simply because no tool is available.
- If a user asks to add numbers, use the calculator tool.
- If a user asks to greet someone, use the say_hello tool.
""",
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
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ]
            }
        )

        print("\nAssistant: ", end="")
        print_response(response["messages"][-1].content)


if __name__ == "__main__":
    main()