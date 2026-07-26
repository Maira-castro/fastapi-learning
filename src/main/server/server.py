
#* ambiente separado para fazer as configurações de servidor

from fastapi import FastAPI
from src.main.routes.users_routes import users_routes

app = FastAPI()

app.include_router(users_routes)