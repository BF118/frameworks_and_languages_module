DOCKER_IMAGE:=server

	
build:
	docker build --tag ${DOCKER_IMAGE} .

test:
	docker run --rm ${DOCKER_IMAGE}
run:
	docker run -it --rm --publish 8000:8000 ${DOCKER_IMAGE}
run_local:
	python3 -m http.server 8000
	python3 app.py