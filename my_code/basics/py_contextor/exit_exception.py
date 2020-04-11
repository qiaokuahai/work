import traceback


class MyContextManager:

    def __enter__(self):
        print("context_manager __enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        :param exc_type:  with语句出现的错误类型， Exception type: <class 'Exception'>
        :param exc_val: with语句出现的错误值，Exception value: Exception raised in main block
        :param exc_tb: 堆栈信息
        :return:
        """
        print("context_manager __exit__")
        print("Exception type: %s" % exc_type)
        print("Exception value: %s" % exc_val)
        print("Exception traceback: %s" % exc_tb)
        print(traceback.format_exc())


with MyContextManager():
    print("in with block")
    raise Exception("Exception raised in main block")
