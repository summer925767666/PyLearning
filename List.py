"""
列表与字符串
字符串是特殊的列表，只存储字符元素的列表
字符串是静态的，列表是动态的
"""


# 列表功能演示
def list():
    lst = [5.4, "hello", 2]  # 使用[]创建并初始化,类型可以不同！！！

    print(lst[0])  # 使用[index]取值
    print(lst[-1])

    print(lst + ["chris"])  # 可以使用+拼接，不改变lst本身

    print(lst * 2)  # 重复

    lst[0] = "chris"  # 可直接赋值

    lst[1:3] = ["hello", "world"]  # 使用切片的方式赋值

    lst.append("chris")  # 追加一个元素
    lst.extend([1, 2, 3.4])  # 追加一个列表
    lst.insert(0, 100)  # 插入

    lst.pop()  # 删除最后一个元素
    lst.remove("chris")  # 删除指定元素
    lst.remove("hello")
    lst.remove("world")
    lst.remove("chris")

    lst.sort()  # py3中不支持str和int的排序
    lst.reverse()  # 逆序

    print(lst)


# 求平均数
def average():
    nums = []

    for i in range(0, 5):
        num = (float)(input())
        nums.append(num)

    print("the average is", sum(nums) / len(nums))


# 交换列表元素
def swap(lst, a, b):
    """"
    函数调用时，列表类似与c语言的指针，可以实现地址传
    因为py没有指针，所以地址传递只能用这种形式
    这一点确实没法跟c语言抗衡
    """
    tmp = lst[a]
    lst[a] = lst[b]
    lst[b] = tmp


# 列表解析、列表推导
def listdeduce():
    """"
    一种简易的在原列表的基础上生成新列表的方法
    类似与c#的foreach linq语句；或者理解为一种语法糖
    格式：[exp for x in list]，对list里的每一个元素x，执行表达式exp操作
    """
    students = [["zhao", 80], ["qian", 70], ["sun", 90]]

    print(1.0 * sum([x[1] for x in students]) / len(students))  # 求平均分

    students.sort(key=lambda x: x[1])  # ！！！使用匿名lambda函数
    # students.sort(key=f，reverse=true) #表示逆序排列
    print(students)


# lambda函数，匿名函数，py支持函数式编程
def lambdafunc():
    f = lambda x: x ** 2  # 返回x平方的匿名函数

    print(f(8))


def main():
    listdeduce()
    # lambdafunc()


main()
