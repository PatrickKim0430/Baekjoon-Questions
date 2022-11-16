# Programmer:  Patrick Junhee Kim 
# Date: 2022/11/16
# Problem: Baekjoon no. 2292, honeycomb
https://www.acmicpc.net/problem/2292
# Solution: Using input().split() and while loop concept to solve this problem

n = int(input())

nums_pileup = 1  
cnt = 1
while n > nums_pileup :
    nums_pileup += 6 * cnt  
    cnt += 1 
print(cnt)
