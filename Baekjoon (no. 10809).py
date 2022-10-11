# Programmer:  Patrick Junhee Kim 
# Date: 2022/10/11
# Problem: Baekjoon no. 10809, Finding Alphabet
https://www.acmicpc.net/problem/10809
# Solution: Using input().split() concept to solve this problem

A = input()
N = list(range(97, 123))

for i in N:
    print(A.find(chr(i)))
