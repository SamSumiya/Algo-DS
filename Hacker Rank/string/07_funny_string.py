def funnyString(s):
    reversed_str = s[::-1]
    i = 0

    while i < len(s) - 1:
        if abs(ord(s[i]) - ord(s[i+1])) != abs(ord(reversed_str[i]) - ord(reversed_str[i+1])):
            return 'Not Funny'

        i += 1

    return 'Funny'
