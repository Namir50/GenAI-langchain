from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

model = ChatOpenAI(model = 'gpt-4')

#schema
class Review(TypedDict):
    summary: Annotated[str,"A brief summary of th review"]
    sentiment: Annotated[str,"Overall sentiment of the review either negative, positive, or neutral"]
    
structure_model = model.with_structured_output(Review)

result  = structure_model.invoke("""I recently bought this gaming console, and my experience has been a mix of positives and a few letdowns. On the bright side, the console runs smoothly with fast load times and crisp graphics that make modern titles look amazing. The controller feels ergonomic and responsive, which makes long sessions comfortable. I also appreciate the user-friendly interface and the seamless integration with online services. However, there are some drawbacks that hold it back from being perfect. The storage fills up quickly, and upgrading feels unnecessarily expensive. Additionally, while most games run flawlessly, I noticed occasional frame drops in more demanding titles. The fan noise can also get distracting during heavy gameplay. Overall, it’s a solid console that delivers great performance for the price, but it still has room for improvement in terms of storage, optimization, and quietness. I’d recommend it, but with some reservations.

Pros:

Smooth performance with fast load times

Crisp, modern graphics

Ergonomic and responsive controller

User-friendly interface with seamless online features

Cons:

Limited storage capacity, costly to upgrade

Occasional frame drops in demanding games

Noticeable fan noise during heavy gameplay""")

print(result['summary'])
print(result['sentiment'])
