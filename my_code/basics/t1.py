class A:
    name = "zhangsan"


def tt():
    o = eval("A()")
    o.name = "lisi"
    o1 = A()
    print(o.name)
    print(o1.name)


tt()
