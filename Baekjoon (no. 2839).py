# Programmer:  Patrick Junhee Kim 
# Date: 2022/8/17
# Problem: Baekjoon no. 2839, Sugar deliver
https://www.acmicpc.net/problem/2839
# Solution: Using while loop and if statement to solve this problem

n=int(input())
a=0

#18
while n >= 0:
    if n % 5 == 0: 
       a= a+ n//5 
       print(a)
       break
    n=n-3
    a=a+1
else:
    print("-1")
