include .env

server = reg.orienteer.ru
image = $(server):5000/utmn_bot:$(VER)
ssh_docker = ssh $(server) docker
name = bot

main: build deploy
echo:
	@echo VER=$(VER)
build:
	docker build --push -t $(image) .
deploy:
	$(ssh_docker) rm $(name) --force
	$(ssh_docker) run -d --restart always --name $(name) $(image)
