# Problem Name: Word Order

# HackerRank Link: https://www.hackerrank.com/challenges/word-order/problem

n = int(input())
words = []
for i in range(n):
    word = input()
    words.append(word)

print(len(set(words)))

for word in dict.fromkeys(words):
    print(words.count(word), end=" ")
