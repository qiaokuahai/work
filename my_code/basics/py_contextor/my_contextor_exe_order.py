class MyContext:
    """
    执行的顺序是：首先执行__init__， 然后执行__enter__，然后执行with中的具体逻辑，最后执行__exit__
    """
    def __init__(self):
        print("I am in __init__")

    def __enter__(self):
        print("I am in __enter__")
        return list("abcde")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("I am in __exit__")


with MyContext() as obj:
    print("start")
