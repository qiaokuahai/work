
###  mysql安装与配置(centos7)
```
如果需要更换ali的yum源
mv /etc/yum.repos.d /etc/yum.repos.d.backup
mkdir /etc/yum.repos.d
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
yum clean all
yum makecache
yum update -y  //升级所有的包

如果需要清除缓存并重建缓存：
yum clean all
yum makecache

实际步骤：
    1. wget -i http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm
    2. yum -y install mysql57-community-release-el7-10.noarch.rpm
    3. yum -y install mysql-community-server
    可能会导致速度过慢：
        解决方案，手动下载rpm包安装
        cd /var/cache/yum/x86_64/7/mysql80-community/packages
        文件夹下会有这几个缓存包：
            mysql-community-client-5.7.29-1.el7.x86_64.rpm
            mysql-community-common-5.7.29-1.el7.x86_64.rpm
            mysql-community-libs-5.7.29-1.el7.x86_64.rpm
            mysql-community-server-5.7.29-1.el7.x86_64.rpm
        然后去 http://uni.mirrors.163.com/mysql/Downloads/MySQL-5.7/ 这个源下面下载对应的rpm包，进行手动安装。
    4. 配置
        systemctl start  mysqld.service  //先启动mysql
        systemctl status mysqld.service
        
        如果MySQL已经开始正常运行，不过要想进入MySQL还得先找出此时root用户的密码，通过如下命令可以在日志文件中找出密码：
        grep "password" /var/log/mysqld.log  // 查询root的初始密码，例如下面：EFl76w+&Yw)r
        2020-03-21T14:28:54.763846Z 1 [Note] A temporary password is generated for root@localhost: EFl76w+&Yw)r
        mysql -uroot -p
        然后输入密码：EFl76w+&Yw)r
        
        // 下面两句mysql指令关闭密码的复杂性验证，可以直接设置123456之类的简单密码
        set global validate_password_policy=0;
        set global validate_password_length=1;
        
        // 设置root密码为 123456
        ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';
        
        // 此时数据库还不能远程访问，下面指令赋予root用户所有权限，包括远程登录
        GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
    
    // 以下为补充，非必要步骤
        
    5. mysql --version 5.7.29, 创建表的时候会报出1055的错误
    [Err] 1055 - Expression #1 of ORDER BY clause is not in GROUP BY clause and contains nonaggregated column 'information_schema.PROFILING.SEQ' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
    解决方法：在my.cnf 里面设置sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'在sql_mode 中去掉only_full_group_by 解决问题！
    关于sql_mode的介绍： https://my.oschina.net/u/3083563/blog/2032397
    
    6. navicat刷新卡顿，缓慢的解决方法，设置一下navicat当前这个连接的间隔配置。将240改为30。
    我试了连接其他数据库，貌似这个问题不明显！只有连接这一个数据库出现类似问题！最终找到原因了！
    Mysql服务器端会定时清理长时间不活跃空闲的数据库连接，以此优化数据库的性能。
    Navicat客户端有一个设置：保持连接间隔，默认是240秒！意思是，客户端在用户无任何交互性操作时，会每隔240秒给Mysql服务端发送一次数据请求。以此来保持数据库连接活跃！
    然而Navicat设置的心跳包间隔太长了，Mysql服务端直接将连接清理掉了。当我们打开一张表的时候，Navicat还是使用旧的连接去请求数据，发现旧的连接超时不能用了，最后又申请了一个新的连接，再去请求数据！
    所以导致我们打开一张表时间需要挺久的！

```