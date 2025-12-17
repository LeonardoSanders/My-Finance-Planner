# /******************************************************************************
# * Nome do Arquivo: environments.py
# * Projeto: My Finance Planner
# * Descrição: Variaveis de ambiente do Postgres
# * Data da Última Modificação: 08/12/2025
# ******************************************************************************/
import os

from dotenv import load_dotenv

load_dotenv()


POSTGRESDB_URL = os.getenv("POSTGRESDB_URL", "")
