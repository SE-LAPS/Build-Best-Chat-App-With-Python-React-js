from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import requests

PRIVATE_KEY = "fe80528e-6a2b-4ad3-a6f2-6181e4770f52"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str

@app.post('/authenticate')
async def authenticate(user: User):
    response = requests.put('https://api.chatengine.io/users/',
        data={
            "username": user.username,
            "secret": user.username,
            "first_name": user.username,
        },
        headers={ "Project-Key": PRIVATE_KEY }
    )
    return response.json()