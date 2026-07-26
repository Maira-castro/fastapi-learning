from fastapi import APIRouter #responsavel para criar as rotas
from fastapi.responses import JSONResponse #ajuda a enviar respostas pelo fastapi

#*criando um conjunto de rotas
users_routes = APIRouter(tags=["Usuários"])

@users_routes.post('/users')
async def criar_usuario():
    return JSONResponse(
        content={"ola":"mundo"},
        status_code=200
    )