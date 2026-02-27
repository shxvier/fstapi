from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from models import UserBasic, UserAge, Feedback

# Задание 1.1: Переименованная переменная приложения
my_app = FastAPI()

feedbacks = []

# Задание 1.1
@my_app.get("/")
def read_root():
    return {"message": "Авторелоад действительно работает"}

# Задание 1.2
@my_app.get("/html")
def read_html():
    return FileResponse("index.html")

# Задание 1.3*
class CalcParams(BaseModel):
    num1: float
    num2: float

@my_app.post("/calculate")
def calculate(data: CalcParams):
    return {"result": data.num1 + data.num2}

# Задание 1.4
current_user = UserBasic(name="Ваше Имя и Фамилия", id=1)

@my_app.get("/users")
def get_users():
    return current_user

# Задание 1.5*
@my_app.post("/user")
def create_user(user: UserAge):
    is_adult = user.age >= 18
    return {"name": user.name, "age": user.age, "is_adult": is_adult}

# Задания 2.1 и 2.2*
@my_app.post("/feedback")
def post_feedback(feedback: Feedback):
    feedbacks.append(feedback.model_dump())
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}