#pydantic helps in explaining what the data type should be when error is thrown
#pydantic is usually used when we need data validation, default values and we want automatic type conversion
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None #in pydantic we have to specify None if the value of attribute is not mentioned
    number : Optional[int] = None
    email: EmailStr  #pydantic has the ability to validate emails, throws the error if invalid
    cgpi: float = Field(gt = 0, lt= 10.1, description='overall pointers of all sem') #field helps to set constraints or criterias and can also used for descriptions
    college: str = 'UCOE' #we can set default value as well
     
new_student = {'name':'namir','number':34, 'email':'namirsayyed50@gmail.com', 'cgpi' : 7.3}  #here if integer is passed as a string, pydantic automatically converts it into int 

student = Student(**new_student)

print(student)

#we can also make dictionary out of it
student_dict = dict(student)
print(student_dict['name'])

#we can also make json out of it
student_json = student.model_dump_json()
print(student_json)