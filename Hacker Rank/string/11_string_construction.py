def stringConstruction(s):
    sub_string = ''
    
    for el in s: 
        if el not in sub_string: 
                sub_string += el

    return len(sub_string)
