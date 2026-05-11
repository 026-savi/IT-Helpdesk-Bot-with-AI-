from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# AI Response Function
def handle_query(query):

    print("🔥 handle_query CALLED 🔥")

    try:

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an IT Helpdesk Assistant. Give short and professional solutions."
                },
                {
                    "role": "user",
                    "content": query
                }
            ],
            temperature=0.5,
            max_tokens=200
        )

        response = completion.choices[0].message.content

        return response

    except Exception as e:

        print("ERROR in handle_query:", e)

        return "Something went wrong. Please try again."