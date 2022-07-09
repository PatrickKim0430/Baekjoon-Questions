# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/9
# Problem: Baekjoon no. 11047, coin 0  
https://www.acmicpc.net/problem/11047
# Solution: Using lists concepts to solve this problem

a,b=input().split()
a=int(a)
b=int(b)
l=[]
count=0
for i in range(a):
    n=int(input())
    l.append(n)
    
l.sort(reverse=True)

for i in l:
    count=count+(b//i)
    b=b%i

print(count)
