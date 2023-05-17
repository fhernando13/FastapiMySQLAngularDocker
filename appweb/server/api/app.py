from fastapi import FastAPI
from routes.routesUser import user
from routes.routesLogin import login

app = FastAPI()

app.include_router(user)
app.include_router(login)
