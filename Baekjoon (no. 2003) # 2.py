# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/17
# Problem: Baekjoon no. 2003, Sum of numbers#2
https://www.acmicpc.net/problem/2003
# Solution: Using while loop and if statement to solve this problem

N, M = map(int,input().split())
List = list(map(int,input().split()))

Left = 0
Right = 0
cnt = 0
sum2 = 0

while Left <= N:
    if sum2 == M: #
        sum2 = sum2 - List[Right] 
        Right = Right+ 1
        cnt = cnt +1
    elif sum2 > M:
        sum2 = sum2 - List[Right] 
        Right = Right +1 
    else: # sum2 < M:
        if Left == N :
            break
        sum2 = sum2 + List[Left] 
        Left = Left + 1 
print(cnt)
    
   
