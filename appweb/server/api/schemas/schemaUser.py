from typing import Optional 
from pydantic import BaseModel


class schemaUsers(BaseModel):
    id: Optional[str]
    name: str
    lastname: str
    phonework: Optional[str]
    phonepersonal: str
    birthdate: str
    email: str
    password: str