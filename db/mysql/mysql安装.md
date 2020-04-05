
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
        
    5. mysql --version 5.7.29, 创建表的时候会报出1055的错误
    [Err] 1055 - Expression #1 of ORDER BY clause is not in GROUP BY clause and contains nonaggregated column 'information_schema.PROFILING.SEQ' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by
    解决方法：在my.cnf 里面设置sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'在sql_mode 中去掉only_full_group_by 解决问题！
    关于sql_mode的介绍： https://my.oschina.net/u/3083563/blog/2032397

```