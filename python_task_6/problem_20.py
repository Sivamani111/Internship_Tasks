# Problem Name: Validating phone numbers

# HackerRank Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com

import re

for _ in range(int(input())):
    n = input().strip()
    if re.fullmatch(r"[789]\d{9}", n):
        print("YES")
    else:
        print("NO")
