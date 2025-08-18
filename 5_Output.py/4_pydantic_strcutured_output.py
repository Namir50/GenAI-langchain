#pydantic helps in explaining what the data type should be when error is thrown
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    
new_student = {'name':'namir'}

student = Student(**new_student)

print(student.name)