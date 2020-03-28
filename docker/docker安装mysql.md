#  docker mysql 安装和配置

###  docker下载 mysql
``` 
docker pull mysql:5.7
```

###  启动
```
mkdir -p /opt/data/docker/mysql
chmod -R 777 /opt/data/docker
docker run --name mysql -v /opt/data/docker/mysql:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7
```

###  进入容器
```
docker exec -it mysql bash
```

###  登录mysql
```
mysql -u root -p
ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';
```

###  添加远程登录用户
```
CREATE USER 'hale'@'%' IDENTIFIED WITH mysql_native_password BY '123456';
GRANT ALL PRIVILEGES ON *.* TO 'hale'@'%';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
```