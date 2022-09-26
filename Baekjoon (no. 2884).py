# Programmer:  Patrick Junhee Kim 
# Date: 2022/9/26
# Problem: Baekjoon no. 2884, Alarm Clock
https://www.acmicpc.net/problem/2884
# Solution: Using int(input()), if statement concept to solve this problem


Hour, Min = map(int, input().split())

if Min < 45 :	 
    if Hour == 0 :	
        Hour = 23
        Min += 60
    else :	
        Hour -= 1	
        Min += 60
        
print(Hour, Min-45)	 
