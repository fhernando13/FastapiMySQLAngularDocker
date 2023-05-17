from typing import Optional 
from pydantic import BaseModel


class schemaUsers(BaseModel):
    id: Optional[str]
    name: str
    lastname: str
    email: str
    age: str
    password: str