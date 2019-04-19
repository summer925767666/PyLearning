"""
列表与字符串
字符串是特殊的列表，只存储字符元素的列表
字符串是静态的，列表是动态的
"""

lst = [5.4, "hello", 2]  # 使用[]创建并初始化
print(lst[:])

print(lst[0])  # 使用[index]取值

lst[0] = "chris"  # 可直接赋值
print(lst[:])

lst[1:3] = ["hello", "world"]  # 使用切片的方式赋值

print(lst[:])

#1233444
