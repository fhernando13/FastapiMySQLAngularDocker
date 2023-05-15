from fastapi import APIRouter
from config.conexion import conn, engine
from models.modelUser import users
from schemas.schemaUser import userSchema
from fastapi.responses import Response
from fastapi import FastAPI, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT


user = APIRouter()


@user.get('/api/index')
def index():
    return "Welcome to the FastAPI"


@user.get('/api/allUsers')
def get_users():      
    with engine.connect() as condb:  
        results = condb.execute(users.select()).fetchall()
        condb.close()
        return results
        
          
@user.get('/api/one_user/{id}', response_model=userSchema)
def get_user(id: str):
    with engine.connect() as condb:
        result = condb.execute(users.select().where(users.c.id == id)).first()
        if result == None:
            raise HTTPException(status_code=404, detail="User not exist")
        return result
     

@user.post('/api/add_user')
def add_user(user: userSchema):
    with engine.connect() as condb:
        new_user = {"name":user.name, "lastname":user.lastname, "email":user.email, "age":user.age}
        condb.execute(users.insert().values(new_user))
        return "add user"


@user.put('/api/update_user/{id}')
def update_user(data_update: userSchema, id: str):
    with engine.connect() as condb:
        sql = condb.execute(users.select().where(users.c.id == id)).first()
        if sql == None:
            raise HTTPException(status_code=404, detail="User not exist")
        condb.execute(users.update().values(name=data_update.name, 
                                             lastname=data_update.lastname, 
                                             email=data_update.email, 
                                             age=data_update.age).where(users.c.id == id))
        result = condb.execute(users.select().where(users.c.id == id)).first()
        print("User updated")
        return result


@user.delete('/api/delete_user/{id}', status_code=HTTP_204_NO_CONTENT)
def delete_user(id: str):
    with engine.connect() as condb:
        condb.execute(users.delete().where(users.c.id == id))
        return Response(status_code=HTTP_204_NO_CONTENT)