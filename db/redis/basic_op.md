### 特别说明
```
redis 迭代命令SCAN、SSCAN、HSCAN、ZSCAN
SCAN 命令用于迭代当前数据库中的数据库键。
SSCAN 命令用于迭代集合键中的元素。
HSCAN 命令用于迭代哈希键中的键值对。
ZSCAN 命令用于迭代有序集合中的元素（包括元素成员和元素分值）
SCAN、SSCAN、HSCAN、ZSCAN每次执行都只会返回少量元素，所以这些命令可以用于生产环境，而不会出现像KEYS、SMEMBERS命令带来的问题，
当KEYS命令被用于处理一个大的数据库时，又或者SMEMBERS命令被用于处理一个大的集合键时，它们可能会阻塞服务器达数秒之久
```

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

### sorted_set
```
zadd name_zset 1 zhangsan
zadd name_zset 3 lisi
zadd name_zset 2 wangwang

zcard name_zset
127.0.0.1:6379> zcard name_zset
(integer) 3

zcount name_zset 2 3  // 返回指定分数区间元素的个数，含头也含尾
127.0.0.1:6379> zcount name_zset 2 3
(integer) 2

zrange name_zset 0 1  //  返回指定索引区间的元素，含头也含尾
127.0.0.1:6379> zrange name_zset 0 1
1) "zhangsan"
2) "wangwang"

zrange name_zset 0 -1 withscores  // 将分数一并返回
127.0.0.1:6379> zrange name_zset 0 -1 withscores
1) "zhangsan"
2) "1"
3) "wangwang"
4) "2"
5) "lisi"
6) "3"

zadd salary 4000 zhangsan
zadd salary 6000 lisi
zadd salary 9000 wangwu
zadd salary 7000 zhaoliu

127.0.0.1:6379> zrange salary 0 -1 withscores
1) "zhangsan"
2) "4000"
3) "lisi"
4) "6000"
5) "zhaoliu"
6) "7000"
7) "wangwu"
8) "9000"

zrangebyscore salary 6000 7000
127.0.0.1:6379> zrangebyscore salary 6000 7000
1) "lisi"
2) "zhaoliu"

zrangebyscore salary 6000 7000 withscores
127.0.0.1:6379> zrangebyscore salary 6000 7000 withscores
1) "lisi"
2) "6000"
3) "zhaoliu"
4) "7000"

zrangebyscore salary -inf 7000 withscores   //获取工资小于等于7000的
127.0.0.1:6379> zrangebyscore salary -inf 7000 withscores
1) "zhangsan"
2) "4000"
3) "lisi"
4) "6000"
5) "zhaoliu"
6) "7000"


127.0.0.1:6379> zrangebyscore salary -inf (7000 withscores  //获取工资小于7000的
1) "zhangsan"
2) "4000"
3) "lisi"
4) "6000"

127.0.0.1:6379> zrangebyscore salary -inf +inf  // 获取全部元素
1) "zhangsan"
2) "lisi"
3) "zhaoliu"
4) "wangwu"

zrank salary zhaoliu  //  返回有序集合中元素的下标索引
127.0.0.1:6379> zrank salary zhaoliu
(integer) 2

zcount salary (6000 (9000   //  返回工资集合中，薪资大于6000小于9000的人的个数
127.0.0.1:6379> zcount salary (6000 (9000
(integer) 1

ZLEXCOUNT key min max  //  有疑问？？？在有序集合中计算指定字典区间内成员数量

zrevrange salary 0 -1 withscores  // 根据索引选取数据，然后根据分数倒序返回
127.0.0.1:6379> zrevrange salary 0 -1 withscores
1) "wangwu"
2) "9000"
3) "zhaoliu"
4) "7000"
5) "lisi"
6) "6000"
7) "zhangsan"
8) "4000"

zrevrangebyscore salary 7000 4000 withscores  // 根据分数范围选取数据，然后根据分数倒序返回
127.0.0.1:6379> zrevrangebyscore salary 7000 4000 withscores
1) "zhaoliu"
2) "7000"
3) "lisi"
4) "6000"
5) "zhangsan"
6) "4000"

----------------------------
127.0.0.1:6379> zrevrange salary 0 -1 withscores
1) "wangwu"
2) "9000"
3) "zhaoliu"
4) "7000"
5) "lisi"
6) "6000"
7) "zhangsan"
8) "4000"

zrevrank salary lisi  //  获取倒序排名中的次序
127.0.0.1:6379> zrevrank salary lisi
(integer) 2
----------------------------

zscore salary lisi  // 获取成员分数
127.0.0.1:6379> zscore salary lisi
"6000"

127.0.0.1:6379> zscan salary 0 
1) "0"
2) 1) "zhangsan"
   2) "4000"
   3) "lisi"
   4) "6000"
   5) "zhaoliu"
   6) "7000"
   7) "wangwu"
   8) "9000"
   
127.0.0.1:6379> zscan salary 0  match z*  // 可以理解为一个迭代器，从索引下标为0开始，value以z开头，按照score排序
1) "0"
2) 1) "zhangsan"
   2) "4000"
   3) "zhaoliu"
   4) "7000"


127.0.0.1:6379> zrange salary 0 -1 withscores
1) "zhangsan"
2) "4000"
3) "lisi"
4) "6000"
5) "zhaoliu"
6) "7000"
7) "wangwu"
8) "9000"

zremrangebyscore salary (6000 7000   //删除分数大于6000小于等于7000的所有元素
127.0.0.1:6379> zremrangebyscore salary (6000 7000 
(integer) 1

127.0.0.1:6379> zrange salary 0 -1 withscores
1) "zhangsan"
2) "4000"
3) "lisi"
4) "6000"
5) "wangwu"
6) "9000"


zremrangebyrank salary 1 2  // 将排名在第二位和第三位的数据删除掉
127.0.0.1:6379> zremrangebyrank salary 1 2
(integer) 2

127.0.0.1:6379> zrange salary 0 -1 withscores
1) "zhangsan"
2) "4000"


zadd salary 10000 hale
127.0.0.1:6379> zrange salary 0 -1 withscores
1) "zhangsan"
2) "4000"
3) "hale"
4) "10000"

zrem salary zhangsan hale  //删除指定元素，可以是多个
127.0.0.1:6379> zrem salary zhangsan hale
(integer) 2

127.0.0.1:6379> zrange salary 0 -1 withscores
(empty list or set)

```


