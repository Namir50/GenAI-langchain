from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

class Review(BaseModel):
    key_themes : list[str] = Field(desription = 'Write all the key themes discuessed in the review')
    summary : str = Field(description = 'Give a summarized version of this review')
    number_of_words: int = Field(description = 'Number of words the review has')
    sentiment : str = Field(description = 'What is the overall sentiment of the review, it could be either Positive, Negative or Neutral')
    pros: Optional[list[str]] = Field(description='All the pros mentioned in the review')
    cons: Optional[list[str]] = Field(description = 'All the cons mentioned in the review')
    name: Optional[str] = Field(description = 'Write the name of the person who wrote this review')
    
strcutured_model = model.with_structured_output(Review)

result = strcutured_model.invoke("""Reviewer: Aditi Menon
I’ve been using the X100 headphones for about three weeks. The sound quality is really good, with clear highs and strong bass. The noise cancellation works fine in cafés and offices, though it struggles a little on airplanes. The battery life is excellent—I only needed to charge them once in a whole week.
However, the ear cups can feel uncomfortable after long use, and the design is a bit bulky if you’re planning to carry them around daily.
Pros:
Great sound quality

Cons:
Can get uncomfortable after long sessions
Noise cancellation not as strong as premium models
Slightly bulky design""")
    
print(
    f"Key themes:{result.key_themes}\n"
    f"Summary:{result.summary}\n"
    f"Sentiment:{result.sentiment}\n"
    f"Pros:{result.pros}\n"
    f"Cons:{result.cons}\n"
    f"Reviewer Name:{result.name}\n"
)