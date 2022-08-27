# Programmer:  Patrick Junhee Kim 
# Date: 2022/8/27
# Problem: Baekjoon no. 1934, the least common mulitiple
https://www.acmicpc.net/problem/1934
# Solution: Using while statement and int(input()) to solve this problem

num = int(input())
for i in range(num):
    a,b = map(int,input().split())
    A,B = a,b
    while a!=0:
        b = b%a
        a,b = b,a   
        # print(a,b)
    gcd = b
    lcm = A * B //b
    print(lcm)
    
