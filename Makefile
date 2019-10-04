


export SUB_TAG=twitter-sub
export CELERY_TAG=twitter-celery

# DOCKER
build_sub:
	docker build . -t ${SUB_TAG} -f docker/sub.Dockerfile

run_sub: build_sub
	docker run --env-file .env -it ${SUB_TAG}

build_celery:
	docker build . -t ${CELERY_TAG} -f docker/worker.Dockerfile

run_celery: build_celery
	docker run -it ${CELERY_TAG}

