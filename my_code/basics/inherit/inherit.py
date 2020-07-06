class A:
    name = "zhangsan"


class B(A):
    pass


class C(A):
    pass


if __name__ == "__main__":
    print(A.name, B.name, C.name)
    B.name = "lisi"
    print(A.name, B.name, C.name)
    A.name = "wangwu"
    print(A.name, B.name, C.name)

