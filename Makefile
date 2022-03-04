tag = $(shell cat .tag)

gen_tag:
	date +"%Y%m%d%H%M" > .tag

docker: gen_tag
	docker build -t tmm:latest -t blubeyondregistry.azurecr.io/tmm:$(tag) .

push:
	docker push blubeyondregistry.azurecr.io/tmm:$(tag)

