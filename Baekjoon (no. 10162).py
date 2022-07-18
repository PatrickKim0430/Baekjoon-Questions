# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/18
# Problem: Baekjoon no. 10162, microwave
https://www.acmicpc.net/problem/10162
# Solution: Using int(input()), statement concept to solve this problem

n=int(input())

if n % 10 != 0:
    print("-1")
else:
    #670
    five = n // 300 # 2  
    one = (n%300) // 60 # 60//60 = 1 
    ten = (n%300)%60 // 10  
    print(five, one, ten) 
