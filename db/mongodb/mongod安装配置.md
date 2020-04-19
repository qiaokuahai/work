```
https://www.runoob.com/mongodb/mongodb-linux-install.html  //到官网下载想安装的版本

curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.0.6.tgz    # 下载
tar -zxvf mongodb-linux-x86_64-3.0.6.tgz                                   # 解压
mv  mongodb-linux-x86_64-3.0.6/ /usr/local/mongodb                         # 将解压包拷贝到指定目录

// 将mongo的bin路径配置到环境变量中
vim ~/.bash_profile
PATH=$PATH:/usr/local/mongodb/bin

```
### 配置文件
vim /etc/mongodb.conf
```
# 远程访问
bind_ip=0.0.0.0
port=27017
# 关闭密码验证
auth=false
# 日志路径
logpath=/var/log/mongodblog/mongo.log
# 设置日志方式为追加
logappend=true
# 数据存储路径
dbpath=/data/db/mongodb
# 后台启动
fork=true
# 每个数据库一个文件夹
directoryperdb=true
```
### 启动
```
mongod -f /etc/mongodb.conf
```
