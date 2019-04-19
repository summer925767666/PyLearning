""""
py函数
1、可以直接对形参赋值，而不必按照参数列表位置对应，如sum（i2=10,i1=1)
2、调用时参数缺省的情况，或者说形参可以赋默认值
"""
x = 1  # 全局变量x


def sum(i1, i2=10):  # def关键字+函数名+（参数列表）
    result = 0
    for i in range(i1, i2 + 1):
        result += i
    return result


def testvar1():
    x = 2


def testvar2():
    global x
    x = 2


def fib(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    print("sum form 1 to 10 is", sum(1, 10))  # 标准调用
    print("sum form 1 to 10 is", sum(1))  # 缺省时调用，i2使用默认值
    print("sum form 11 to 20 is", sum(i2=20, i1=11))  # 直接对形参赋值

    testvar1()  # 局部变量x
    print("x=%d" % x)
    testvar2()  # 全局变量x
    print("x=%d" % x)

    print(fib(10))

main()
