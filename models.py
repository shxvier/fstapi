from pydantic import BaseModel, Field, field_validator
import re

# Задание 1.4
class UserBasic(BaseModel):
    name: str
    id: int

# Задание 1.5*
class UserAge(BaseModel):
    name: str
    age: int

# Задания 2.1 и 2.2*
class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)

    @field_validator('message')
    @classmethod
    def check_forbidden_words(cls, v: str) -> str:
        # Регулярное выражение для поиска корней недопустимых слов в любых падежах
        pattern = re.compile(r'(кринж|рофл|вайб)', re.IGNORECASE)
        if pattern.search(v):
            raise ValueError("Использование недопустимых слов")
        return v