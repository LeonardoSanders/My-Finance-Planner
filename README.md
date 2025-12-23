# Comandos úteis

## Comandos para rodar a aplicação local

- pipx inject poetry poetry-plugin-shell
- poetry shell
- task run

## Comandos para rodar o script de formatação

- chmod +x ./lint.sh
- poetry run ./lint.sh ou ./lint.sh

## Comandos para rodar a aplicação completa (Backend + Postgres)

- alembic init migrations
- alembic upgrade head
- chmod +x backend/entrypoint.sh
- git update-index --chmod=+x entrypoint.sh
- docker compose up --build
