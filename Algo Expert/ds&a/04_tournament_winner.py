'''
    Tournament Winner

    approach: hashmap 

        iterate throught the length of competition list
        then we can use it to get the winning team
        first, we will need to get the results
            if the results[idx] is 0 then we will need to - 1 from it
            else we will need to + 1 to subtract 1 from it
        then we can get the right team by accessing the competitions[idx][result number]
        we will store each winning team to hashamp 
        and return the team has the higest value at the end

        max(iterable, *[, key, default])
        key is a function that will be applied to each item in the iterable and it returns a value based on the passed argument

        




'''


def tournamentWinner(competitions, results):
    hashmap = {}

    for i in range(len(competitions)):
        if results[i] == 1:
            p = competitions[i][results[i]-1]
        else:
            p = competitions[i][results[i]+1]
        if p not in hashmap:
            hashmap[p] = 1
        else: 
            hashmap[p] += 1
    print(hashmap.items())
    max_value = max(hashmap.items())
    max_value_2 = max(hashmap.items(), key = lambda x: x[1])
    print(max_value == max_value_2)
    print(max_value, max_value_2)
    return max_value_2[0]



competitions = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["Java", "C#"],
    ["C#", "HTML"],
    ["SQL", "C#"],
    ["HTML", "SQL"],
    ["SQL", "Python"],
    ["SQL", "Java"]
]
results = [0, 1, 1, 1, 0, 1, 0, 1, 1, 0]


r = tournamentWinner(competitions, results)
print(r)
