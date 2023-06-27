from fastapi import APIRouter, Header
from config.jwt_config import write_token, validate_token
from config.conexion import engine
from models.modelUser import users
from schemas.schemaLogin import loginSchema
from werkzeug.security import check_password_hash
from fastapi.responses import JSONResponse


login = APIRouter()


@login.post("/api/users/login")
def user_login(data_user: loginSchema):
    with engine.connect() as condb:
        result = condb.execute(users.select().where(users.c.email == data_user.email)).first()
        if result != None:            
            check_password = check_password_hash(result[7], data_user.password)
            if check_password != True:
                return "Password incorrect"
            else:
                return write_token(data_user.dict())
        else:
            return JSONResponse(content={"message":"User not found"}, status_code=401)


@login.post("/api/verify")
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)