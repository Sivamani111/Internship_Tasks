# Problem Name: Check Subset

# HackerRank Link: https://www.hackerrank.com/challenges/py-check-subset/problem


for _ in range(int(input())):
    n = int(input())
    A = set(map(int, input().split()))

    m = int(input())
    B = set(map(int, input().split()))

    print(A.issubset(B))
