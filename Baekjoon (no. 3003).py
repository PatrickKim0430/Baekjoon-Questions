# Programmer:  Patrick Junhee Kim 
# Date: 2022/9/24
# Problem: Baekjoon no. 3003, Queen, King, Bishop, Rook, Knight 
https://www.acmicpc.net/problem/10162
# Solution: Using int(input()), statement concept to solve this problem

cp = [1, 1, 2, 2, 2, 8]
li = list(map(int, input().split()))
for i in range(6):
    print(cp[i]-li[i], end=' ')
