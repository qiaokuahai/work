### top命令
```
[root@VM_0_6_centos ~]# top
top - 22:58:49 up 77 days,  5:51,  2 users,  load average: 0.00, 0.01, 0.05
Tasks:  88 total,   1 running,  87 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.2 us,  0.2 sy,  0.0 ni, 99.5 id,  0.2 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  3881072 total,   134444 free,  1959472 used,  1787156 buff/cache
KiB Swap:        0 total,        0 free,        0 used.  1646812 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                                                       
 1617 root      20   0  609120  11336   1544 S   0.3  0.3 394:04.25 barad_agent                                                   
16048 redis     20   0  142956   1704    676 S   0.3  0.0  26:32.51 redis-server                                                  
    1 root      20   0  191056   3312   1836 S   0.0  0.1  10:26.56 systemd                                                       
    2 root      20   0       0      0      0 S   0.0  0.0   0:00.63 kthreadd                                                      
    3 root      20   0       0      0      0 S   0.0  0.0   0:45.09 ksoftirqd/0                                                   
    5 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kworker/0:0H                                                  
    7 root      rt   0       0      0      0 S   0.0  0.0   0:17.70 migration/0                                                   
    8 root      20   0       0      0      0 S   0.0  0.0   0:00.00 rcu_bh                                                        
    9 root      20   0       0      0      0 S   0.0  0.0  24:45.45 rcu_sched                                                     
   10 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 lru-add-drain                                                 
   11 root      rt   0       0      0      0 S   0.0  0.0   0:20.34 watchdog/0                                                    
   12 root      rt   0       0      0      0 S   0.0  0.0   0:18.07 watchdog/1                                                    
   13 root      rt   0       0      0      0 S   0.0  0.0   0:17.43 migration/1                                                   
   14 root      20   0       0      0      0 S   0.0  0.0   3:49.77 ksoftirqd/1                                                   
   16 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kworker/1:0H                                                  
   18 root      20   0       0      0      0 S   0.0  0.0   0:00.00 kdevtmpfs  

!!! load average
    多核CPU的话，满负荷状态的数字为 "1.00 * CPU核数"，即双核CPU为2.00，四核CPU为4.00。


首先，我们将它的结果分为两大区域统计信息区和进程信息区

统计信息区

第一行：任务队列信息，与uptime命令执行结果相同。
17:32:34：系统当前时间
up 3 days, 8:04：主机已运行时间
5 users：用户连接数（不是用户数，who命令）
load average: 0.09, 0.12, 0.19：系统平均负载，统计最近1,5,15分钟的系统平均负载
补充：uptime -V可查询版本

第二行：进程信息
Tasks: 287 total：进程总数
2 running：正在运行的进程数
285 sleeping：睡眠的进程数
0 stopped：停止的进程数
0 zombie：僵尸进程数
    
第三行：CPU信息（当有多个CPU时，这些内容可能会超过两行）
1.5 us：用户空间所占CPU百分比
0.9 sy：内核空间占用CPU百分比
0.0 ni：用户进程空间内改变过优先级的进程占用CPU百分比
97.5 id：空闲CPU百分比
0.2 wa：等待输入输出的CPU时间百分比
0.0 hi：硬件CPU中断占用百分比
0.0 si：软中断占用百分比
0.0 st：虚拟机占用百分比

第四行：内存信息（与第五行的信息类似与free命令）
8053444 total：物理内存总量
7779224 used：已使用的内存总量
274220 free：空闲的内存总量（free+used=total）
359212 buffers：用作内核缓存的内存量

第五行：swap信息
8265724 total：交换分区总量
33840 used：已使用的交换分区总量
8231884 free：空闲交换区总量
4358088 cached Mem：缓冲的交换区总量，内存中的内容被换出到交换区，然后又被换入到内存，但是使用过的交换区没有被覆盖，
                    交换区的这些内容已存在于内存中的交换区的大小，相应的内存再次被换出时可不必再对交换区写入。


进程信息区：
PR:优先级
NI:nice值。负值表示高优先级，正值表示低优先级

top使用格式
top [-] [d] [p] [q] [c] [C] [S] [s] [n]

top参数说明
d: 指定每两次屏幕信息刷新之间的时间间隔。当然用户可以使用s交互命令来改变之。
p: 通过指定监控进程ID来仅仅监控某个进程的状态。
q: 该选项将使top没有任何延迟的进行刷新。如果调用程序有超级用户权限，那么top将以尽可能高的优先级运行。
S: 指定累计模式
s: 使top命令在安全模式中运行。这将去除交互命令所带来的潜在危险。
i: 使top不显示任何闲置或者僵死进程。
c: 显示整个命令行而不只是显示命令名
```

# strace 命令
```
我们回到strace的使用上来。strace有两种运行模式。

一种是通过它启动要跟踪的进程。用法很简单，在原本的命令前加上strace即可。
比如我们要跟踪 "ls -lh /var/log/messages" 这个命令的执行，可以这样：

strace ls -lh /var/log/messages
另外一种运行模式，是跟踪已经在运行的进程，在不中断进程执行的情况下，理解它在干嘛。 
这种情况，给strace传递个-p pid 选项即可。

比如，有个在运行的some_server服务，第一步，查看pid:
pidof some_server                      
17553
得到其pid 17553然后就可以用strace跟踪其执行:
strace -p 17553

strace常用选项：
从一个示例命令来看：
strace -tt -T -v -f -e trace=file -o /data/log/strace.log -s 1024 -p 23489

-tt 在每行输出的前面，显示毫秒级别的时间
-T 显示每次系统调用所花费的时间
-v 对于某些相关调用，把完整的环境变量，文件stat结构等打出来。
-f 跟踪目标进程，以及目标进程创建的所有子进程
-e 控制要跟踪的事件和跟踪行为,比如指定要跟踪的系统调用名称
-o 把strace的输出单独写到指定的文件
-s 当系统调用的某个参数是字符串时，最多输出指定长度的内容，默认是32个字节
-p 指定要跟踪的进程pid, 要同时跟踪多个pid, 重复多次-p选项即可。

```
