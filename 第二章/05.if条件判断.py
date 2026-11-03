# # if条件判断,如果分数超过600,我就去清华
# num = input("你的高考分数是:")
# if int(num) > 600:
#     print("你能去读清华")
# if int(num) <600:
#     print("你不能去清华")
# print("-----------")

# bilibili登录
# zh = input("请输入你的账号:")
# mm = input("请输入你的密码:")
# if int(zh) == 1234567890 and int(mm) == 88888888:
#     print("登录成功")
# if int(zh) != 1234567890 or int(mm) != 88888888:
#     print("账号或密码错误")

# if...else...
# zh = input("请输入你的账号: ")
# mm = input("请输入你的密码: ")
# if int(zh) == 1234567890 and int(mm) == 88888888:
#     print("登录成功")
# else:
#     print("账号或密码错误")

# 练习
# 需求1.根据用户输入的数字,判断该数字是奇数还是偶数
# num = input("请输入一个数字:")
# if int(num)%2 == 0:
#     print("该数字是偶数")
# else:
#     print("该数字是奇数")
#
# # 需求2.根据用户输入的年龄,判断该用户是否成年
# num = input("请输入你的年龄:")
# if int(num) >=18:
#     print("你已成年")
# else:
#     print("你还未成年")

# #需求3.根据用户输入的数字,判断该数字是正数还是负数(不考虑0)
# num = input("请输入一个数字:")
# if int(num) >0:
#     print(f"{num}是正数")
# if int(num) <0:
#     print(f"{num}是负数")

# # 需求4.根据用户输入的考试分数,判断该分数是否及格
# num = input("请输入你的分数")
# if int(num) >=60:
#     print("及格")
# else:
#     print("不及格")
#
# #  if...elif...else...
# # 需求5.根据用户输入的数字,判断该数字是正数还是负数,还是0
# num = input("请输入一个数字:")
# if int(num) >0:
#     print(f"{num}是正数")
# elif int(num) <0:
#     print(f"{num}是负数")
# else:
#     print(f"{num}是0")

# 案例:根据输入的用户名和密码进行系统登录 --- admin/666888    root/547527    zhangsan/123456
# a = input("请输入你的用户名:")
# b = input("请输入你的密码:")
# if (a == "admin" and b == "666888") or (a == "root" and b == "547527") or (a == "zhangsan" and b == "123456"):
#     print("登录成功")
# else:
#     print("用户米或密码错误")

# elif 没有数量限制
# a = input("请输入你的用户名:")
# b = input("请输入你的密码:")
# if (a == "admin" and b == "666888") or (a == "root" and b == "547527") or (a == "zhangsan" and b == "123456"):
#      print("登录成功")
# elif (a == "root" and b == "547527"):
#      print("登录成功")
# elif (a == "zhangsan" and b == "123456"):
#      print("登录成功")
# else:
#     print("用户米或密码错误")

# 案例:根据输入的考试成绩,判断成绩等级
# num = input("请输入你的分数:")
# if int(num) >= 85
#     print("你的成绩是优秀")
# elif int(num) < 85 and int(num) >= 60:
#     print("你的成绩是及格")
# else:
#     print("你的成绩是不及格")

# 案例:购物折扣计算:根据输入的购物车的商品总额,以及如下的折扣规则,计算实际的金额
# num = input("请你输入你购物车的商品总额:")
# if int(num) >= 500:
#     print("实际应付的金额是",int(num)*0.8)
# elif 300 <= int(num) < 500:
#     print("实际应付的金额是",int(num)*0.9)
# elif 100 <= int(num) < 300:
#     print("实际应付的金额是", int(num) * 0.95)
# else:
#     print(f"实际应付的金额是{num}")

# 案例:根据输入的用电度数,计算电费
num = int(input("请输入你的用电度数:"))
if num <= 2880:
    print("你的电费是:",num*0.4883)
elif 2880 < num < 4800:
    print("你的电费是:", 2800*0.4883+(num-2880)*0.5383)
else:
    print("你的电费是:",2880*0.4883+1920*0.5383+(num-4800)*0.7883)