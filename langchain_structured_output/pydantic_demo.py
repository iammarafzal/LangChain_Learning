from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = "New Student"
    age: Optional[int] = None
    email: EmailStr
    cpga: float = Field(gt=0, lt=4.0, default=1.5, description="A decimal value representing the cgpa of the student")


new_student = {'age': "32", 'email': 'abc@gmail.com'}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()