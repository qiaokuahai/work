###  删除所有已经停止的容器
docker rm -v $(docker ps -aq -f status=exited)

###  强行删除正在运行的容器
docker rm -f your_container_name

###  启动容器

### 进入容器

