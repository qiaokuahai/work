#  元类看似复杂，其实很简单，注意一下当前obj的class的mro顺序就很好理解了
def get_obj_fields(curr_obj, *args, **kwargs):
    print("I am sing, my obj_cls is %s" % curr_obj.__class__.__name__)
    obj_attr_names = dir(curr_obj)
    res_dict = {name: getattr(curr_obj, name) for name in obj_attr_names if not(name.startswith("__"))}
    return res_dict


class ConstType(type):
    #  有装饰器的性质，程序在载入的时候先执行
    def __new__(mcs, name, bases, attrs):
        print("enter metaclass ConstType")
        # 在元类中将函数get_obj_fields加入到Person类中
        attrs["get_obj_fields"] = get_obj_fields
        meta_cls = type.__new__(mcs, name, bases, attrs)
        # meta_cls = super(ConstType, mcs).__new__(mcs, name, bases, attrs)  # 返回一个类，而不是类实例
        print("leave metaclass ConstType")
        return meta_cls


class Person(metaclass=ConstType):
    name = 'person'

    def __new__(cls, *args, **kwargs):
        obj = super(Person, cls).__new__(cls)  # 返回一个本类的实例
        return obj

    def __init__(self, school, score):
        self.school = school
        self.score = score


print("调用之前")

if __name__ == "__main__":
    p = Person("beida", 100)
    res = p.get_obj_fields()
    print(res)
