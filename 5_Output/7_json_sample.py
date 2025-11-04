from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Use a valid Gemini model
model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

# JSON Schema
json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Write down all the key themes discussed in the review",
        },
        "summary": {
            "type": "string",
            "description": "Write a summary of the review",
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "negative", "neutral"],
            "description": "Return sentiment of the review",
        },
        "pros": {
            "anyOf": [
                {"type": "array", "items": {"type": "string"}},
                {"type": "null"}
            ],
            "description": "Write down all the pros in the review",
        },
        "cons": {
            "anyOf": [
                {"type": "array", "items": {"type": "string"}},
                {"type": "null"}
            ],
            "description": "Write down all the cons in the review",
        },
        "name": {
            "anyOf": [
                {"type": "string"},
                {"type": "null"}
            ],
            "description": "Write the name of the reviewer",
        },
    },
    "required": ["key_themes", "summary", "sentiment"],
}


structure_model = model.with_structured_output(json_schema)

review_text = """
I recently bought this gaming console, and my experience has been a mix of positives and a few letdowns. 
On the bright side, the console runs smoothly with fast load times and crisp graphics that make modern titles look amazing. 
The controller feels ergonomic and responsive, which makes long sessions comfortable. 
I also appreciate the user-friendly interface and the seamless integration with online services. 
However, there are some drawbacks that hold it back from being perfect. 
The storage fills up quickly, and upgrading feels unnecessarily expensive. 
Additionally, while most games run flawlessly, I noticed occasional frame drops in more demanding titles. 
The fan noise can also get distracting during heavy gameplay. 
Overall, it’s a solid console that delivers great performance for the price, but it still has room for improvement in terms of storage, optimization, and quietness. 
I’d recommend it, but with some reservations.

Pros:
Smooth performance with fast load times
Crisp, modern graphics
Ergonomic and responsive controller
User-friendly interface with seamless online features

Cons:
Limited storage capacity, costly to upgrade
Occasional frame drops in demanding games
Noticeable fan noise during heavy gameplay

Review by Jon Snow
"""

result = structure_model.invoke(review_text)

print(result)
