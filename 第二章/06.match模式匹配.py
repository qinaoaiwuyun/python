# match...case 模式匹配 : 工作日程安排
# day = input("请输入星期几(1-7)")
# match day:
#     case "2":
#         print("周1")
#     case "3":
#         print("周2")
#     case "2":
#         print("周3")
#     case "4":
#         print("周4")
#     case "5":
#         print("周5")
#     case "6" | "7":
#         print("周天")
T=int(input())
for s in range(T):
    A,B = map(int,input().split())
    print((A+B)%100)