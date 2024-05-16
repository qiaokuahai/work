
global_dict = {}


def outer(name):
    global_dict[name] = name
    def deco(func):
        def inner(*args, **kwargs):
            print("---start")
            res = func(*args, **kwargs)
            print("---end")
            return res
        return inner
    print(global_dict)
    return deco


@outer("zhangsan")
def p():
    print("hello")

p()

