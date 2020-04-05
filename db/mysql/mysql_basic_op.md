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
