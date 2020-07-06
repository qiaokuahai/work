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


# def my_test():
#     print("before yield")
#     yield "zhangsan"
#     print("after yield")
#
#
# for x in my_test():
#     print(x)


@contextmanager
def tt():
    # 体现在函数中yield这行代码的上面和下面
    print("before yield")
    yield
    print("after yield")


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
    print("---对比装饰器，上下文更加灵活，可以在代码中任何地方插入---")
    with tt() as res:
        # raise Exception()
        print("middle")
