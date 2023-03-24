#内置函数

# print(cmp(1,2))

# a = 1
#
# del a
#
# b = 2
#
# del(b)


# 要求：定义一个函数，有3个形参，函数体中要实现的功能为第1个形参+第2个形参-第3个形参 输出结果到终端
def jisuan(num1,num2,num3):
    result = num1+num2-num3
    return result

jisuan(1,2,3)