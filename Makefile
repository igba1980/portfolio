.PHONY: start kill stop install_kind create_kind_cluster install_kubectl \
	create_docker_registry connect_registry_to_kind_network connect_registry_to_kind \
	create_kind_cluster_with_registry delete_kind_cluster delete_local_registry install_app

start:
	docker-compose run --rm web

kill:
	docker-compose down -v --remove-orphans

stop:
	docker-compose stop web
	docker-compose down --remove-orphans

install_kind:
	curl --location --output ./kind https://github.com/kubernetes-sigs/kind/releases/download/v0.17.0/kind-darwin-arm64 && \
		./kind --version

create_kind_cluster: install_kind install_kubectl create_docker_registry
	./kind create cluster --name portfolio --config ./kind_config.yaml || true && \
		kubectl get nodes

install_kubectl:
	brew install kubectl

create_docker_registry:
	if docker ps -a | grep -q 'local-registry'; \
	then echo "---> local-registry already created; skipping"; \
	else docker run -d --name local-registry -d --restart=always -p "127.0.0.1:5000:5000" registry; \
	fi

connect_registry_to_kind_network:
	docker network connect kind local-registry || true

connect_registry_to_kind: connect_registry_to_kind_network
	kubectl apply -f ./kind_configmap.yaml

create_kind_cluster_with_registry:
	$(MAKE) create_kind_cluster && $(MAKE) connect_registry_to_kind

delete_kind_cluster: delete_local_registry
	./kind delete cluster

delete_local_registry:
	docker stop local-registry && docker rm local-registry

install_app:
	helm upgrade --atomic --install portfolio-website ./chart
