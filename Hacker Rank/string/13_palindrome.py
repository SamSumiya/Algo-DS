from collections import Counter

def gameOfThrones(s):
    # Write your code here
    hash_map = Counter(s)
    counts = 0 

    for _, val in hash_map.items(): 
        if val % 2 == 1: 
                counts += 1
    if counts > 1: 
        return False
    return True

s = 'cdefghmnopqrstuvw'
print(gameOfThrones(s))