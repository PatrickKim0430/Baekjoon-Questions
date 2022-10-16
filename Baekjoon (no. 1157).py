# Programmer:  Patrick Junhee Kim 
# Date: 2022/10/16
# Problem: Baekjoon no. 1157, Studying words
https://www.acmicpc.net/problem/1157
# Solution: Using list and for loop to solve this problem

n = input().upper()
n_list = list(set(n))

cnt = []
for i in n_list:
  count = n.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(n_list[(cnt.index(max(cnt)))])
