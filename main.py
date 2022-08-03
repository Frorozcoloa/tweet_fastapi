from datetime import date, datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

from fastapi import FastAPI

app = FastAPI()

#Models
class User(BaseModel):
    user_id : UUID = Field(
        ...,
        title = "User id",
    )
    email : EmailStr = Field(
        ...,
        )
    password : str = Field(
        ...,
        min_length=8,
        max_length=50
    )
    first_name : str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name : str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_dat : Optional[date] = Field(default=None)


class Tweet(BaseModel):
    tweet_id : UUID = Field(...)
    content : str = Field(
        ...,
        min_length=1,
        max_length=255
        )
    created_at : datetime = Field(
        default = datetime.now(),
    )
    updated_at : Optional[datetime] = Field(None)
    by: User = Field(...)

@app.get(path="/")
def home():
    return {"Twitter API": "Working"}