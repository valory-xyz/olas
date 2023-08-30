build:
ifndef DOCKER_AUTH
	$(error DOCKER_AUTH is undefined)
endif
	skaffold build --default-repo docker.io/valory

deploy:
ifndef DOCKER_AUTH
	$(error DOCKER_AUTH is undefined)
endif
ifndef KUBECONFIG
	$(error KUBECONFIG is undefined)
endif
ifndef OLAS_API_HOSTNAME
	$(error OLAS_API_HOSTNAME is undefined)
endif
ifndef OLAS_API_ALCHEMY_API_KEY
	$(error OLAS_API_ALCHEMY_API_KEY is undefined)
endif
	skaffold run --default-repo docker.io/valory

