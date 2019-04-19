"""
列表与字符串
字符串是特殊的列表，只存储字符元素的列表
字符串是静态的，列表是动态的
"""


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


def main():
    # 列表功能演示
    # list()

    # 求平均数
    nums = []

    for i in range(0, 5):
        num = (float)(input())
        nums.append(num)

    print("the average is", sum(nums) / len(nums))


main()
