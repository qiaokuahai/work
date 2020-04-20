```
1. ulimit -n  //查看用户句柄限制
[root@VM_0_6_centos 32346]# ulimit -n
100001

2. cat /proc/[pid]/limits  //查看某一个进程的句柄配置情况
// 查看本机nginx主进程的limit情况
[root@VM_0_6_centos 32346]# cat /proc/32346/limits
Limit                     Soft Limit           Hard Limit           Units     
Max cpu time              unlimited            unlimited            seconds   
Max file size             unlimited            unlimited            bytes     
Max data size             unlimited            unlimited            bytes     
Max stack size            8388608              unlimited            bytes     
Max core file size        0                    unlimited            bytes     
Max resident set          unlimited            unlimited            bytes     
Max processes             15076                15076                processes 
Max open files            1024                 4096                 files     
Max locked memory         65536                65536                bytes     
Max address space         unlimited            unlimited            bytes     
Max file locks            unlimited            unlimited            locks     
Max pending signals       15076                15076                signals   
Max msgqueue size         819200               819200               bytes     
Max nice priority         0                    0                    
Max realtime priority     0                    0                    
Max realtime timeout      unlimited            unlimited            us   


3. 永久修改打开文件句柄限制 vim /etc/security/limits.conf

4. chown chmod

chown:
例：把目录/his及其下的所有文件和子目录的属主改成wang，属组改成users。
$ chown - R wang.users /his

chmod:
chmod ［who］ ［+ | - | =］ ［mode］ 文件名

　　命令中各选项的含义为：
　　操作对象who可是下述字母中的任一个或者它们的组合：
　　u 表示“用户（user）”，即文件或目录的所有者。
　　g 表示“同组（group）用户”，即与文件属主有相同组ID的所有用户。
　　o 表示“其他（others）用户”。
　　a 表示“所有（all）用户”。它是系统默认值。

　　操作符号可以是：
　　+ 添加某个权限。
　　- 取消某个权限。
　　= 赋予给定权限并取消其他所有权限（如果有的话）。

　　设置mode所表示的权限可用下述字母的任意组合：
　　r 可读。
　　w 可写。
　　x 可执行。
　　X 只有目标文件对某些用户是可执行的或该目标文件是目录时才追加X属性。
　　s 在文件执行时把进程的属主或组ID置为该文件的文件属主。方式“u＋s”设置文件的用户ID位，“g＋s”设置组ID位。
　　t 保存程序的文本到交换设备上。
　　u 与文件属主拥有一样的权限。
　　g 与和文件属主同组的用户拥有一样的权限。
　　o 与其他用户拥有一样的权限。

　　文件名：以空格分开的要改变权限的文件列表，支持通配符。
　　在一个命令行中可给出多个权限方式，其间用逗号隔开。例如：chmod g+r，o+r example
　　使同组和其他用户对文件example 有读权限。

5. 杀掉包含指定名字的进程，例如nginx
ps -ef | grep nginx | grep -v grep | awk '{print $2}' | xargs kill -9

```