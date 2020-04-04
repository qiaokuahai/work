###  datetime 和 timestamp

```
1. 存储范围不同：datetime的存储范围是 1000-01-01 00:00:00.000000 到 9999-12-31 23:59:59.999999，而timestamp的范围是 
1970-01-01 00:00:01.000000 到 2038-01-19 03:14:07.999999；

2. datetime存储与时区无关，而timestamp存储的是与时区有关，这也是两者最大的不同。MySql在存储timestamp时会先将时间转为
UTC（世界协调时）进行存储，然后查询的时候再从UTC转为当前的时区进行返回。也就是说使用timestamp进行存储的时间返回的时候
会随着数据库的时区而发生改变。而datetime的存储则与时区无关，数据是什么，就存储什么，也就返回什么。

3. datetime适用于记录数据的创建时间，因为这个时间是不会变的。而timestamp有自动修改更新的功能，也就是说，我们对表里的其他
数据进行修改，timestamp修饰的字段会自动更新为当前的时间，这个特性称为自动初始化和自动更新(Automatic Initialization and
 Updating)。所以timestamp适用于那种记录数据的最后修改时间的字段。当然，我们也可以设置timestamp不自动更新，通过设置 
 explicit_defaults_for_timestamp配置，从OFF设置为ON 来实现。从MySql5.6.5之后，Automatic Initialization and Updating这种
 特性不但适用于timestamp，也适用于datetime了。并且以前MySql版本要求同一张表中满足该特性的timestamp只能有一个字段，而现在
 也不再限制数量了。

4. 时区信息是MySql的系统变量，我们可以通过 show variables like '%time_zone%' 来获取mysql的时区信息，默认值一般是 SYSTEM，
即服务器的时区。

5. 修改当前会话的时区只会影响到当前连接，如果再开一个连接，时区将仍是mysql默认时区。如果要修改整个mysql的时区，可以有多
种方式，比如修改my.ini配置等，然后记得重启即可。

```


