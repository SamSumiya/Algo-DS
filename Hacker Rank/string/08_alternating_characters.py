def alternatingCharacters(s):
    i = 0
    count = 0

    while i < len(s) - 1:
        if s[i] == s[i+1]:
            count += 1
        i += 1

    return count
