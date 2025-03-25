#!/bin/bash
# 取得 build.sh 所在的目錄（也就是 docker 目錄）
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 取得專案根目錄
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# 設定正確的 build 指令
cmd="DOCKER_BUILDKIT=1 docker build -t chenhung0506/python-grpc:latest -f $SCRIPT_DIR/Dockerfile $PROJECT_ROOT --no-cache"

echo $cmd
eval $cmd
