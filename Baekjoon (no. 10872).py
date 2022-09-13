# Programmer:  Patrick Junhee Kim 
# Date: 2022/9/13
# Problem: Codeup no. 10872, factorial
https://codeup.kr/problem.php?id=10872
# Solution: Using if statement and input() to solve this problem

n = int(input())

result = 1
if n > 0:
    for i in range(1, n+1):
        result *= i
print(result)
