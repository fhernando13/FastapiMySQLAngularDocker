from fastapi import APIRouter
from config.conexion import engine
from models.modelUser import users
from schemas.schemaLogin import loginSchema
from werkzeug.security import check_password_hash


login = APIRouter()

@login.post("/api/users/login")
def user_login(data_user: loginSchema):
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