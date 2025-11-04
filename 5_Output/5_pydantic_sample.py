from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-pro')

#schema
class Review(BaseModel):
    key_themes : list[str] = Field(description = "write down all the key themes discuessed in the review")
    summary: str = Field(description= "A brief summary of the review")
    sentiment: str = Field(description="overall sentiment of the review, either positive, negative, or neutral")
    pros: Optional[list[str]] = Field(description='All the pros mentioned in the review')
    cons: Optional[list[str]] = Field(description='All the cons mentioned in the review')
    name: Optional[str] = Field(description='Name of the reviewer')
    
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

print(
    f"Key Themes: {result.key_themes}\n"
    f"Summary: {result.summary}\n"
    f"Sentiment: {result.sentiment}\n"
    f"Pros: {result.pros}\n"
    f"Cons: {result.cons}\n"
    f"Name: {result.name}"
)

