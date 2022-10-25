# Programmer:  Patrick Junhee Kim 
# Date: 2022/10/25
# Problem: Baekjoon no. 5597, Assignment
https://www.acmicpc.net/problem/5597
# Solution: Using list and for loop concept to solve this problem

s = [i for i in range(1,31)]

for _ in range(28):
    applied = int(input())
    s.remove(applied) 

print(min(s))
print(max(s))
