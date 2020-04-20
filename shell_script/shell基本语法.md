###  说明
```
shell是相当不规范的一门脚本语言
针对 数字型、字符串、文件类型 三种类型有不同的运算符，注意！！！

```

### shell 注意事项
```
单引号字符串和双引号字符串
单引号：
1. 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
2. 单引号字串中不能出现单独一个的单引号（对单引号使用转义符后也不行），但可成对出现，作为字符串拼接使用。

双引号：
1. 双引号里可以有变量
2. 双引号里可以出现转义字符

获取字符串长度
string="abcd"
echo ${#string} #输出 4

Shell 数组：
数组名=(值1 值2 ... 值n)
array_name=(value0 value1 value2 value3)

读取数组元素值的一般格式是：
${数组名[下标]}
例如：
valuen=${array_name[n]}

使用 @ 符号可以获取数组中的所有元素，例如：
echo ${array_name[@]}

# 取得数组元素的个数
length=${#array_name[@]}


获取数组长度的方法与获取字符串长度的方法相同，例如：

# 取得数组元素的个数
length=${#array_name[@]}
# 或者
length=${#array_name[*]}
# 取得数组单个元素的长度
lengthn=${#array_name[n]}

注释：
:<<EOF
注释内容...
注释内容...
注释内容...
EOF

$* 和 $@ 的区别
$* 与 $@ 区别：

相同点：都是引用所有参数。
不同点：只有在双引号中体现出来。假设在脚本运行时写了三个参数 1、2、3，，则 " * " 等价于 "1 2 3"（传递了一个参数），而 "@" 等价于 "1" "2" "3"（传递了三个参数）。

#!/bin/bash

echo "-- \$* 演示 ---"
for i in "$*"; do
    echo $i
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
    echo $i
done
```

### 运算符
```
关系运算符
关系运算符只支持数字，不支持字符串，除非字符串的值是数字。
下表列出了常用的关系运算符，假定变量 a 为 10，变量 b 为 20：

运算符	说明	举例
-eq	检测两个数是否相等，相等返回 true。	[ $a -eq $b ] 返回 false。
-ne	检测两个数是否不相等，不相等返回 true。	[ $a -ne $b ] 返回 true。
-gt	检测左边的数是否大于右边的，如果是，则返回 true。	[ $a -gt $b ] 返回 false。
-lt	检测左边的数是否小于右边的，如果是，则返回 true。	[ $a -lt $b ] 返回 true。
-ge	检测左边的数是否大于等于右边的，如果是，则返回 true。	[ $a -ge $b ] 返回 false。
-le	检测左边的数是否小于等于右边的，如果是，则返回 true。	[ $a -le $b ] 返回 true。

```

###  bool运算符
```
下表列出了常用的布尔运算符，假定变量 a 为 10，变量 b 为 20：

运算符	说明	举例
!	非运算，表达式为 true 则返回 false，否则返回 true。	[ ! false ] 返回 true。
-o	或运算，有一个表达式为 true 则返回 true。	[ $a -lt 20 -o $b -gt 100 ] 返回 true。
-a	与运算，两个表达式都为 true 才返回 true。	[ $a -lt 20 -a $b -gt 100 ] 返回 false。
```

###  注意
```
数值的相等比较使用 ==
字符串的相等比较使用 =

```

###  逻辑运算符
```
Shell 的逻辑运算符，假定变量 a 为 10，变量 b 为 20:

运算符	说明	举例
&&	逻辑的 AND	[[ $a -lt 100 && $b -gt 100 ]] 返回 false
||	逻辑的 OR	[[ $a -lt 100 || $b -gt 100 ]] 返回 true
!!!!!!!! 需要特别注意的是： if的判断条件需要用[[ ]]，注意！！！
```

### 字符串运算符,注意和数字运算符的区别
```
字符串运算符
下表列出了常用的字符串运算符，假定变量 a 为 "abc"，变量 b 为 "efg"：

运算符	说明	举例
=	检测两个字符串是否相等，相等返回 true。	[ $a = $b ] 返回 false。
!=	检测两个字符串是否相等，不相等返回 true。	[ $a != $b ] 返回 true。
-z	检测字符串长度是否为0，为0返回 true。	[ -z $a ] 返回 false。
-n	检测字符串长度是否不为 0，不为 0 返回 true。	[ -n "$a" ] 返回 true。
$	检测字符串是否为空，不为空返回 true。	[ $a ] 返回 true。

```

### 文件运算符
```
文件测试运算符
文件测试运算符用于检测 Unix 文件的各种属性。

属性检测描述如下：

操作符	说明	举例
-b file	检测文件是否是块设备文件，如果是，则返回 true。	[ -b $file ] 返回 false。
-c file	检测文件是否是字符设备文件，如果是，则返回 true。	[ -c $file ] 返回 false。
-d file	检测文件是否是目录，如果是，则返回 true。	[ -d $file ] 返回 false。
-f file	检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。	[ -f $file ] 返回 true。
-g file	检测文件是否设置了 SGID 位，如果是，则返回 true。	[ -g $file ] 返回 false。
-k file	检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。	[ -k $file ] 返回 false。
-p file	检测文件是否是有名管道，如果是，则返回 true。	[ -p $file ] 返回 false。
-u file	检测文件是否设置了 SUID 位，如果是，则返回 true。	[ -u $file ] 返回 false。
-r file	检测文件是否可读，如果是，则返回 true。	[ -r $file ] 返回 true。
-w file	检测文件是否可写，如果是，则返回 true。	[ -w $file ] 返回 true。
-x file	检测文件是否可执行，如果是，则返回 true。	[ -x $file ] 返回 true。
-s file	检测文件是否为空（文件大小是否大于0），不为空返回 true。	[ -s $file ] 返回 true。
-e file	检测文件（包括目录）是否存在，如果是，则返回 true。	[ -e $file ] 返回 true。

```

### 控制语句
```
if判断：

a=10
b=20
if [ $a == $b ]
then
   echo "a 等于 b"
elif [ $a -gt $b ]
then
   echo "a 大于 b"
elif [ $a -lt $b ]
then
   echo "a 小于 b"
else
   echo "没有符合的条件"
fi



```





























