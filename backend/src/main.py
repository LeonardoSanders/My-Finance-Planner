# /******************************************************************************
# * Nome do Arquivo: app.py
# * Projeto: My Finance Planner
# * Descrição: Inicializa a aplicação
# * Data da Última Modificação: 29/12/2025
# ******************************************************************************/

from http import HTTPStatus

from fastapi import FastAPI

from .config.database.models import table_registry
from .modules.auth.controller import router as auth
from .modules.users.controller import router as users

app = FastAPI(title="My Finance Planner")

app.include_router(auth)
app.include_router(users)


@app.get("/", status_code=HTTPStatus.OK)
async def reed_root():
    return {"message": "Welcome to My Finance Planner!"}
