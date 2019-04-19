"""
程序结构
1、selection statement
2、loop statement
"""

# 1、selection statement

grade = int(input("grade="))
sex = str(input("sex="))
count = 0

if (grade >= 60):
    if (sex == "女"):  # nested
        count += 1
    else:
        pass
else:
    pass

print("count=", count)

# 1.1、multi-branch select statement

count90 = count80 = count70 = count60 = countless60 = 0

if grade >= 90:
    count90 += 1
elif grade >= 80:
    count80 += 1
elif grade >= 70:
    count70 += 1
elif grade >= 60:
    count60 += 1
else:
    countless60 += 1

print(count90, count80, count70, count60, countless60)

# 2、loop statement
#  2.1、while statement
num = 0
grade = 0
count = 0

while (num < 5):
    if (int(input("NO." + str(num + 1) + "\'s grade=")) >= 60):
        count += 1
    else:
        pass
    num += 1

print("the number of passed students is ", count)

# 2.2、for statement
for num in range(0, 5):
    if (int(input("NO." + str(num + 1) + "'s grade=")) >= 60):
        count += 1
    else:
        pass

print("the number of passed students is ", count)

# example
# range(a,b) is a,a+1,...,b-1
# range(b) is equal to range(0,b)
# range(a,b,k) is a,a+k,a+2k,...b-x
# range(a,b,-1) is decreased

# eg1.用for循环实现e
e = 0
n = 0
fac = 1
temp = 1

while (temp >= 1e-6):
    e += temp  # 累加每一项的值

    n += 1  # 计数器加1
    fac *= n  # 计算阶乘
    temp = 1.0 / fac  # 计算阶乘的倒数，也就是单独项

print("the value of e is %-.5f" % e)
