# Programmer:  Patrick Junhee Kim 
# Date: 2022/8/14
# Problem: Baekjoon no. 14681, quadrant
https://www.acmicpc.net/problem/14681
# Solution: Using int(input()), if statement concept to solve this problem

a=int(input())
b=int(input())

if a > 0 and b >0:
    print("1")
elif a <0 and b > 0:
    print("2")
elif a < 0 and b < 0: 
    print("3")
else:
    print("4")
