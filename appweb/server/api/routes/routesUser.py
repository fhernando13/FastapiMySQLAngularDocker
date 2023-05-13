from fastapi import APIRouter
from config.conexion import conn
from models.modelUser import users
from schemas.schemaUser import userSchema
import json

user = APIRouter()


@user.get('/index')
def index():
    return "Welcome to the FastAPI"


@user.get('/api/allUsers')
def get_users():        
    results = conn.execute(users.select()).fetchall()
    return results
          
          
@user.get('/user')
def get_user():
    return "only one user"


@user.post('/add_user', status_code=201)
def add_user(user: userSchema):
    try:
        new_user = {"name":user.name, "lastname":user.lastname, "email":user.email, "age":user.age}
        conn.execute(users.insert().values(new_user))
        conn.commit()
        return "add user"
    except Exception as e:
        return print(f'Error: {e}', status_code=400) 


@user.put('/update_user')
def update_user():
    return "update an user"


@user.delete('/delete_user')
def delete_user():
    return "delete an user"

