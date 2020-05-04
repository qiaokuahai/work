### 第一种并发方式（workers 模式，又名 UNIX 进程模式）
```
每个 worker 都是一个加载 Python 应用程序的 UNIX 进程。worker 之间没有共享内存。
建议的 workers 数量是 (2*CPU)+1。
对于一个双核（两个CPU）机器，5 就是建议的 worker 数量。

```