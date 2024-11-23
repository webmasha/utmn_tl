include .env

server = reg.orienteer.ru
image = $(server):5000/$(SRV):$(VER)
ssh_docker = ssh $(server) docker
args_run = -e UTMN_TL_TOKEN=$$UTMN_TL_TOKEN -e UTMN_TL_BOT_NAME=${UTMN_TL_BOT_NAME}
# args_build = --push

main: build run
# main: build ssh-up
echo:
	@echo VER=$(VER)
build:
	docker build $(args_build) --tag $(image) --build-arg SRV=$(SRV) .
ssh-up: down
	$(ssh_docker) run -d --restart always --name $(SRV) $(image)
ssh-down:
	$(ssh_docker) rm $(SRV) --force
run:
	docker run $(args_run) -v $$PWD/utmn_tl.py:/app/utmn_tl.py --rm -it --name $(SRV) $(image)
