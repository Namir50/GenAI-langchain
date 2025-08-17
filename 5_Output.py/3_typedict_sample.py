from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated,Optional

load_dotenv()

model = ChatOpenAI(model = 'gpt-4')

#schema
class Review(TypedDict):
    key_themes: Annotated[list[str], "All the key themes discussed"]
    summary: Annotated[str,"A brief summary of th review"]
    sentiment: Annotated[str,"Overall sentiment of the review either negative, positive, or neutral"] #here we can use literal as positive or negative using 'literal' in annotated
    pros: Annotated[Optional[list[str]], "Pros in the review"] #optional as some reviews dont contain pros
    cons: Annotated[Optional[list[str]],"Cons in the review"] #optional as some reviews dont contain cons
    name: Annotated[Optional[str], 'Name of the reviewer']
    
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
Noticeable fan noise during heavy gameplay

Review by Jon Snow""")

print(result['summary'])
print(result['sentiment'])
