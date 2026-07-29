from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
)

while True:
    q = input("You: ")
    if q == "quit":
        break

    response = model.invoke(q)
    print("Gemini:", response.content)