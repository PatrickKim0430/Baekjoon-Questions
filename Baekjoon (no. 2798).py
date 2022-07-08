# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/8 
# Problem: Baekjoon 2798 https://www.acmicpc.net/problem/2798
# Solution: Using list and for loops to solve this problem


N,M=input().split() #5, 21
N=int(N)
M=int(M)

L=list(map(int,input().split()))
ans=0
# 3 cards, 3 possibles 
for i in range(len(L)): #5 times, 0, 1, 2, 3, 4 
    for j in range(i+1, len(L)): 
        for k in range(j+1, len(L)):
            if L[i] + L[j]+ L[k] >  M:
                 continue
            else:
                ans=max(ans, L[i] + L[j] + L[k])
                
                
    

print(ans)
