# FROM python:3.13.0-slim-bookworm
FROM python:3.13.0-alpine3.20
# COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Copy the project into the image
ADD . /app

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app
RUN uv sync --frozen

# Presuming there is a `my_app` command provided by the project
CMD ["uv", "run", "utmn_bot.py"]
