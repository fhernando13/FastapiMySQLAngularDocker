from typing import Optional 
from pydantic import BaseModel


class userSchema(BaseModel):
    id: Optional[str]
    name: str
    lastname: str
    email: str
    age: str
    password: str

class userLogin(BaseModel):
    email: str
    password: str
