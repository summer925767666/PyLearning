"""
py基本数据类型
1、字符型
2、整型
3、浮点型
4、布尔型
5、复数型
"""

# type()函数表示
print(type("小明"))
print(type(1))
print(type(1.2))
print(type(True))
print(type(1 + 1j))

# 不同类型的对象的不同的运算规则
print(1 + 2)  # 整型
print("1" + "2")  # 字符型
print('1' + '2')

# 算术运算
print(3 * 3)
print(2 ** 3)  # 指数运算
print(5 / 9)  # py2中/表示取整，但是py3中/不是
print(10 % 3)  # 取余

# 模块
import math

print(math.e)

# 关系运算、逻辑运算
print(1 == 2)
print(not 1 == 2)
print(1 == 2 or 3 == 3)

# 标准输入input() 读入字符串
radius = float(input('Radius='))
area = math.pi * radius ** 2
print('the area of the circle is', area)
