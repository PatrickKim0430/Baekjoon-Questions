# Programmer:  Patrick Junhee Kim 
# Date: 2022/10/1
# Problem: Baekjoon no. 4678, Self number
https://www.acmicpc.net/problem/4678
# Solution: Using set(), for loop to solve this problem

numbers = set(range(1, 10000))
remove_set = set()  
for num in numbers :
    for n in str(num):
        num += int(n)
    remove_set.add(num) 

self_numbers = numbers - remove_set  
for self_num in sorted(self_numbers): 
    print(self_num)
