def compareTriplets(a, b):
    alice = 0 
    bob = 0 
    
    i = 0
    while i < len(a):
        if a[i] < b[i]: 
                alice += 1
        elif a[i] > b[i]: 
                bob += 1 
        i += 1 
    return [bob, alice]
