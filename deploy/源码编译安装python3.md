```
官网下载对应版本源码 https://www.python.org/downloads/source/
本次下载的版本  Python-3.6.8.tgz
cd到存放目录下：
tar -xzvf Python-3.6.8.tgz
cd Python-3.6.8/
./configure --prefix=/usr/local/python36
make && make install
// 将python的bin路径放到当前用户环境变量中，生效配置文件

vim ~/.bash_profile
PATH=$PATH:/usr/local/python36/bin
source ~/.bash_profile

```