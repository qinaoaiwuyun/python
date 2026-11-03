# 需求:用户名密码登录,正确的用户名和密码为:admin/666888 zhangsan/123456 taoge/888666,输入错误五次,不允许再操作了
# num=0
# while num<5:
#     a=input("请输入你的用户名:")
#     b=input("请输入你的密码:")
#     if a==" " or b==" ":
#         continue
#     if (a=="admin" and b=="666888") or (a=="zhangsan" and b=="123456") or (a=="taoge" and b=="888666"):
#         print("登陆成功")
#         break
#     else:
#         print("登陆失败")
#         num+=1
#         m=5-num
#         print(f"你还有{m}次机会")




n=int(input())
m=list(map(int,input().split()))
c=n*(n+1)//2
h=c-sum(m)
print(h)

