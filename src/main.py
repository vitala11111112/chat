from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserRegistration(BaseModel):
      name:str
      password:str

@app.get("/")
async def root():
	return {"message": "Hello World"}

@app.post("/users")
async def register_user(user_data: UserRegistration):
    print(f"Получены данные: имя={user_data.name}, пароль={user_data.password}")
    



uvicorn.run(app, host="127.0.0.1", port=8080)