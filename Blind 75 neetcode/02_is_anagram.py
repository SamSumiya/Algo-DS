'''
    Subset of Arrays and Hashing
    Link: https://leetcode.com/problems/valid-anagram/submissions/

    approach: hashmap
        create a new hashmap and populate it with the element as key and encounter times as value
        iterate through the t and this time minus 1 if hashmap has the same value or get create a new key with value 1
        at the end, loop through the value and if the value is not 0 
        we know that the two string dont match 

'''


def isAnagram_hashmap(s, t):
    hashmap = {}

    for el in s:
        if el not in hashmap:
            hashmap[el] = 1
        else:
            hashmap[el] += 1
    print(hashmap)
    for el in t:
        if el in hashmap:
            hashmap[el] -= 1
        else:
            hashmap[el] = 1

    print(hashmap)
    for key, value in hashmap.items():
        if value != 0:
            return False

    return True


def isAnagram_hashmap_sort(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    if len(sorted_s) != len(sorted_t):
        return False
    i = 0

    while i < len(sorted_s):
        if sorted_s[i] != sorted_t[i]:
            return False
        i += 1
    return True
