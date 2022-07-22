# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/22
# Problem: Baekjoon no. 1978, Prime number
https://www.acmicpc.net/problem/1978
# Solution: Using int(input()), statement concept to solve this problem

n=int(input()) # 4
num=list(map(int,input().split(" "))) # [1, 3, 5, 7]
a=0

for i in num: 
    if i <= 1: 
        continue 
    for j in range(2,i+1):
        if i%j == 0:
            if i == j:
                a = a +1 
            break 
print(a)    
