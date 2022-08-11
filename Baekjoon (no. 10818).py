# Programmer:  Patrick Junhee Kim 
# Date: 2022/8/12
# Problem: Baekjoon no. 10818, Maximum and Minimum 
https://www.acmicpc.net/problem/10818
# Solution: Using int(input()), sort concept to solve this problem

n=int(input())
L=list(map(int,input().split()))
L.sort()
print(L[0],L[-1])
