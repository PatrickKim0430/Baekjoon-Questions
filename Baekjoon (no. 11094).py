# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/13
# Problem: Baekjoon no. 11094, Simon says
https://www.acmicpc.net/problem/11094
# Solution: Using for loop concept to solve this problem

n=int(input())

for i in range(n):
    simon=input()
    if "Simon says" in simon:
        print(simon[10:])
