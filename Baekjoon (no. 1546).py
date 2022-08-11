# Programmer:  Patrick Junhee Kim 
# Date: 2022/8/11
# Problem: Baekjoon no. 1546, Average
https://www.acmicpc.net/problem/1546
# Solution: Using int(input()), for loop concept to solve this problem

n=int(input())
a=list(map(int,input().split()))
m=max(a)
result=0

for i in range(0,n):
    a[i]=a[i]/m*100
    result=result+a[i]
    
result=result/n
print(result)
