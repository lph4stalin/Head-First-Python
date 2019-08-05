# 使用类允许你将行为和状态打包在一个对象中。
# 行为：可以理解为函数，是一个完成某种工作的代码块
# 状态：可以理解成便利，是一个在类中存储值得位置。
# self 属性在整个类的范围内有效，也就是它在方法中被改变了，也会作用于方法之外。


class CountFromBy:
    def __init__(self, v=0, i=1):
        self.val = v
        self. incr = i

    def increase(self):
        self.val += self.incr

    def __repr__(self):
        return str(self.val)


k = CountFromBy()
k.increase()
print(k)
