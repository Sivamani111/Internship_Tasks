# Problem Name: Find the Runner-Up Score!

# HackerRank Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
num = list(map(int,input().split()))
num = sorted(set(num))
print(num[-2])
