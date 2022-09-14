# Programmer:  Patrick Junhee Kim 
# Date: 2022/9/14
# Problem: Baekjoon no. 2747, Fibonacci number
https://www.acmicpc.net/problem/2747
# Solution: Using int(input()), for loop concept to solve this problem

n = int(input())
a, b = 0, 1
for i in range(n):
    a, b = b, a+b
print(a
