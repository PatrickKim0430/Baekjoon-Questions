# Programmer:  Patrick Junhee Kim 
# Date: 2022/10/31
# Problem: Baekjoon no. 2775
https://www.acmicpc.net/problem/2775
# Solution: Using for loop concept to solve this problem


t = int(input())

for _ in range(t):  
    floor = int(input())  
    num = int(input())  
    f0 = [x for x in range(1, num+1)]  
    for k in range(floor):  
        for i in range(1, num): 
            f0[i] += f0[i-1]  
    print(f0[-1])  
