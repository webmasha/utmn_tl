include .env

server = reg.orienteer.ru
image = $(server):5000/$(SRV):$(VER)
ssh_docker = ssh $(server) docker
args_run = -e UTMN_TL_TOKEN=$$UTMN_TL_TOKEN -e UTMN_TL_BOT_NAME=$$UTMN_TL_BOT_NAME -e UTMN_TL_JWT=$$UTMN_TL_JWT
args_build = --push

main: build run
echo:
	@echo VER=$(VER)
build:
	docker build $(args_build) --tag $(image) --build-arg SRV=$(SRV) .
ssh-up: ssh-down
	$(ssh_docker) run $(args_run) -d --restart always --name $(SRV) $(image)
ssh-down:
	$(ssh_docker) rm $(SRV) --force ||:
ssh-ps:
	$(ssh_docker) ps
run_cmd = docker run $(args_run) -v $$PWD/bot.py:/app/bot.py --rm -it --name $(SRV) $(image)
run:
	$(run_cmd)
run-sh:
	$(run_cmd) sh
set_jwt:
	fish -c "set -Ux UTMN_TL_JWT (cat modeus/tmp/jwt.txt)"
