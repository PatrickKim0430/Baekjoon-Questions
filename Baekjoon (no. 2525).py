# Programmer:  Patrick Junhee Kim 
# Date: 2022/9/27
# Problem: Baekjoon no. 2525, oven clock
https://www.acmicpc.net/problem/2525
# Solution: Using input().split() and if statement concept to solve this problem

H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)
