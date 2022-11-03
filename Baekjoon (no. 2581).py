# Programmer:  Patrick Junhee Kim 
# Date: 2022/11/3
# Problem: Baekjoon no. 2581, prime number
https://www.acmicpc.net/problem/2581
# Solution: Using for loop and int(input()) to solve this problem

n1 = int(input())
n2= int(input())

list = []
for num in range(n1, n2):
    error = 0
    if num > 1 :
        for i in range(2, num): 
            if num % i == 0:
                error += 1
                break  
        if error == 0:
            sosu_list.append(num)  
            
if len(list) > 0 :
    print(sum(list))
    print(min(list))
else:
    print(-1)
