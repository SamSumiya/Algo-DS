def camelcase(s):
    counts = 1 
    
    for val in s:
        if val == val.upper():
                counts += 1
    return counts