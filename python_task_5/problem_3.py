# Problem Name: Mutations

# HackerRank Link: https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    result = []

    for i in range(position):
        result.append(string[i])

    result.append(character)

    for i in range(position + 1, len(string)):
        result.append(string[i])

    return "".join(result)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
