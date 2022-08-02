# Programmer:  Patrick Junhee Kim 
# Date: 2022/8/2
# Problem: Baekjoon no. 2609, the greatest common denominator and the least common multiple
https://www.acmicpc.net/problem/2609
# Solution: Using int(input()), function concept to solve this problem

a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))
