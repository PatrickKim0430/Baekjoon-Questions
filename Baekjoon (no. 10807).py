# Programmer:  Patrick Junhee Kim 
# Date: 2022/10/26
# Problem: Baekjoon no. 10807, Counting numbers
https://www.acmicpc.net/problem/10807
# Solution: Using list, input().split() concept to solve this problem

N = int(input())
list = list(map(int, input().split()))
a = int(input())
print(list.count(a))
