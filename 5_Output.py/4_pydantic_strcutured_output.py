#pydantic helps in explaining what the data type should be when error is thrown
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None #in pydantic we have to specify None if the value of attribute is not mentioned
    number : Optional[int] = None
    email: EmailStr  #pydantic has the ability to validate emails, throws the error if invalid
    cgpi: float = Field(gt = 0, lt= 10.1) #field helps to set constraints or criterias
    
new_student = {'name':'namir','number':34, 'email':'namirsayyed50@gmail.com', 'cgpi' : 7.3}  #here if integer is passed as a string, pydantic automatically converts it into int 

student = Student(**new_student)

print(student)