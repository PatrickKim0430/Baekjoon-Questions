# Programmer:  Patrick Junhee Kim 
# Date: 2022/10/12
# Problem: Baekjoon no. 2675, Repetition String
https://www.acmicpc.net/problem/2675
# Solution: Using for loop concept to solve this problem

t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)
