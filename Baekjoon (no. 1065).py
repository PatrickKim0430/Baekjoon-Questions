# Programmer:  Patrick Junhee Kim 
# Date: 2022/10/9
# Problem: Baekjoon no. 1065, arithmetic sequence
https://www.acmicpc.net/problem/1065
# Solution: Using int(input()), for loop concept to solve this problem

n = int(input())

a= 0
for i in range(1, n+1):
    n_list = list(map(int, str(i)))
    if i < 100:
        a += 1  
    elif n_list[0]-n_list[1] == n_list[1]-n_list[2]:
        a += 1  
print(a)
