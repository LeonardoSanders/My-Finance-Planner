# /******************************************************************************
# * Nome do Arquivo: environments.py
# * Projeto: My Finance Planner
# * Descrição: Variaveis de ambiente do Projeto
# * Data da Última Modificação: 29/12/2025
# ******************************************************************************/
import os

from dotenv import load_dotenv

load_dotenv()


POSTGRESDB_URL = os.getenv("POSTGRESDB_URL", "")
