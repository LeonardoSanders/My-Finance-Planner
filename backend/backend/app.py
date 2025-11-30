# /******************************************************************************
# * Nome do Arquivo: app.py
# * Projeto: My Finance Planner
# * Descrição: Inicializa a aplicação
# * Data da Última Modificação: 29/12/2025
# ******************************************************************************/

from http import HTTPStatus

from fastapi import FastAPI

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK)
async def reed_root():
    return {"message": "Welcome to My Finance Planner!"}
