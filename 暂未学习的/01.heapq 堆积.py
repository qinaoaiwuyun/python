# 开头:import heapq
# import heapq
# heap=[]
# for num in a:
#     heapq.heappush(heap,num) # 小堆积
#     heapq.heappush(heap,-num) # 用符号模拟大堆积
#
#     cur=-heapq.heappop(heap) # 取出最小值,加-,相当于取出最大值.注意:取出相当于删除,需重新添加
#     heapq.heappush(heap,-new_num) # 重新添加一个数




n,m=map(int,input().split())
a=list(map(int,input().split()))
q=0
for i in range(n-1):
    if sum(a[0:i+1])%m==sum(a[i+1:n+1])%m:
        q+=1
print(q)