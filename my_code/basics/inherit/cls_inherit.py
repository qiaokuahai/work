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
        Base.__init__(self)
        print("leave A")

    # def call(self):
    #     print("A call()")


class B(Base):
    def __init__(self, b_name):
        print("enter B")
        self.b_name = b_name
        print("leave B")

    def call(self):
        super().call()
        print("B call()")


class D(A, B):
    def __init__(self, d_name):
        print("enter D")
        self.d_name = d_name
        A.__init__(self, "a_name")
        B.__init__(self, "b_name")
        print("leave D")


if __name__ == "__main__":
    print("初始化顺序为")
    d = D("d_name")
    print("初始化结束")
    print("---" * 30)
    print(d.__class__.mro())
