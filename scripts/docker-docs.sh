#!/usr/bin/env bash

set -x

: ${DOC_IMG:=f5devcentral/containthedocs:v2.0.2-beta}

exec docker run --rm -it \
  -v $PWD:$PWD --workdir $PWD \
  ${DOCKER_RUN_ARGS} \
  -e "LOCAL_USER_ID=$(id -u)" \
  ${DOC_IMG} "$@"
