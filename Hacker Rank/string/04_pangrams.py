import string 

def pangrams(s):
    s = s.lower()
    alphabets = list(string.ascii_lowercase)
    indices = [0 for _ in range(26)]
    for el in s:
        if el in alphabets:
                indices[alphabets.index(el)] = 1

    if list(set(indices)) == [1]:
        return('pangram')
    else: 
        return('not pangram')