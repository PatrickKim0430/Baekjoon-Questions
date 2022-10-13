# Programmer:  Patrick Junhee Kim 
# Date: 2022/10/13
# Problem: Baekjoon no. 5622, dial
https://codeup.kr/problem.php?id=5622
# Solution: Using if statement and input() to solve this problem

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
n = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            n += dial.index(i)+3
print(n)
