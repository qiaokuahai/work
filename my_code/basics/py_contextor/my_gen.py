# 生成器
# 注意：当一个函数中有yield的时候，就是一个生成器，当第一次执行的时候，不会执行里面的代码，只是返回一个可迭代对象
# 当执行next()的时候才开始执行函数中的具体代码。
# 理解了这一点，python中的contextmanager中就很好理解了。

# 可以直接点进去看源码
from contextlib import contextmanager


def my_gen():
    print("before yield")
    yield 1
    print("after yield")


res = my_gen()
for i in range(2):
    next(res)
