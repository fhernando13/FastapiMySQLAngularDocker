from fastapi import FastAPI
from routes.routesUser import user

app = FastAPI()

app.include_router(user)
