from collections import Counter


def anagram(s):
    # Write your code here
    mid = len(s) // 2
    count = 0
    if len(s) % 2 == 1:
        return -1

    r = Counter(s[mid:]) - Counter(s[:mid])
    for _, val in r.items():
        count += val

    return count
