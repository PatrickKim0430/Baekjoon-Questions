# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/7 
# Problem: Baekjoon 7568 / body size
  https://www.acmicpc.net/problem/7568
# Solution: Using python and list concept to solve this problem

n=int(input())
s=[]

for i in range(n):
    w,h=input().split()
    w=int(w)
    h=int(h)
    s.append((w,h))
    
for i in s: 
    rank = 1 
    for j in s: 
        if i[0] < j[0] and i[1] < j[1]:
               rank = rank +1 
    print(rank, end = " ")
