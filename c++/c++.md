```
1、安装centos-release-scl
sudo yum install centos-release-scl
2、安装devtoolset，注意，如果想安装7.*版本的，就改成devtoolset-7-gcc*，以此类推
sudo yum install devtoolset-8-gcc*
3、激活对应的devtoolset，所以你可以一次安装多个版本的devtoolset，需要的时候用下面这条命令切换到对应的版本
scl enable devtoolset-8 bash
大功告成，查看一下gcc版本
gcc -v

每个版本的目录下面都有个 enable 文件，如果需要启用某个版本，只需要执行
source ./enable
所以要想切换到某个版本，只需要执行
source /opt/rh/devtoolset-8/enable

4、直接替换旧的gcc
旧的gcc是运行的 /usr/bin/gcc，所以将该目录下的gcc/g++替换为刚安装的新版本gcc软连接，免得每次enable
mv /usr/bin/gcc /usr/bin/gcc-4.8.5
ln -s /opt/rh/devtoolset-8/root/bin/gcc /usr/bin/gcc
mv /usr/bin/g++ /usr/bin/g++-4.8.5
ln -s /opt/rh/devtoolset-8/root/bin/g++ /usr/bin/g++
gcc --version
g++ --version

```