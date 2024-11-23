# UTMN bot 

## uv

- https://docs.astral.sh/uv/getting-started/features/

```sh
brew install uv

uv init
uv venv --seed
uv add requests python-telegram-bot
uv run utmn_bot.py

uv sync --frozen
```

## docker

- https://hub.docker.com/_/registry

```sh
docker run --rm ghcr.io/astral-sh/uv --help
# docker run --rm -it python:3.13.0-slim-bookworm sh
docker run --rm -it python:3.13.0-alpine3.20 sh

ssh reg.orienteer.ru docker run -d -p 5000:5000 --restart always --name registry registry:2
docker build -t reg.orienteer.ru:5000/utmn_bot:0.0.1 .
docker run --rm -it reg.orienteer.ru:5000/utmn_bot:0.0.1
# docker run --rm -it reg.orienteer.ru:5000/utmn_bot:0.0.1 sh

docker push reg.orienteer.ru:5000/utmn_bot:0.0.1

cpc srv/daemon.json vpn:/etc/docker/daemon.json
ssh reg.orienteer.ru systemctl restart docker

ssh reg.orienteer.ru docker run -d --restart always --name bot reg.orienteer.ru:5000/utmn_bot:0.0.1
ssh reg.orienteer.ru docker stop bot
ssh reg.orienteer.ru docker start bot
ssh reg.orienteer.ru docker ps -a

set -Ux UTMN_TL_TOKEN 78..:..
```

```json
{"insecure-registries" : [ "reg.orienteer.ru:5000" ],}
```
