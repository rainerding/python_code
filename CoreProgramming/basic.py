"""
==========我的名片==========
姓名: 顾安老师
email: wt_poppies@sina.com
QQ:xxxxxxx
手机号:172xxxxxx
公司地址:湖南省长沙市xxxx
===========================
"""
# print('==========我的名片==========')
# print('姓名: 顾安老师')
# print('email: wt_poppies@sina.com')
# print('QQ:xxxxxxx')
# print('手机号:172xxxxxx')
# print('公司地址:湖南省长沙市xxxx')
# print('===========================')

# aduit and female and (benke or yanjiu) and not age<18

# print((18 <= age <=60 and gender == "male") or (18 <= age <=50 and gender == "female"))

# age = input('请输入年龄：')

# length = input('请输入身高（cm）：')
# if float(length) <= 150:
#     print('无需买票')
# else:
#     print('需要买票')

# balance = 2
#
# seats = False
#
# if balance >= 2:
#     print('可以乘车')
#     if seats:
#         print('可以落座')
#     else:
#         print('没有座位')
# else:
#     print('余额不足，不能乘车')


# import random
#
# player = input('请输入：剪刀（0） 石头（1） 布（2）')
# player = int(player)
#
# computer = random.randint(0,2)
#
# if ((player == 1) and (computer == 0)) or ((player == 0) and (computer == 2)) or ((player == 2) and (computer == 1)):
#     print('哈哈，你赢了')
#
# elif player == computer:
#     print('平局')
#
# else:
#     print('不好意思，你输了')

# 计算1~100的累积和（包含1和100）
# i = 1
# j = 0
# while i <= 100:
#     j += i
#     i += 1
# print(j)

# 计算1~100之间偶数的累积和（包含1和100）
# i = 1
# j = 0
# while i <= 100:
#     if i % 2 == 0:
#         j += i
#     i += 1
# print(j)

# 实现计算1~100之间能被3整除且能够7整除的所有数之和
# i = 1
# k = 0
# while i <= 100:
#     if (i%3 == 0) and (i%7 == 0):
#         k = k + i
#     i = i + 1
# print(k)


# i = 1
# while i <= 10:
#     j = i**2
#     print(f'{i}--->{j}')
#     i += 1

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print('*',end= '')
#         j += 1
#     print('\n',end='')
#     i += 1

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print('X*Y=Z',end=' ')
#         j += 1
#     print('\n')
#     i += 1

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print(f'{j}*{i}=Z',end=' ')
#         j += 1
#     print('\n')
#     i += 1

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f'{j}*{i}={i*j}',end=' ')
#         j += 1
#     print('\n')
#     i += 1


# my_str= """
# sxasxsaxa
# csacsasac
# cscsc asascsa adas
# :''''c
# """
# # y = my_str.rfind('df')
# # g = my_str.replace('d','h')  #全部替换
# # b = my_str.replace('d','h',1)  #只替换1个
# #
# # print(y)
# # print(g)
# # print(b)
#
# b = my_str.splitlines()
# print(b)
# print(my_str.isalpha())
# print(my_str.isdigit())
# print(my_str.isalnum())


# join 在字符串/可迭代的对象 的每个元素后面加上 str，得到一个新字符串

# mydd = '1231231'
# cd = 'dcd'
#
# f = mydd.join(cd)
# print(f)
# 定义一个集合
# nums = {100, 200, 200, 300, 300, 300}

# # 测试数据类型真的是集合吗？
# print(type(nums))
#
# # 遍历
# for temp in nums:
#     print(temp)
# # 集合会打乱顺序
#
# jjjson = {
#     "ss": 4,
#     "ff": "e"
# }
# print(jjjson.get('gg','ffffff'))


# 推导式

# a = [x for x in range(4)]
# print(a)
# a = [x for x in range(0,3)]
# print(a)
#
# a = [x for x in range(3, 4)]
# print(a)
#
# a = [x for x in range(3, 19)]
# print(a)
#
# a = [x for x in range(3, 19, 2)]
# print(a)
# 一个 list 里面的元素,比如[1,2,3,...100]变成[[1,2,3],[4,5,6]....]

#
# a = [i for i in range(1,101)]
# b = [a[x:x+3] for x in range(0,len(a),3)]
#
# print(a)
# print(b)

# 推导式外层是啥，结果就是啥类型，[],{}.()

#快速生成一个1~10内key可以1时value为2，key为2时value3....依次类推的字典

# a = {x:x+1 for x in range(1,11)}
# print(a)

# a = [{x:x**2} for x in range(10)]
# print(a)

#拆包
a,b,c,d = (1,2,3,4)
print(a,b,c,d)








