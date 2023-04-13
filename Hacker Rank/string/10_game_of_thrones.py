def gameOfThrones(s):

    hashmap = {}
    count = 0

    for el in s:
        if el not in hashmap:
            hashmap[el] = 1
        else:
            hashmap[el] += 1

    for _, value in hashmap.items():
        if value % 2 == 1:
            count += 1

    if count < 2:
        return ('YES')
    else:
        return ('NO')
