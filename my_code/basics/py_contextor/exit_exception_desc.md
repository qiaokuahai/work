```
Python特性（十四）：context manager的__exit__方法
在context manager对象的__exit__方法中，共有三个参数，保存with语句在运行过程中的异常信息。其中：

第1个参数保存异常类型；
第2个参数保存异常对象的值；
第3个参数保存异常的traceback信息。
```

###  具体代码

``` 
class MyContextManager:  
  
    def __enter__(self):  
        print "Entering my conext manager"  
          
  
    def __exit__(self, exc_t, exc_v, traceback):  
        print "Exiting my conext manager"  
        print "Exception type:"  
        print exc_t  
        print "Exception value:"  
        print exc_v  
        print "Exception traceback:"  
        print traceback  
    
  
with MyContextManager():  
    print "In main block"  
    raise Exception("Exception raised in main block")  
    
```
##### 错误如下
```
Entering my conext manager  
In main block  
Exiting my conext manager  
Exception type:  
<type 'exceptions.Exception'>  
Exception value:  
Exception raised in main block  
Exception traceback:  
<traceback object at 0x0000000002AB0848>  
Traceback (most recent call last):  
  File "test.txt", line 30, in <module>  
    raise Exception("Exception raised in main block")  
Exception: Exception raised in main block
```

```

需要指出的是，只有在with语句块中抛出的异常才会交给__exit__方法处理。如果在contextmanager的初始化方法和__enter__方法中抛
出的异常，并不会交给__exit__方法处理，而是直接向外抛出。看下面的例子。

class MyContextManager:  
  
    def __init__(self):  
        print "Initializing my context manager"  
  
    def __enter__(self):  
        print "Entering my conext manager"  
        raise Exception("Exception raised in __enter__")  
  
    def __exit__(self, exc_t, exc_v, traceback):  
        print "Exiting my conext manager"  
        print "Exception type:"  
        print exc_t  
        print "Exception value:"  
        print exc_v  
        print "Exception traceback:"  
        print traceback  
    
  
with MyContextManager():  
    print "In main block"  

```
#####  报错信息
```
Initializing my context manager  
Entering my conext manager  
Traceback (most recent call last):  
  File "test.txt", line 31, in <module>  
    with MyContextManager():  
  File "test.txt", line 19, in __enter__  
    raise Exception("Exception raised in __enter__")  
Exception: Exception raised in __enter__  

注意：上面输出中虽然也打印了异常的traceback信息，但却不是__exit__方法打印的。

```


