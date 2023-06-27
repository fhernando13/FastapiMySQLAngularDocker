from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse


MY_SECRET_KEY="mysecretkey"
ALGORITHM='HS256'


def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date


def write_token(date: dict):
    token: str = encode(payload=date, key=MY_SECRET_KEY, algorithm=ALGORITHM)
    return token


def validate_token(token, output=True):
    try:
        if output:
            decode(token, key=MY_SECRET_KEY, algorithms=[ALGORITHM])
        decode(token, key=MY_SECRET_KEY, algorithms=[ALGORITHM])
    except exceptions.DecodeError:
        return JSONResponse(content={"message":"Invalid token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message":"Token expired"}, status_code=401)
    
    