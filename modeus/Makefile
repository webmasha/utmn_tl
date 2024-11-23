include .env

server = reg.orienteer.ru
image = $(server):5000/$(SRV):$(VER)
ssh_docker = ssh $(server) docker
name = bot
args_run = -e MODEUS_LOGIN=$$MODEUS_LOGIN -e MODEUS_PASSWORD=$$MODEUS_PASSWORD -e MODEUS_REMOTE=192.168.0.9
# args_build = --push

main: build run
# main: build deploy
echo:
	@echo VER=$(VER)
build:
	docker build $(args_build) --tag $(image) --build-arg SRV=$(SRV) .
deploy:
	$(ssh_docker) rm $(name) --force
	$(ssh_docker) run -d --restart always --name $(name) $(image)
run:
	docker run $(args_run) --rm -it --name $(SRV) $(image)

selenium_up:
	docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" --name selenium selenium/standalone-chrome:latest
selenium_down:
	docker rm selenium --force
