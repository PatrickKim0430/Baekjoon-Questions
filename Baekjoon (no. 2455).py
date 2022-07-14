# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/14
# Problem: Baekjoon no. 2455, Train problem
https://www.acmicpc.net/problem/2455
# Solution: Using for loop and list concept to solve this problem

people_nums = []
people = 0 

for _ in range(4) :
    out_num, in_num = map(int,input().split())
    people += in_num
    people -= out_num 

    people_nums.append(people) 
    
print(max(people_nums))
