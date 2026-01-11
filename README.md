# Instruções de Instalação e Utilização

## Serviços

- Python versão 3.12 ou maior
- Node versão 14 ou maior
- Angular CLI versão 20.3.10
- Docker
- Git

## Comandos para rodar o backend local

- pipx inject poetry poetry-plugin-shell
- poetry shell
- task run

## Comandos para rodar o script de formatação do backend

- chmod +x ./lint.sh
- poetry run ./lint.sh ou ./lint.sh

## Comandos para rodar o frontend local

- npm install
- ng serve / npm run start

## Comandos para rodar a aplicação completa (Backend + Frontend + Postgres)

- alembic init migrations
- alembic upgrade head
- chmod +x backend/entrypoint.sh
- git update-index --chmod=+x entrypoint.sh
- docker compose up --build
