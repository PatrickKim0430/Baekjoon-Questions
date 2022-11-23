# Programmer:  Patrick Junhee Kim 
# Date: 2022/11/23
# Problem: Baekjoon no. 14425, Set of strings
https://www.acmicpc.net/problem/14425
# Solution: Using import sys concept to solve this problem

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0

S = {input().strip() for _ in range(n)}

for j in range(m):
    if input().strip() in S:cnt+=1
