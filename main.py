from datetime import date, datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

from fastapi import FastAPI, status

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

# Path Operation

## User

@app.post(
    path="/singup",
    response_model=User,
    response_model_exclude={"password"},
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["User"]
)
def singup():
    pass

@app.post(
    path="/login",
    response_model=User,
    response_model_exclude={"password"},
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["User"]
)
def login():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    response_model_exclude={"password"},
    status_code=status.HTTP_200_OK,
    summary="show all Users",
    tags=["User"]
)
def show_all_user():
    pass

@app.get(
    path="/user/{user_id}",
    response_model=User,
    response_model_exclude={"password"},
    status_code=status.HTTP_200_OK,
    summary="show aUser",
    tags=["User"]
)
def show_a_user():
    pass

@app.delete(
    path="/user/{user_id}/delete",
    response_model=User,
    response_model_exclude={"password"},
    status_code=status.HTTP_200_OK,
    summary="delete a User",
    tags=["User"]
)
def delete_a_user():
    pass

@app.put(
    path="/user/{user_id}/update",
    response_model=User,
    response_model_exclude={"password"},
    status_code=status.HTTP_200_OK,
    summary="update a User",
    tags=["User"]
)
def update_a_user():
    pass


## Tweet

@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweet",
    tags=["Tweets"]
    )
def home():
    return {"Twitter API": "Working"}


@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post():
    pass

@app.get(
    path="/tweet/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="show a tweet",
    tags=["Tweets"]
)
def show_a_tweet():
    pass

@app.delete(
    path="/tweet/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="show a tweet",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass

@app.put(
    path="/tweet/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="show a tweet",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass

