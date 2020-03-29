###  redis常用数据结构

```
type key  //查看当前的key是什么类型

```

####  string 
```
set name zhangsan  
del name
exists name  //存在返回1，不存在返回0
expire name 15  //给name这个key设置15秒过期时间，成功返回1
persist name  //删除name的过期时间
ttl name  //返回name的剩余过期时间(单位秒)，如果没有过期时间返回-1，否则返回剩余秒数
rename name new_name  //将name这个key的名称修改为new_name

setnx name lisi  //如果name不存在，返回1，更新成功，如果name已经存在返回0，不进行更新
```

####  hash
```
Redis 中每个 hash 可以存储 232 - 1 键值对（40多亿）
hset tenant project1 50
hset tenant project2 70
hget tenant project1

hgetall tenant
返回数据为：  
    1) "project1"
    2) "50"
    3) "project2"
    4) "70"
    
hkeys tenant   //  获取当前key下所有的field
返回数据为：
    1) "project1"
    2) "project2"
    
hvals tenant  //  获取key下所有的value,重复的值也会返回
    1) "111"
    2) "222"
    3) "100"
    4) "000"
    5) "000"
    
hlen tenant

hmget tenant project1 project2  //  批量获取key下对应field的值
返回数据：
    1) "50"
    2) "70"

hmset tenant project1 111 project2 222  //批量更新

hsetnx tenant project4 000  //  当project4不存在，返回1，更新成功。否则返回0

```

###  list
```

```



