'''


'''



def fib_iter(num): 
    if num == 1: return 1
    if num == 2: return 1
    output = 0 
    l = [1, 1]
    i = 0 
    while num > 2: 
        output = l[i] + l[i+1]
        l.append(output)      
        i += 1 
        num -= 1

    return l

result = fib_iter(9)
print(result)


