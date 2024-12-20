FROM python:3.13.0-alpine3.20
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
WORKDIR /app
CMD ["uv", "run", "bot.py"]
ADD . /app
RUN uv sync --frozen
