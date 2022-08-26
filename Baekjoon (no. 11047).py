# Programmer:  Patrick Junhee Kim 
# Date: 2022/8/26
# Problem: Baekjoon no. 11047, Coin 0
https://www.acmicpc.net/problem/11047
# Solution: Using int(input()), for statement concept to solve this problem

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
