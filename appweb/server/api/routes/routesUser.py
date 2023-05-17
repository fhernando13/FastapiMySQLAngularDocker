from fastapi import APIRouter
from config.conexion import conn, engine
from models.modelUser import users
from schemas.schemaUser import userSchema, userLogin
from fastapi.responses import Response
from fastapi import FastAPI, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List


user = APIRouter()


@user.get('/api/users/index')
def index():
    return "Welcome to the FastAPI"


@user.get('/api/users/all_users', response_model=List[userSchema])
def get_users():      
    with engine.connect() as condb:  
        results = condb.execute(users.select()).fetchall()
        condb.close()
        return results
        
          
@user.get('/api/users/one_user/{id}', response_model=userSchema)
def get_user(id: str):
    with engine.connect() as condb:
        result = condb.execute(users.select().where(users.c.id == id)).first()
        if result == None:
            raise HTTPException(status_code=404, detail="User not exist")
        return result
     

@user.post('/api/users/add_user', status_code=HTTP_201_CREATED)
def add_user(user: userSchema):
    with engine.connect() as condb:
        new_user = user.dict()
        new_user["password"] = generate_password_hash(user.password, "pbkdf2:sha256:30", 30)
        condb.execute(users.insert().values(new_user))
        return Response(status_code=HTTP_201_CREATED)
        

@user.put('/api/users/update_user/{id}', response_model=userSchema)
def update_user(data_update: userSchema, id: str):
    with engine.connect() as condb:
        encryp_password  = generate_password_hash(data_update.password, "pbkdf2:sha256:30", 30)
        query = condb.execute(users.select().where(users.c.id == id)).first()
        if query == None:
            raise HTTPException(status_code=404, detail="User not exist")
        condb.execute(users.update().values(name=data_update.name, 
                                             lastname=data_update.lastname, 
                                             email=data_update.email, 
                                             age=data_update.age,
                                             password=encryp_password).where(users.c.id == id))
        result = condb.execute(users.select().where(users.c.id == id)).first()
        print("User updated")
        return result


@user.delete('/api/users/delete_user/{id}', status_code=HTTP_204_NO_CONTENT)
def delete_user(id: str):
    with engine.connect() as condb:
        condb.execute(users.delete().where(users.c.id == id))
        return Response(status_code=HTTP_204_NO_CONTENT)

@user.post("/api/users/login")
def user_login(data_user: userLogin):
    with engine.connect() as condb:
        result = condb.execute(users.select().where(users.c.email == data_user.email)).first()

        if result != None:
            check_password = check_password_hash(result[5], data_user.password)
            if check_password != True:
                return "Password incorrect"
            else:
                return "Success"
        else:
            return "User not exist"