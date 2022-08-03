# Programmer:  Patrick Junhee Kim 
# Date: 2022/8/3
# Problem: Baekjoon no. 2739, multiplication table
https://www.acmicpc.net/problem/2793
# Solution: Using int(input()), for loop to solve this problem

n = int(input())

for i in range(1,10):  # 1~9
    print(n, '*', i, '=', n*i)
