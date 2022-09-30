# Programmer:  Patrick Junhee Kim 
# Date: 2022/9/30
# Problem: Baekjoon no. 25304, receipt
https://www.acmicpc.net/problem/25304
# Solution: Using input().split() and for loop concept to solve this problem


total= int(input())
type= int(input())
 
sum=0 
 

for i in range(type):
    a,b= map(int,input().split())
    sum += a*b
     
if total==sum: print("Yes")
else: print("No")
