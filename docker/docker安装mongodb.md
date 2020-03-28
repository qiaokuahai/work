###  docker启动并且初始化mongodb
```
rm -rf /opt/data/docker/mongodb
mkdir -p /opt/data/docker/mongodb
chmod -R 777 /opt/data/docker

// 启动并且创建了一个根用户 admin， 密码是： 123456, 可以不加 --auth
docker run -itd --name mongo -v /opt/data/docker/mongodb:/data/db -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=123456 mongo --auth
```


###  其他参考
```
容器启动mongodb命令：
 docker run -d --name mongodb_docker -v /root/mongodb_docker/db:/data/db -p 27017:27017  -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=123456 mongo

容器连接mongodb命令： 
docker run -it --rm --link mongodb_docker:mongo mongo mongo --host mongo -u admin -p admin --authenticationDatabase admin

创建数据库 ：
use weasel；

创建用户 ：
> db.createUser(
... {
... user:"weasel",
... pwd:"weasel123",
... roles: [{ role:"readWrite" , db: "weasel"}]
... });

使用新用户连接：　
docker run -it --rm --link mongodb_docker:mongo mongo mongo --host mongo -u weasel -p weasel123 --authenticationDatabase weasel　

使用：
use weasel;

> db.test2.insert({"cc":"123", "das":'123444444'});
WriteResult({ "nInserted" : 1 })
> 
> db.test2.count()
1
> 
> db.test2
db.test2
> db.test2.find({"cc":'123'});
{ "_id" : ObjectId("5b4c3b24099d1b0ef30cc0fb"), "cc" : "123", "das" : "123444444" }

```