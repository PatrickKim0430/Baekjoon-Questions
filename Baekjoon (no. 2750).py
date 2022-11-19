# Programmer:  Patrick Junhee Kim 
# Date: 2022/11/19
# Problem: Codeup no. 2750, number sort
https://codeup.kr/problem.php?id=2750
# Solution: Using for loop and input() to solve this problem

x = int(input())
num_list = []
for i in range(x):
    num_list.append(int(input()))
num_list1 = sorted(num_list)
for i in range(len(num_list)):
    print(num_list1[i])
