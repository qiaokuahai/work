
global_dict = {}


def store_data(name):
    def print_log(func):
        def wrapper(*args, **kwargs):
            print("before ->>>")
            res = func(*args, **kwargs)
            print("after ->>>")
            return res
        global_dict[name] = wrapper
        return wrapper
    return print_log


@store_data("eat")
def eat():
    print("yes")
    return "yes"


res = eat()
print(res)
