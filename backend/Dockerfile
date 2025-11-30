FROM python:3.13-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=2.1.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PATH="/opt/poetry/bin:$PATH"

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

# --- ESTÁGIO DE DESENVOLVIMENTO (Instala TUDO, inclusive pytest) ---
FROM base AS dev
COPY pyproject.toml poetry.lock ./
# Aqui NÃO tem o --without dev, então instala pytest, black, isort, etc.
RUN poetry install --no-root 

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

# Cria usuário, mas em DEV as vezes é melhor rodar como root para evitar
# problemas de permissão ao escrever arquivos (como .pytest_cache) no volume montado.
# Se preferir usar usuário, descomente as linhas abaixo.
# RUN addgroup --system --gid 1001 appgroup && adduser --system --uid 1001 --ingroup appgroup appuser
# USER appuser

EXPOSE 8000
# O comando padrão ativa o reload
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


# --- ESTÁGIO DE BUILD DE PRODUÇÃO (Só dependências principais) ---
FROM base AS builder-prod
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --without dev


# --- ESTÁGIO FINAL (PRODUÇÃO) ---
FROM python:3.13-slim AS prod
ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"
WORKDIR /app

# Usuário de segurança para produção
RUN addgroup --system --gid 1001 appgroup && \
    adduser --system --uid 1001 --ingroup appgroup appuser

COPY --from=builder-prod /app/.venv /app/.venv
COPY . .
RUN chown -R appuser:appuser /app

USER appuser
EXPOSE 8000
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]