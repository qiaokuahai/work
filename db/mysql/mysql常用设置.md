1. 开启慢查询日志： set global slow_query_log = on;

2. 设置慢查询时间： set global long_query_time = 1;  //单位秒

3. 慢查询日志的路径默认是 MySQL 的数据目录

mysql> show global variables like "datadir";

```
+---------------+------------------------+
| Variable_name | Value                  |
+---------------+------------------------+
| datadir       | /data/mysql/data/3306/ |
+---------------+------------------------+

```
