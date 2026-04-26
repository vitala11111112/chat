from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.db import Users
import socketio
from fastapi.staticfiles import StaticFiles

# sio = socketio.AsyncServer(async_mode="asgi")
app = FastAPI()
Users_db = Users()
# socket_app = socketio.ASGIApp(sio, other_asgi_app=app)
app.mount("/static", StaticFiles(directory="static"), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserRegistration(BaseModel):
    name: str
    password: str


# @sio.event
# async def connect(sid, environ):
#     print(f"Клиент подключился: {sid}")
#     await sio.emit("message", {"data": "Вы подключены"}, room=sid)


# @sio.on("chat_message")
# async def handle_chat_message(sid, data):
#     print(f"Сообщение чата от {sid}: {data}")
#     # Отправляем ответ конкретному клиенту
#     await sio.emit("chat_response", {"data": "Сообщение получено"}, room=sid)
#     # Если нужно отправить сообщение всем клиентам:
#     # await sio.emit("chat_response", {"data": "Новое сообщение"}, broadcast=True)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/users")
async def register_user(user_data: UserRegistration):
    Users_db.insert(user_data.name, user_data.password)
    print(Users_db.read())

    return {"messege": "данные успешно"}


@app.post("/users_log")
async def login_user(user_data: UserRegistration):
    user_id = Users_db.find(user_data.name, user_data.password)
    print(user_id)

    return {"real_acc": user_id}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
