```
DML执行流程(从数据完全取到内存后开始)：
数据页到内存中-->修改数据-->更新数据页-->写入redolog，状态为prepare-->写binlog-->提交事务，redolog状态修改为commit

在做Crash recovery时：
binlog有记录，redolog状态commit：正常完成的事务，不需要恢复
binlog有记录，redolog状态prepare：在binlog写完提交事务之前的crash，恢复操作：提交事务
binlog无记录，redolog状态prepare：在binlog写完之前的crash，恢复操作：回滚事务
binlog无记录，redolog无记录：在redolog写之前crash，恢复操作：回滚事务

可以看出来在这种"两阶段提交"下事务的提交or回滚是由binlog决定的，可以理解为靠binlog做判断，靠redo log做恢复操作
```