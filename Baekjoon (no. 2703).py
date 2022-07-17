# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/17
# Problem: Baekjoon no. 2703, Cryptoquote
https://www.acmicpc.net/problem/2703
# Solution: Using for loop and list to solve this problem

n=int(input())
a=[] # 5,4,3,2,1
for i in range(n):    
    x=int(input())
    a.append(x)
    
for i in range(len(a)): # 0 - 1,2,3,4,5 / 1 - 1,2,3,4,5 / 2- 1,2,3,4,5 
    for j in range(len(a)):
        if a[i] < a[j]
    
   
