###  创建表
```
drop table if exists userinfo;
create table `userinfo`(
	`id` int(11) unsigned not null auto_increment comment '主键',
	`name` varchar(20) default '' comment '姓名',
	`mobile` char(11) default null comment '手机号码：用定长char更合适',
	`address` varchar(100) default null comment '居住地址：长度可变，使用varchar',
	`desc` text comment '个人介绍：大段文本，不确定长度，使用text类型',
	`sex` char(1) default null comment '或者使用tinyint',
	`age` tinyint(2) unsigned default null comment '年龄不可能超过200岁，不可能是负数',
	`idno` char(18) default null comment '身份证号码',
	`created_at` timestamp not null comment '创建时间',
	primary key(`id`),
	unique key `mobile_idx` (`mobile`) comment '创建名称是mobile_idx的唯一索引',
	unique key `idcard_idx` (`idno`) comment '创建名称是idno_idx的唯一性索引',
	key `name_idx` (`name`) comment '创建名称是name_idx的索引，但没有唯一性约束'
)engine=innodb auto_increment=2 default charset=utf8;

auto_increment=2:  累加步长，一次加2。实际的数据例如： 1  3  5  7
```

###  更改表结构
```
alter table userinfo drop created_at;  // 删除表字段
alter table userinfo add created_at timestamp not null;  //添加表字段
alter table userinfo modify created_at datetime not null;  //更改timestamp类型为datatime类型
alter table userinfo change new_created_at created_at timestamp;  // 更改字段名并且可以更改类型
alter table userinfo rename new_userinfo;  //修改表名
alter table new_userinfo engine=myisam;  //修改存储引擎
alter table new_userinfo drop foreign key your_foreign_key_name;  //删除外键
```

###  索引
```
create index name_address_idx on new_userinfo(name, address);
show index from new_userinfo\G;

```

###  导出数据以及复制表操作
```
导出数据可能会出现 MySQL server is running with the --secure-file-priv option so it cannot execute this statement
修改/etc/my.cnf文件，加入以下配置，指定存放的目录文件。
secure-file-priv=/tmp
select * from new_userinfo into outfile '/tmp/new_userinfo.txt';

复制表操作 
MySQL 数据库不支持 SELECT ... INTO 语句
insert into select from 要求目标表存在。

复制表尽量使用下面的操作,不需要提前创建表
create table auto_new_userinfo as select * from new_userinfo; //复制表以及数据
create table auto_new_userinfo as select * from new_userinfo where 1=2;  //只复制表结构

```

###  mysqldump
```
备份数据：
    // 加入-B 会包含建库语句
    mysqldump -h127.0.0.1 -p3306 -uroot -p123456 -B > ~/tmp_file/just_data.sql  //导出整个数据库包含数据，包含建立库的语句
    mysqldump -h 127.0.0.1 -p3306 -uroot -p123456  test > ~/tmp_file/test.sql  //导出这个库中所有的表结构以及数据，不包含建库语句
    mysqldump -h 127.0.0.1 -p3306 -uroot -p123456  test new_userinfo student > ~/tmp_file/many_table.sql  // 导出多张表的结构以及数据
    
    //加入 -d 指令表示导出表结构，如果不加表示表结构及数据同时导出。
    mysqldump -h 127.0.0.1 -p3306 -uroot -p123456 -d test > ~/tmp_file/test.sql  //只导出test库的表结构
    mysqldump -h 127.0.0.1 -p3306 -uroot -p123456 -d test new_userinfo> ~/tmp_file/new_userinfo.sql  //导出test库下面new_userinfo这张表的表结构
    
    // 加入-t只导出数据
    mysqldump -h127.0.0.1 -p3306 -uroot -p123456 test new_userinfo student -t > ~/tmp_file/just_data.sql  //只导出数据
恢复数据：
    mysql -uroot -p123456 < your.sql  // 这里的your.sql的语句中应该包含建库语句
    mysql -uroot -p123456 test < test.sql  
    或者登陆之后
    使用source your.sql  

```


###  插入insert
```
// 注意， name和desc是mysql中的关键字，所以需要将其加上特殊引号
insert into userinfo (`name`, mobile, address, `desc`, sex, age, idno, created_at)
values
('zhangsan', '13888888888', '深圳', '此人国士无双', '男', 29, '141111198910011223', NOW());
insert into userinfo (`name`, mobile, address, `desc`, sex, age, idno, created_at)
values
('lisi', '13811111111', '北京', '此人不可貌相', '女', 22, '142111198910011223', NOW());
```

###  更新
```
update userinfo 
set address='北京'
where name='zhangsan';

```

###  删除
```
delete from userinfo
where name='zhangsan';

```

###  union  union_all
```
//  union会做去重， union_all不做去重
select * from userinfo
where age>5
union 
select * from userinfo
where age>10;

mysql> select * from userinfo
    -> where age>5
    -> union
    -> select * from userinfo
    -> where age>10;
+----+----------+-------------+---------+--------------------+------+------+--------------------+---------------------+
| id | name     | mobile      | address | desc               | sex  | age  | idno               | created_at          |
+----+----------+-------------+---------+--------------------+------+------+--------------------+---------------------+
|  2 | zhangsan | 13888888888 | 深圳    | 此人国士无双       | 男   |   29 | 141111198910011223 | 2020-04-05 12:27:31 |
|  3 | lisi     | 13811111111 | 北京    | 此人不可貌相       | 女   |   22 | 142111198910011223 | 2020-04-05 12:27:32 |
+----+----------+-------------+---------+--------------------+------+------+--------------------+---------------------+
2 rows in set (0.00 sec)

-------------------------------------------------------------
select * from userinfo
where age>5
union all
select * from userinfo
where age>10;

mysql> select * from userinfo
    -> where age>5
    -> union all
    -> select * from userinfo
    -> where age>10;
+----+----------+-------------+---------+--------------------+------+------+--------------------+---------------------+
| id | name     | mobile      | address | desc               | sex  | age  | idno               | created_at          |
+----+----------+-------------+---------+--------------------+------+------+--------------------+---------------------+
|  2 | zhangsan | 13888888888 | 深圳    | 此人国士无双       | 男   |   29 | 141111198910011223 | 2020-04-05 12:27:31 |
|  3 | lisi     | 13811111111 | 北京    | 此人不可貌相       | 女   |   22 | 142111198910011223 | 2020-04-05 12:27:32 |
|  2 | zhangsan | 13888888888 | 深圳    | 此人国士无双       | 男   |   29 | 141111198910011223 | 2020-04-05 12:27:31 |
|  3 | lisi     | 13811111111 | 北京    | 此人不可貌相       | 女   |   22 | 142111198910011223 | 2020-04-05 12:27:32 |
+----+----------+-------------+---------+--------------------+------+------+--------------------+---------------------+
4 rows in set (0.00 sec)

```
