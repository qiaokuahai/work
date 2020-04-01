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
对于list来说，左边是头，右边是尾部
lpush names zhangsan lisi wangwu zhaoliu //  向names这个list中压入两个元素,先push  zhangsan， 再push lisi

llen names

rpop names  //  返回zhangsan

brpop names 10  //移出并获取列表names的最后一个元素， 如果有则返回，如果没有元素则block住，直到10秒结束
返回数据：
    1) "names"
    2) "zhang"

lindex names 0  //获取列表首个元素，注意首个元素是从头部开始，也就是从左边开始。
返回数据：
    "zhaoliu"

lrange names 0 1  //获取下标从0开始到1结束之间的元素，含头又含尾
返回数据：
    1) "zhaoliu"
    2) "wangwu"

lpushx new_names zhang wang li zhao  // !!! 注意，会报错，lpushx的Key后面只能跟一个value,
返回数据：
    (error) ERR wrong number of arguments for 'lpushx' command
    
lpushx new_names zhang  // !!! 不会报错，但是不会向new_names这个list中push元素，只有当new_names存在时才push元素

lrem names 0 lisi  //移除names中所有等于lisi的数据
Redis Lrem 根据参数 COUNT 的值，移除列表中与参数 VALUE 相等的元素。
COUNT 的值可以是以下几种：
count > 0 : 从表头开始向表尾搜索，移除与 VALUE 相等的元素，数量为 COUNT 。
count < 0 : 从表尾开始向表头搜索，移除与 VALUE 相等的元素，数量为 COUNT 的绝对值。
count = 0 : 移除表中所有与 VALUE 相等的值。

lset names 0 helloworld  // 设置第一个位置元素等于helloworld

------------------------
lpush first a b c
lpush second aa bb cc
rpoplpush first second
测试结果：
    127.0.0.1:6379> lrange first 0 100
    1) "c"
    2) "b"
    
    127.0.0.1:6379> lrange second 0 100
    1) "a"
    2) "cc"
    3) "bb"
    4) "aa"
```

###  set
```
sadd myset zhang wang li zhao
scard myset  //获取set中的元素数量
返回数据：
    127.0.0.1:6379> scard myset
    (integer) 4

sadd myset1 zhang wang qian sun
sdiff myset myset1  // 获取myset中有，但是myset1中没有的元素
返回数据：
    127.0.0.1:6379> sdiff myset myset1
    1) "li"
    2) "zhao"

sdiffstore dest_set myset myset1  //获取myset中有，但是myset1中没有的元素,并将元素存到dest_set中
smembers dest_set  // 获取dest_set中的所有成员
返回数据：
    127.0.0.1:6379> smembers dest_set
    1) "li"
    2) "zhao"

sinter myset myset1  // 获取交集
sunion myset myset1  // 获取并集
127.0.0.1:6379> sunion myset myset1
1) "sun"
2) "zhang"
3) "li"
4) "wang"
5) "qian"
6) "zhao"


sismember myset haha // 判断haha是否在myset中

sadd new_set a b c
spop new_set //返回一个集合中的随机元素
测试返回：
    127.0.0.1:6379> spop new_set
    "a"
    
    127.0.0.1:6379> smembers new_set
    1) "c"
    2) "b"

-------------------------------
127.0.0.1:6379> sadd new_set a b c d e f g
(integer) 5
srandmember new_set 3  // 随机返回3个元素，但是不删除
    127.0.0.1:6379> srandmember new_set 3
    1) "f"
    2) "d"
    3) "c"

srem new_set a g  //从new_set中删除a和g两个元素
127.0.0.1:6379> smembers new_set
1) "f"
2) "d"
3) "b"
4) "c"
5) "e"
```



