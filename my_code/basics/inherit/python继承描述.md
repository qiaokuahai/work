```
// 不要一说到 super 就想到父类！super 指的是 MRO 中的下一个类！！！
// 实际的super(your_cls_name, self), 做了如下动作
def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]

两个参数 cls 和 inst 分别做了两件事： 
1. inst 负责生成 MRO 的 list 
2. 通过 cls 定位当前 MRO 中的 index, 并返回 mro[index + 1] 
这两件事才是 super 的实质，一定要记住！ 

具体对比 cls_inherit.py和cls_inherit_new的执行不同。

参考博客 https://laike9m.com/blog/li-jie-python-super,70/
```