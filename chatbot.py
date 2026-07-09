from google import genai
from config import GEMINI_API_KEY

# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)


def get_response(user_message):
    """
    Send the user's message to Gemini
    and return the AI response.
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"


# -------------------------
# Test chatbot
# -------------------------
if __name__ == "__main__":

    print("Gemini ChatBot Started!")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ")

        if question.lower() in ["exit", "quit"]:
            break

        answer = get_response(question)

        print("\nBot:", answer)
        print()