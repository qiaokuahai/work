class Base:
    _base_lock = "base_lock"

    def __init__(self, base_name="base_name"):
        print("enter Base")
        self.base_name = base_name
        print("leave Base")

    def call(self):
        print("Base call()")


class A(Base):
    def __init__(self, a_name):
        print("enter A")
        self.a_name = a_name
        # print(id(self))  # 注意这里的self是D的实例，不是A的
        super(A, self).__init__("from_a")  # 注意！！！这里的super(A, self)其实调用的是B的__init__方法
        print("leave A")

    # def call(self):
    #     print("A call()")


class B(Base):
    def __init__(self, b_name):
        print("enter B")
        self.b_name = b_name
        super(B, self).__init__("from_b")
        print("leave B")

    def call(self):
        super().call()
        print("B call()")


class D(A, B):
    def __init__(self, d_name):
        print("enter D")
        self.d_name = d_name
        super(D, self).__init__("from_d")
        print("leave D")


if __name__ == "__main__":
    print("初始化顺序为")
    d = D("d_name")
    print("初始化结束")
    print(id(d))
    print("---" * 30)
    print(d.__class__.mro())
