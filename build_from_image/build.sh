#!/bin/bash
cmd="DOCKER_BUILDKIT=1 docker build -t chenhung0506/python-with-chrome:latest -f ~/linebot-linux/build_from_image/Dockerfile $( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $cmd
eval $cmd
