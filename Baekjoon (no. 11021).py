# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/13
# Problem: Baekjoon no. 11021, A+B -7 
https://www.acmicpc.net/problem/11021
# Solution: Using input.split() concept to solve this problem

n=int(input())
for i in range(n):
    a,b=input().split()
    a=int(a)
    b=int(b)
    ans=a+b
    print("Case #%s: %s"%(i+1, ans ))
