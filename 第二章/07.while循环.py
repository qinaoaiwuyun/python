# while案例:技术按1-100之间所有偶数的累加之和
# total=0 # 记录累加之和
# i = 1 # 循环开始数字
# while I <=100:
#     if i%2==0:
#         total += i
#     i += 1
# print(f"1-100之间所有偶数的累加之和:{total}")


# t = int(input())
# i = 0
# while i < t:
#     a, b, c = map(int, input(). split())
#     if a > c and b > c:
#         print((a + b) / c)
#     elif a > b and c > b:
#         print((a + c) / c)
#     else:
#         print((b + c) / a)
#     i += 1



# n=int(input())
# for i in range(n):
#     for m in range(i):
#         print(m,end=" ")
#     print()



n=input()
m=input()
for i in range(10):
	if i%2==1:
		for j in range(10):
			if j%2==0:
				print(n,end=" ")
			else:
				print(m,end=" ")
	else:
		for j in range(10):
			if j%2==1:
				print(n,end=" ")
			else:
				print(m,end=" ")
	print()