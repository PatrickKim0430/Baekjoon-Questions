# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/8
# Problem: USACO bronze problem (2017 january contest, problem 2) 
# Baekjoon 14456 https://www.acmicpc.net/problem/14456
# Solution: Using if, elif, and else statements to solve this problem



n=int(input())
# 1: scissors
# 2: hoof
# 3: papers
count=0
loss=0
for i in range(n):
    a,b=input().split()
    a=int(a)
    b=int(b)
    if a == 1 and b ==3:
        count = count +1
    elif a == 1 and b==2:
        loss=loss+1
    elif a == 2 and b == 1:
        count = count +1
    elif a ==2 and b ==3:
        loss = loss+1
    elif a == 3 and b == 2:
        count = count +1
    elif a ==3 and b ==1:
        loss = loss +1
        
if loss > count: 
    print(loss)
else:
    print(count)
