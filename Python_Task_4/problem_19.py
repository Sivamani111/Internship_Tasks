# Problem Name: collections.Counter()

# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

n = int(input())
rooms = list(map(int, input().split()))
customers = int(input())

total = 0

for i in range(customers):
    size, price = map(int, input().split())

    if size in rooms:
        total += price
        rooms.remove(size)

print(total)
