```
    https://www.cnblogs.com/yyy-blog/p/11073957.html
    
--- 无参数备份数据库mytest和恢复 ---
（1）备份操作
a、备份
mysqldump -uroot -p‘123456’ mytest > /mnt/mytest_bak_$(date +%F).sql

（2）恢复操作
a、删除student表（库必须要保留，空库都行）
mysql -uroot -p'123456' -e "use mytest;drop table student;"
b、恢复数据
mysql -uroot -p'123456' mytest < /mnt/mytest_bak.sql 
c、查看数据
mysql -u root -p'123456' -e "select * from mytest.student;"

--- -B参数备份和恢复（建议使用） ---
（1）备份操作
a、备份
mysqldump -uroot -p'123456' -B mytest > /mnt/mytest_bak_B.sql

说明：加了-B参数后，备份文件中多的Create database和use mytest的命令
加-B参数的好处：
加上-B参数后，导出的数据文件中已存在创建库和使用库的语句，不需要手动在原库是创建库的操作，在恢复过程中不需要手动建库，可以直接还原恢复。

（2）恢复操作
a、删除mytest库
mysql -uroot -p'123456' -e "drop database mytest;"
b、恢复数据
（1）使用不带参数的导出文件导入（导入时不指定要恢复的数据库），报错
mysql -uroot - p'123456' < /mnt/mytest_bak.sql   
ERROR 1046 (3D000) at line 22: No database selected
（2）使用带-B参数的导出文件导入（导入时也不指定要恢复的数据库），成功
mysql -uroot -p'123456' < /mnt/mytest_bak_B.sql 
c、查看数据
mysql -uroot -p'123456' -e "select * from mytest.student;"

--- 指定压缩命令来压缩备份文件 --- 
（1）备份
mysqldump -uroot -p'123456'  -B mytest | gzip > /mnt/mytest_bak_.sql.gz
说明：
mysqldump导出的文件是文本文件，压缩效率很高


```