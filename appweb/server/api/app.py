from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.routesUser import user
from routes.routesLogin import login

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(login)
