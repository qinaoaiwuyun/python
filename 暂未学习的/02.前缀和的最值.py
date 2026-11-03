# 过程中最大和最小值
# mx=-float('inf')
# mn=float('inf')
# mx=max(mn,s)
# mn=min(mn,s)


n=3
for i in range(n):
    print(" "*(n-i-1),"*"*(2*i+1))
for i in range(n-1,0,-1):
    print(" "*(n-i),"*"*(2*i-1))

# 保留三位小数
a=input().strip()
x=float(a[::-1])
print(f"{x:.2f}")
print("{:.2f}".format(x))

# 输出07
n=7
print(f"{n:02d}")
print("{:02d}".format(n))

# 前缀和数组
pre = [0]*(n+1)
for i in range(n):
    pre[i+1] = pre[i]+a[i]
# a[l]-a[r]的总和
sum=pre[r+1]-pre[l]
