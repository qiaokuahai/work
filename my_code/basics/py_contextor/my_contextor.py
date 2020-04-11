"""
参照python源码实现一个上下文管理器

"""
from functools import wraps
# from contextlib import contextmanager


class _ContextWorker:

    def __init__(self, func, args, kwargs):
        self.gen = func(*args, **kwargs)

    def __enter__(self):
        print("start")
        return next(self.gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            print("end")
            next(self.gen)
        except:
            if exc_type is None:
                return False
            else:
                print("__exit__ error --->>>")
                raise


def contextmanager(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return _ContextWorker(func, args, kwargs)
    return inner


@contextmanager
def tt():
    # 装饰器里面的业务逻辑需要提前写好但是上下文的逻辑不需要提前写好，具体在写代码的过程中动态添加逻辑，
    # 体现在函数中yield这行代码的上面和下面
    yield


def my_deco(func):
    @wraps(func)
    def inner_wrapper(*args, **kwargs):
        print("start do your process")
        # do your process
        res = func(*args, **kwargs)
        print("do final process")
        # 处理结尾逻辑
        return res
    return inner_wrapper


@my_deco
def tt2():
    print("I am in tt2")


if __name__ == "__main__":
    tt2()
    print("----上面是装饰器，下面是上下文-----")
    print("---装饰器里面的业务逻辑需要提前写好但是上下文的逻辑不需要提前写好，具体在写代码的过程中动态添加逻辑，体现在函数中yield这行代码的上面和下面---")
    with tt() as res:
        # raise Exception()
        print("middle")
