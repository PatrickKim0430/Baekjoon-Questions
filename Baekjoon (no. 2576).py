# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/21
# Problem: Baekjoon no. 2576, odd number
https://www.acmicpc.net/problem/2576
# Solution: Using for loop and if, else statement concept to solve this problem

a=[]
for i in range(7):
    n=int(input())
    if n % 2 ==1:
        a.append(n)

if a: 
    print(sum(a))
    print(min(a))
else:
    print("-1")
