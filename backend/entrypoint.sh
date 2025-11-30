#!/bin/sh

# Garante que o script pare se um comando falhar
set -e

echo "Aguardando o banco de dados iniciar..."
# Adicionar um sleep ou um wait-for-it.sh aqui é uma boa prática em produção

echo "Aplicando migrações do banco de dados..."
poetry run alembic upgrade head

echo "Iniciando a aplicação..."
# O "$@" executa o comando passado para o script (o CMD do Dockerfile)
exec "$@"