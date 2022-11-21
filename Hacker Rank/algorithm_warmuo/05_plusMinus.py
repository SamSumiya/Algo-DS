def plusMinus(arr):
    pos = 0 
    zero = 0 
    ne = 0 
    size = len(arr)
    output = [] 
    for val in arr: 
        if val > 0: 
                pos += 1 
        elif val < 0: 
                ne += 1 
        else: 
                zero += 1 
        
    output.append('{:.6f}'.format(pos / size))
    output.append(round(ne / size, 6))
    output.append(round(zero / size, 6))
    