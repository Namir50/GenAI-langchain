#TypeDict is a way to define a python dictionary where you specify what keys and values should exist
#It helps ensure your dictionary follows a spcific structure
#suppose we give value as string to the key which takes integer, typedict rectifies this error and stores value anyway
#typedict is usually used when we only need type hints and dont need validation
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    
new_person: Person = {'name':'Namir','age':22}  #you can see the datatype by hovering on the key and if we store the datatype otherwise, it still takes it without throwing error

print(new_person)