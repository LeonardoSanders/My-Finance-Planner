#!/bin/bash
# Script para rodar todas as verificações de formatação e linting

echo "--- Organizando imports com isort ---"
isort .

echo "--- Formatando código com black ---"
black .

echo "--- Verificando erros com pylint ---"
pylint backend

echo "--- Verificando tipos com pyright ---"
pyright .

echo "--- Verificações concluídas! ---"
