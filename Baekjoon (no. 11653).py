# Programmer:  Patrick Junhee Kim 
# Date: 2022/9/12
# Problem: Baekjoon no. 11653, Factorization 
https://www.acmicpc.net/problem/11653
# Solution: Using while loop and int(input()) to solve this problem

N = int(input())  
d = 2  

while N != 1:
    if N % d != 0:
        d += 1
    else:
        N //= d
        print(d)
