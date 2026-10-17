# Problem Name: The Minion Game

# HackerRank Link: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    Stuart = 0
    Kevin = 0
    vowels = "AEIOU"
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            Kevin += n - i
        else:
            Stuart += n - i

    if Stuart > Kevin:
        print("Stuart", Stuart)
    elif Kevin > Stuart:
        print("Kevin", Kevin)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
