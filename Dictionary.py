# 使用{key：value，key：value，...}的形式创建字典
# key必须是不可变且不能重复的（如不能使用列表，但可以使用元祖），值可以是任意类型

def dict():
    my_dict={"zhao":123,"qian":456,"sun":789} #定义
    print(my_dict) #字典是无序的
    print(my_dict["zhao"])#使用[key]来引用
    my_dict["li"]=111

    print(len(my_dict))
    print("zhao" in my_dict)

def dict_reverse():
    dict={'a':123,'b':234,'c':123}

    rvsd_dict={}

    for k,v in dict.items():
        if v in rvsd_dict:
            rvsd_dict[v].append(k)
        else:
            rvsd_dict[v] = [k]

    print(dict)
    print(rvsd_dict)

#集合set，无重复的值的元素组合
#性质为数学上的集合
#与列表的对比，主要是
# 1、无重复元素
# 2、使用in判断时速度比较快，时间复杂度在o（1），跟字典的key值判断一样
def setfunc():
    x=set()
    x.add(1)
    x.add(2)
    x.remove(1)


def main():
    dict_reverse()
main()
