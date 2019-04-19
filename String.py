# 字符串的使用
# 可以使用单引号或者双引号
# 可以使用三引号，保留字符串的所有信息
# 转义字符

# 字符串函数
# len（）求字符串的长度
# + 字符串的拼接
# * 字符串的重复
# in 字符串子串判断
# for 语句，循环字符串的每一个字符
# [] 字符串索引 既可以从前往后（从0开始递增），也可以从后往前（从-1开始递减）
# [start:finish:step] 字符串切片
# replace(old,new)

# 统计元音字母的个数
def vowels_count(string):
    count = 0
    for c in string:  # 使用for对字符串遍历
        if c in "AEIOUaeiou":  # 使用in判断是否为子串！！！
            count += 1

    return count


# 字符切片
def strsplit():
    s = "hello world"
    print(s[4])
    print(s[0:5])
    print(s[:])  # 默认值为从开始到结尾
    print(s[::2])  # step表示步长
    print(s[::-1])  # 字符串的逆序！！！python好强大


# 人名游戏
def namegame():
    f = open("names")  # open()打开文件，f为文件句柄
    for line in f:  # 按行遍历文件
        name = line.strip()  # 删除回车
        name = name.title()  # 首字母大写，其余字母小写
        print(name)
        # print (line.strip().title())  #链式编程

    f.close()


# 回文的判断

# 字符串的比较

# 格式化输出format(),比较复杂，举例如下
def testformat():
    """"
    {fieldname:align width.precision type}"""
    import math
    # 无参数
    print("pi is {}".format(math.pi))

    # 9表示占9个字符位，不足的用空格补齐，超过的话不做限制；.5表示精度,f为浮点数
    print("pi is {:9.5}".format(math.pi))

    # 保留5为小数，而不对整体的占位长度限制
    print("pi is {:.5}".format(math.pi))

    # e表示科学计数法
    print("pi is {:.5e}".format(math.pi))


# 正则表达式
""""
.表示任意字符
\d+表示一系列数字
[a-z]表示一个小写字母
...
"""


def is_include():
    import re  # 引入正则表达模块
    pattern = "a.g"  # 创建模式

    f = open("names")
    for line in f:
        name = line.strip()
        res = re.search(pattern, name)  # 判断字符串中是否存在自定义的模式
        if res:
            print(name)


def main():
    # 统计元音字母的个数
    # string = input("输入字符串：")
    string = "ChrisZhang"
    # print(vowels_count(string))

    # 字符串切片
    # strsplit()

    # 人名游戏
    # namegame()

    # 格式化输出
    # testformat()

    # 正则表达式
    is_include()


main()
