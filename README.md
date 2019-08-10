# Head First Python
 学习《Head First Python》的练习


关于类：
使用类允许你将行为和状态打包在一个对象中。
行为：可以理解为函数，是一个完成某种工作的代码块
状态：可以理解成便利，是一个在类中存储值得位置。
self 属性在整个类的范围内有效，也就是它在方法中被改变了，也会作用于方法之外。


关于代码重复使用：
方案1：包装成函数，重复调用
方案2：修饰器

修饰器举例：
1，如何创建一个函数？
def function():

2，如何把一个函数作为参数传递到另一个函数？
函数和其他对象一样，可以通过函数名传递到另一个函数作为参数。

3，如何从函数返回一个函数？
同理，直接使用函数名返回一个函数。
例如：
def apply(func, value):
    return func(value)
函数嵌套函数：
def outer():
    def inner():
        print('This is inner.')
    print('This is outer, invoking inner.')
    inner()
预期输出：
>>>'This is outer, invoking inner.'
>>>'This is inner.'
问题在于，很难想到什么时候需要使用嵌套函数。这种技术更常见的用法是，外围函数使用 return 语句返回嵌套函数作为它的返回值。
从函数返回函数：
def outer():
    def inner():
        print('This is inner.')
    print('This is outer, invoking inner.')
    return inner()
return 语句不调用 inner，而是把 inner 函数对象返回给调用代码。

4，如何处理任意数量和类型的函数参数？
使用 *args 来接收多个参数（作为列表打包传入也可）, **kwargs 接收关键字参数（也可作为字典传入）。
多参数和关键字参数例子：
def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()

def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()

def myfunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()

修饰器：
1，修饰器是一个函数。它下面的函数称为被修饰的函数
2，修饰器取被修饰函数为参数。
3，修饰器返回一个新函数。
4，修饰器维护被修饰函数的签名。修饰器需要确保它返回的函数与被修饰函数具有同样的参数（个数和类型一致）。函数参数的个数和类型称为签名。
"""
一个修饰器模板
def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Code to execute BEFORE calling the decorated function.

        # 2. Call the decorated function as required, returning its
        #    results if needed.
             return func(*args, **kwargs)

        # 3. Code to execute INSTEAD of calling the decorated function.
    return wrapper
"""

存储服务器端状态，可以用 session：1，设置 secret_key（密钥，用于加密 cookie）；2，session 是一个类似字典的对象，里面存储了状态信息
